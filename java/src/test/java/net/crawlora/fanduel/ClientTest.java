package net.crawlora.fanduel;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(72, Client.OPERATION_IDS.size());
        assertEquals(List.of("fanduel-casino-categories", "fanduel-casino-category", "fanduel-casino-game", "fanduel-racing-carryover-pools", "fanduel-racing-filters", "fanduel-racing-horse", "fanduel-racing-past-race", "fanduel-racing-past-races", "fanduel-racing-past-tracks", "fanduel-racing-race", "fanduel-racing-races", "fanduel-racing-results", "fanduel-racing-search", "fanduel-racing-track", "fanduel-racing-tracks", "fanduel-racing-wager-types", "fanduel-research", "fanduel-research-article", "fanduel-research-articles", "fanduel-research-author", "fanduel-research-authors", "fanduel-research-featured-articles", "fanduel-research-fixtures", "fanduel-research-nfl-schedule", "fanduel-research-player-news", "fanduel-research-projection-slates", "fanduel-research-projection-tables", "fanduel-research-projections", "fanduel-research-quick-picks-daily", "fanduel-research-sports", "fanduel-research-sub-categories", "fanduel-sportsbook-autocomplete", "fanduel-sportsbook-builder", "fanduel-sportsbook-builder-events", "fanduel-sportsbook-builder-quotes", "fanduel-sportsbook-competition", "fanduel-sportsbook-event", "fanduel-sportsbook-event-box-score", "fanduel-sportsbook-event-play-by-play", "fanduel-sportsbook-event-players", "fanduel-sportsbook-event-score", "fanduel-sportsbook-event-stats", "fanduel-sportsbook-events-status", "fanduel-sportsbook-home", "fanduel-sportsbook-league", "fanduel-sportsbook-live", "fanduel-sportsbook-live-count", "fanduel-sportsbook-live-data", "fanduel-sportsbook-live-scores", "fanduel-sportsbook-market-prices", "fanduel-sportsbook-parlays", "fanduel-sportsbook-player", "fanduel-sportsbook-player-news", "fanduel-sportsbook-player-props", "fanduel-sportsbook-player-stats", "fanduel-sportsbook-players", "fanduel-sportsbook-promotions", "fanduel-sportsbook-schedule", "fanduel-sportsbook-search", "fanduel-sportsbook-search-tabs", "fanduel-sportsbook-sport", "fanduel-sportsbook-sports", "fanduel-sportsbook-standings", "fanduel-sportsbook-stats", "fanduel-sportsbook-team-depth-chart", "fanduel-sportsbook-team-news", "fanduel-sportsbook-team-odds", "fanduel-sportsbook-team-roster", "fanduel-sportsbook-team-schedule", "fanduel-sportsbook-team-stats", "fanduel-sportsbook-teams", "fanduel-sportsbook-trending"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("fanduel-casino-category", Map.ofEntries(Map.entry("category", "all-games"), Map.entry("q", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            // This operation has no path parameters to encode.
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("casinoCategory", Map.class).invoke(client, Map.ofEntries(Map.entry("category", "all-games"), Map.entry("q", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("fanduel-casino-categories", Map.of()));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("fanduel-casino-category", Map.ofEntries(Map.entry("category", "all-games"), Map.entry("q", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("fanduel-casino-category", Map.ofEntries(Map.entry("category", "all-games"), Map.entry("q", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("fanduel-casino-categories", Map.ofEntries(Map.entry("region", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("fanduel-casino-category", Map.ofEntries(Map.entry("category", "all-games"), Map.entry("q", "value &/one"))));
    }
}
