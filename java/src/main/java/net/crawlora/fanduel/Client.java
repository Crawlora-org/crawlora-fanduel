package net.crawlora.fanduel;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the FanDuel endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 72;
    public static final List<String> OPERATION_IDS = List.of(
            "fanduel-casino-categories",
            "fanduel-casino-category",
            "fanduel-casino-game",
            "fanduel-racing-carryover-pools",
            "fanduel-racing-filters",
            "fanduel-racing-horse",
            "fanduel-racing-past-race",
            "fanduel-racing-past-races",
            "fanduel-racing-past-tracks",
            "fanduel-racing-race",
            "fanduel-racing-races",
            "fanduel-racing-results",
            "fanduel-racing-search",
            "fanduel-racing-track",
            "fanduel-racing-tracks",
            "fanduel-racing-wager-types",
            "fanduel-research",
            "fanduel-research-article",
            "fanduel-research-articles",
            "fanduel-research-author",
            "fanduel-research-authors",
            "fanduel-research-featured-articles",
            "fanduel-research-fixtures",
            "fanduel-research-nfl-schedule",
            "fanduel-research-player-news",
            "fanduel-research-projection-slates",
            "fanduel-research-projection-tables",
            "fanduel-research-projections",
            "fanduel-research-quick-picks-daily",
            "fanduel-research-sports",
            "fanduel-research-sub-categories",
            "fanduel-sportsbook-autocomplete",
            "fanduel-sportsbook-builder",
            "fanduel-sportsbook-builder-events",
            "fanduel-sportsbook-builder-quotes",
            "fanduel-sportsbook-competition",
            "fanduel-sportsbook-event",
            "fanduel-sportsbook-event-box-score",
            "fanduel-sportsbook-event-play-by-play",
            "fanduel-sportsbook-event-players",
            "fanduel-sportsbook-event-score",
            "fanduel-sportsbook-event-stats",
            "fanduel-sportsbook-events-status",
            "fanduel-sportsbook-home",
            "fanduel-sportsbook-league",
            "fanduel-sportsbook-live",
            "fanduel-sportsbook-live-count",
            "fanduel-sportsbook-live-data",
            "fanduel-sportsbook-live-scores",
            "fanduel-sportsbook-market-prices",
            "fanduel-sportsbook-parlays",
            "fanduel-sportsbook-player",
            "fanduel-sportsbook-player-news",
            "fanduel-sportsbook-player-props",
            "fanduel-sportsbook-player-stats",
            "fanduel-sportsbook-players",
            "fanduel-sportsbook-promotions",
            "fanduel-sportsbook-schedule",
            "fanduel-sportsbook-search",
            "fanduel-sportsbook-search-tabs",
            "fanduel-sportsbook-sport",
            "fanduel-sportsbook-sports",
            "fanduel-sportsbook-standings",
            "fanduel-sportsbook-stats",
            "fanduel-sportsbook-team-depth-chart",
            "fanduel-sportsbook-team-news",
            "fanduel-sportsbook-team-odds",
            "fanduel-sportsbook-team-roster",
            "fanduel-sportsbook-team-schedule",
            "fanduel-sportsbook-team-stats",
            "fanduel-sportsbook-teams",
            "fanduel-sportsbook-trending"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("fanduel-casino-categories", new Operation("fanduel-casino-categories", "GET", "/fanduel/casino/categories", Map.ofEntries(Map.entry("region", new Param("region", "query", false, "string", List.of("mi", "on"), "csv"))), List.of("application/json")));
        operations.put("fanduel-casino-category", new Operation("fanduel-casino-category", "GET", "/fanduel/casino/category", Map.ofEntries(Map.entry("region", new Param("region", "query", false, "string", List.of("mi", "on"), "csv")), Map.entry("category", new Param("category", "query", true, "string", List.of("all-games", "new", "slots", "double-your-bet-category", "jackpots", "daily-jackpots", "hot-slots", "classic-reels-category", "bonus-buy-category", "high-limit-category", "spooky-slots-category", "exclusives", "pick-play", "arcade", "blackjack", "baccarat", "roulette", "table", "livecasino", "online-casino-favorites", "explore-videos", "motorcity-favorites", "fallsview-favourites-category", "the-wolf-den-category", "sports-central"), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("provider", new Param("provider", "query", false, "string", List.of(), "csv")), Map.entry("badge", new Param("badge", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-casino-game", new Operation("fanduel-casino-game", "GET", "/fanduel/casino/game", Map.ofEntries(Map.entry("region", new Param("region", "query", false, "string", List.of("mi", "on"), "csv")), Map.entry("game", new Param("game", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-carryover-pools", new Operation("fanduel-racing-carryover-pools", "GET", "/fanduel/racing/carryover-pools", Map.ofEntries(Map.entry("status", new Param("status", "query", false, "string", List.of("O", "IC", "SK", "RO"), "csv")), Map.entry("track", new Param("track", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-filters", new Operation("fanduel-racing-filters", "GET", "/fanduel/racing/filters", Map.of(), List.of("application/json")));
        operations.put("fanduel-racing-horse", new Operation("fanduel-racing-horse", "GET", "/fanduel/racing/horse", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-past-race", new Operation("fanduel-racing-past-race", "GET", "/fanduel/racing/past-race", Map.ofEntries(Map.entry("date", new Param("date", "query", true, "string", List.of(), "csv")), Map.entry("track", new Param("track", "query", true, "string", List.of(), "csv")), Map.entry("number", new Param("number", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-past-races", new Operation("fanduel-racing-past-races", "GET", "/fanduel/racing/past-races", Map.ofEntries(Map.entry("date", new Param("date", "query", true, "string", List.of(), "csv")), Map.entry("track", new Param("track", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-past-tracks", new Operation("fanduel-racing-past-tracks", "GET", "/fanduel/racing/past-tracks", Map.ofEntries(Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("track", new Param("track", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-race", new Operation("fanduel-racing-race", "GET", "/fanduel/racing/race", Map.ofEntries(Map.entry("track", new Param("track", "query", true, "string", List.of(), "csv")), Map.entry("number", new Param("number", "query", true, "string", List.of(), "csv")), Map.entry("include", new Param("include", "query", false, "string", List.of("handicapping", "timeform", "pool_grids"), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-races", new Operation("fanduel-racing-races", "GET", "/fanduel/racing/races", Map.ofEntries(Map.entry("track", new Param("track", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("exclude_country", new Param("exclude_country", "query", false, "string", List.of(), "csv")), Map.entry("race_type", new Param("race_type", "query", false, "string", List.of("T", "H", "Q", "L"), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("O", "IC", "SK", "RO"), "csv")), Map.entry("open", new Param("open", "query", false, "boolean", List.of(), "csv")), Map.entry("within_minutes", new Param("within_minutes", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("mtp", "post_time", "race_number"), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-results", new Operation("fanduel-racing-results", "GET", "/fanduel/racing/results", Map.ofEntries(Map.entry("track", new Param("track", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("exclude_country", new Param("exclude_country", "query", false, "string", List.of(), "csv")), Map.entry("race_type", new Param("race_type", "query", false, "string", List.of("T", "H", "Q", "L"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-search", new Operation("fanduel-racing-search", "GET", "/fanduel/racing/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("runner", "jockey", "trainer", "owner"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("name", "last_event"), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-track", new Operation("fanduel-racing-track", "GET", "/fanduel/racing/track", Map.ofEntries(Map.entry("code", new Param("code", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-tracks", new Operation("fanduel-racing-tracks", "GET", "/fanduel/racing/tracks", Map.ofEntries(Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("exclude_country", new Param("exclude_country", "query", false, "string", List.of(), "csv")), Map.entry("race_type", new Param("race_type", "query", false, "string", List.of("T", "H", "Q", "L"), "csv")), Map.entry("code", new Param("code", "query", false, "string", List.of(), "csv")), Map.entry("finished", new Param("finished", "query", false, "boolean", List.of(), "csv")), Map.entry("featured", new Param("featured", "query", false, "boolean", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("name", "mtp", "wagerable_mtp", "ivr"), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-racing-wager-types", new Operation("fanduel-racing-wager-types", "GET", "/fanduel/racing/wager-types", Map.of(), List.of("application/json")));
        operations.put("fanduel-research", new Operation("fanduel-research", "GET", "/fanduel/research", Map.of(), List.of("application/json")));
        operations.put("fanduel-research-article", new Operation("fanduel-research-article", "GET", "/fanduel/research/article", Map.ofEntries(Map.entry("article", new Param("article", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-articles", new Operation("fanduel-research-articles", "GET", "/fanduel/research/articles", Map.ofEntries(Map.entry("sport", new Param("sport", "query", false, "string", List.of("casino", "nascar", "ncaab", "f1", "ufc", "boxing", "ncaaf", "womenssoccer", "tv-and-podcast", "nba", "pga", "tennis", "nhl", "mma", "soccer", "fanduel-sportsbook-promo-codes", "sports-betting-101", "horse-racing", "wnba", "predicts", "mlb", "canada", "nfl"), "csv")), Map.entry("exclude_sport", new Param("exclude_sport", "query", false, "string", List.of(), "csv")), Map.entry("sub_category", new Param("sub_category", "query", false, "string", List.of(), "csv")), Map.entry("team", new Param("team", "query", false, "integer", List.of(), "csv")), Map.entry("player", new Param("player", "query", false, "integer", List.of(), "csv")), Map.entry("author", new Param("author", "query", false, "string", List.of(), "csv")), Map.entry("hero_type", new Param("hero_type", "query", false, "string", List.of("IMAGE", "JWPLAYER"), "csv")), Map.entry("published_after", new Param("published_after", "query", false, "string", List.of(), "csv")), Map.entry("published_before", new Param("published_before", "query", false, "string", List.of(), "csv")), Map.entry("hide_deprioritized", new Param("hide_deprioritized", "query", false, "boolean", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-author", new Operation("fanduel-research-author", "GET", "/fanduel/research/author", Map.ofEntries(Map.entry("author", new Param("author", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-authors", new Operation("fanduel-research-authors", "GET", "/fanduel/research/authors", Map.ofEntries(Map.entry("sport", new Param("sport", "query", false, "string", List.of("casino", "nascar", "ncaab", "f1", "ufc", "boxing", "ncaaf", "womenssoccer", "tv-and-podcast", "nba", "pga", "tennis", "nhl", "mma", "soccer", "fanduel-sportsbook-promo-codes", "sports-betting-101", "horse-racing", "wnba", "predicts", "mlb", "canada", "nfl"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-featured-articles", new Operation("fanduel-research-featured-articles", "GET", "/fanduel/research/featured-articles", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("casino", "nascar", "ncaab", "f1", "ufc", "boxing", "ncaaf", "womenssoccer", "tv-and-podcast", "nba", "pga", "tennis", "nhl", "mma", "soccer", "fanduel-sportsbook-promo-codes", "sports-betting-101", "horse-racing", "wnba", "predicts", "mlb", "canada", "nfl"), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-fixtures", new Operation("fanduel-research-fixtures", "GET", "/fanduel/research/fixtures", Map.ofEntries(Map.entry("sport", new Param("sport", "query", false, "string", List.of("nba", "nfl", "nhl", "mlb"), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-nfl-schedule", new Operation("fanduel-research-nfl-schedule", "GET", "/fanduel/research/nfl-schedule", Map.ofEntries(Map.entry("week", new Param("week", "query", true, "integer", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("PRE", "REGULAR", "POST"), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-player-news", new Operation("fanduel-research-player-news", "GET", "/fanduel/research/player-news", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("nfl", "nba", "mlb", "nhl"), "csv")), Map.entry("news_type", new Param("news_type", "query", false, "string", List.of("INJURY", "RECAP", "TRANSACTION", "LINEUP", "GAME_UPDATE", "OUTLOOK"), "csv")), Map.entry("team", new Param("team", "query", false, "integer", List.of(), "csv")), Map.entry("player", new Param("player", "query", false, "integer", List.of(), "csv")), Map.entry("position", new Param("position", "query", false, "string", List.of("G", "F", "C", "W", "D", "QB", "DB", "DL", "K", "LB", "OL", "P", "RB", "TE", "WR", "IF", "OF", "DH"), "csv")), Map.entry("include_non_primary", new Param("include_non_primary", "query", false, "boolean", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-quick-picks-daily", new Operation("fanduel-research-quick-picks-daily", "GET", "/fanduel/research/podcasts/quick-picks-daily", Map.ofEntries(Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-projection-slates", new Operation("fanduel-research-projection-slates", "GET", "/fanduel/research/projection-slates", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("mlb", "nba", "nfl", "nhl", "golf"), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("week", new Param("week", "query", false, "integer", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-projection-tables", new Operation("fanduel-research-projection-tables", "GET", "/fanduel/research/projection-tables", Map.ofEntries(Map.entry("sport", new Param("sport", "query", false, "string", List.of("mlb", "nba", "nfl", "nhl", "golf"), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-projections", new Operation("fanduel-research-projections", "GET", "/fanduel/research/projections", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("mlb", "nba", "nfl", "nhl", "golf"), "csv")), Map.entry("type", new Param("type", "query", true, "string", List.of("DAILY", "WEEKLY", "YEARLY", "REMAINING", "PPR", "SEASON_STATS"), "csv")), Map.entry("position", new Param("position", "query", false, "string", List.of("batters", "pitchers", "c", "1b", "2b", "3b", "ss", "of", "sp", "rp", "qb", "rb", "wr", "te", "flex", "k", "defense", "all", "pg", "sg", "guards", "sf", "pf", "forwards", "centers", "skaters", "goalies", "wingers", "d", "idp"), "csv")), Map.entry("scope", new Param("scope", "query", false, "string", List.of("TOTAL", "PER_GAME"), "csv")), Map.entry("slate_id", new Param("slate_id", "query", false, "string", List.of(), "csv")), Map.entry("event_id", new Param("event_id", "query", false, "string", List.of(), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("week", new Param("week", "query", false, "integer", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-sports", new Operation("fanduel-research-sports", "GET", "/fanduel/research/sports", Map.ofEntries(Map.entry("sport", new Param("sport", "query", false, "string", List.of("casino", "nascar", "ncaab", "f1", "ufc", "boxing", "ncaaf", "womenssoccer", "tv-and-podcast", "nba", "pga", "tennis", "nhl", "mma", "soccer", "fanduel-sportsbook-promo-codes", "sports-betting-101", "horse-racing", "wnba", "predicts", "mlb", "canada", "nfl"), "csv"))), List.of("application/json")));
        operations.put("fanduel-research-sub-categories", new Operation("fanduel-research-sub-categories", "GET", "/fanduel/research/sub-categories", Map.of(), List.of("application/json")));
        operations.put("fanduel-sportsbook-autocomplete", new Operation("fanduel-sportsbook-autocomplete", "GET", "/fanduel/sportsbook/autocomplete", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-builder", new Operation("fanduel-sportsbook-builder", "GET", "/fanduel/sportsbook/builder", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv")), Map.entry("experience", new Param("experience", "query", false, "string", List.of("yourway", "head-to-head", "player-combos", "bullseye", "player-podium", "or-bets"), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-builder-events", new Operation("fanduel-sportsbook-builder-events", "GET", "/fanduel/sportsbook/builder/events", Map.ofEntries(Map.entry("experience", new Param("experience", "query", false, "string", List.of("yourway", "head-to-head", "player-combos", "bullseye", "player-podium", "or-bets"), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-builder-quotes", new Operation("fanduel-sportsbook-builder-quotes", "GET", "/fanduel/sportsbook/builder/quotes", Map.ofEntries(Map.entry("ramp_event_id", new Param("ramp_event_id", "query", true, "integer", List.of(), "csv")), Map.entry("choice_id", new Param("choice_id", "query", true, "array", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-competition", new Operation("fanduel-sportsbook-competition", "GET", "/fanduel/sportsbook/competition", Map.ofEntries(Map.entry("event_type_id", new Param("event_type_id", "query", true, "string", List.of("6423", "1", "7522", "3", "7511", "7524", "2", "26420387", "2593174", "3503", "6", "5", "4", "8", "1477", "6422", "468328", "28608997", "998917", "4726642", "10", "2378961"), "csv")), Map.entry("competition_id", new Param("competition_id", "query", true, "integer", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv")), Map.entry("tab", new Param("tab", "query", false, "string", List.of(), "csv")), Map.entry("market_type", new Param("market_type", "query", false, "string", List.of(), "csv")), Map.entry("exclude_markets", new Param("exclude_markets", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-event", new Operation("fanduel-sportsbook-event", "GET", "/fanduel/sportsbook/event", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv")), Map.entry("tab", new Param("tab", "query", false, "string", List.of(), "csv")), Map.entry("market_type", new Param("market_type", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-event-box-score", new Operation("fanduel-sportsbook-event-box-score", "GET", "/fanduel/sportsbook/event/box-score", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-event-play-by-play", new Operation("fanduel-sportsbook-event-play-by-play", "GET", "/fanduel/sportsbook/event/play-by-play", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv")), Map.entry("current", new Param("current", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-event-players", new Operation("fanduel-sportsbook-event-players", "GET", "/fanduel/sportsbook/event/players", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-event-score", new Operation("fanduel-sportsbook-event-score", "GET", "/fanduel/sportsbook/event/score", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-event-stats", new Operation("fanduel-sportsbook-event-stats", "GET", "/fanduel/sportsbook/event/stats", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-events-status", new Operation("fanduel-sportsbook-events-status", "GET", "/fanduel/sportsbook/events/status", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "array", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-home", new Operation("fanduel-sportsbook-home", "GET", "/fanduel/sportsbook/home", Map.ofEntries(Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv")), Map.entry("tab", new Param("tab", "query", false, "string", List.of(), "csv")), Map.entry("competition_id", new Param("competition_id", "query", false, "integer", List.of(), "csv")), Map.entry("market_type", new Param("market_type", "query", false, "string", List.of(), "csv")), Map.entry("exclude_markets", new Param("exclude_markets", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-league", new Operation("fanduel-sportsbook-league", "GET", "/fanduel/sportsbook/league", Map.ofEntries(Map.entry("custom_page_id", new Param("custom_page_id", "query", true, "string", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv")), Map.entry("tab", new Param("tab", "query", false, "string", List.of(), "csv")), Map.entry("competition_id", new Param("competition_id", "query", false, "integer", List.of(), "csv")), Map.entry("market_type", new Param("market_type", "query", false, "string", List.of(), "csv")), Map.entry("exclude_markets", new Param("exclude_markets", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-live", new Operation("fanduel-sportsbook-live", "GET", "/fanduel/sportsbook/live", Map.ofEntries(Map.entry("event_type_id", new Param("event_type_id", "query", false, "string", List.of("6423", "1", "7522", "3", "7511", "7524", "2", "26420387", "2593174", "3503", "6", "5", "4", "8", "1477", "6422", "468328", "28608997", "998917", "4726642", "10", "2378961"), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv")), Map.entry("market_type", new Param("market_type", "query", false, "string", List.of(), "csv")), Map.entry("exclude_markets", new Param("exclude_markets", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-live-count", new Operation("fanduel-sportsbook-live-count", "GET", "/fanduel/sportsbook/live-count", Map.ofEntries(Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-live-data", new Operation("fanduel-sportsbook-live-data", "GET", "/fanduel/sportsbook/live-data", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-live-scores", new Operation("fanduel-sportsbook-live-scores", "GET", "/fanduel/sportsbook/live-scores", Map.ofEntries(Map.entry("event_id", new Param("event_id", "query", true, "array", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-market-prices", new Operation("fanduel-sportsbook-market-prices", "GET", "/fanduel/sportsbook/market-prices", Map.ofEntries(Map.entry("market_id", new Param("market_id", "query", true, "string", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-parlays", new Operation("fanduel-sportsbook-parlays", "GET", "/fanduel/sportsbook/parlays", Map.ofEntries(Map.entry("view", new Param("view", "query", false, "string", List.of("popular", "all", "next-to-start", "event"), "csv")), Map.entry("event_id", new Param("event_id", "query", false, "integer", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("PARLAY", "SGP", "SGP_PLUS"), "csv")), Map.entry("event_type_id", new Param("event_type_id", "query", false, "string", List.of("6423", "1", "7522", "3", "7511", "7524", "2", "26420387", "2593174", "3503", "6", "5", "4", "8", "1477", "6422", "468328", "28608997", "998917", "4726642", "10", "2378961"), "csv")), Map.entry("competition_id", new Param("competition_id", "query", false, "string", List.of(), "csv")), Map.entry("min_odds", new Param("min_odds", "query", false, "number", List.of(), "csv")), Map.entry("max_odds", new Param("max_odds", "query", false, "number", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-player", new Operation("fanduel-sportsbook-player", "GET", "/fanduel/sportsbook/player", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba"), "csv")), Map.entry("player", new Param("player", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-player-news", new Operation("fanduel-sportsbook-player-news", "GET", "/fanduel/sportsbook/player/news", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba"), "csv")), Map.entry("player", new Param("player", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-player-props", new Operation("fanduel-sportsbook-player-props", "GET", "/fanduel/sportsbook/player/props", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba"), "csv")), Map.entry("player", new Param("player", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-player-stats", new Operation("fanduel-sportsbook-player-stats", "GET", "/fanduel/sportsbook/player/stats", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba"), "csv")), Map.entry("player", new Param("player", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-players", new Operation("fanduel-sportsbook-players", "GET", "/fanduel/sportsbook/players", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba"), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-promotions", new Operation("fanduel-sportsbook-promotions", "GET", "/fanduel/sportsbook/promotions", Map.ofEntries(Map.entry("context", new Param("context", "query", false, "string", List.of("home", "league", "sport"), "csv")), Map.entry("custom_page_id", new Param("custom_page_id", "query", false, "string", List.of(), "csv")), Map.entry("event_type_id", new Param("event_type_id", "query", false, "string", List.of("6423", "1", "7522", "3", "7511", "7524", "2", "26420387", "2593174", "3503", "6", "5", "4", "8", "1477", "6422", "468328", "28608997", "998917", "4726642", "10", "2378961"), "csv")), Map.entry("tag", new Param("tag", "query", false, "string", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-schedule", new Operation("fanduel-sportsbook-schedule", "GET", "/fanduel/sportsbook/schedule", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football"), "csv")), Map.entry("week", new Param("week", "query", false, "string", List.of(), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("end_date", new Param("end_date", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-search", new Operation("fanduel-sportsbook-search", "GET", "/fanduel/sportsbook/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("all", "event", "competition"), "csv")), Map.entry("event_type_id", new Param("event_type_id", "query", false, "string", List.of("6423", "1", "7522", "3", "7511", "7524", "2", "26420387", "2593174", "3503", "6", "5", "4", "8", "1477", "6422", "468328", "28608997", "998917", "4726642", "10", "2378961"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-search-tabs", new Operation("fanduel-sportsbook-search-tabs", "GET", "/fanduel/sportsbook/search/tabs", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("tab", new Param("tab", "query", false, "string", List.of(), "csv")), Map.entry("pill", new Param("pill", "query", false, "string", List.of(), "csv")), Map.entry("start_index", new Param("start_index", "query", false, "integer", List.of(), "csv")), Map.entry("timezone", new Param("timezone", "query", false, "string", List.of(), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-sport", new Operation("fanduel-sportsbook-sport", "GET", "/fanduel/sportsbook/sport", Map.ofEntries(Map.entry("event_type_id", new Param("event_type_id", "query", true, "string", List.of("6423", "1", "7522", "3", "7511", "7524", "2", "26420387", "2593174", "3503", "6", "5", "4", "8", "1477", "6422", "468328", "28608997", "998917", "4726642", "10", "2378961"), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv")), Map.entry("tab", new Param("tab", "query", false, "string", List.of(), "csv")), Map.entry("competition_id", new Param("competition_id", "query", false, "integer", List.of(), "csv")), Map.entry("market_type", new Param("market_type", "query", false, "string", List.of(), "csv")), Map.entry("exclude_markets", new Param("exclude_markets", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-sports", new Operation("fanduel-sportsbook-sports", "GET", "/fanduel/sportsbook/sports", Map.ofEntries(Map.entry("state", new Param("state", "query", false, "string", List.of("ar", "az", "co", "ct", "dc", "ia", "il", "in", "ks", "ky", "la", "ma", "md", "mi", "mo", "mr", "nc", "nj", "ny", "oh", "on", "pa", "pr", "tn", "va", "vt", "wv", "wy"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-standings", new Operation("fanduel-sportsbook-standings", "GET", "/fanduel/sportsbook/standings", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-stats", new Operation("fanduel-sportsbook-stats", "GET", "/fanduel/sportsbook/stats", Map.ofEntries(Map.entry("competition_id", new Param("competition_id", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-team-depth-chart", new Operation("fanduel-sportsbook-team-depth-chart", "GET", "/fanduel/sportsbook/team/depth-chart", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv")), Map.entry("team", new Param("team", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-team-news", new Operation("fanduel-sportsbook-team-news", "GET", "/fanduel/sportsbook/team/news", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv")), Map.entry("team", new Param("team", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-team-odds", new Operation("fanduel-sportsbook-team-odds", "GET", "/fanduel/sportsbook/team/odds", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv")), Map.entry("team", new Param("team", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-team-roster", new Operation("fanduel-sportsbook-team-roster", "GET", "/fanduel/sportsbook/team/roster", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv")), Map.entry("team", new Param("team", "query", true, "string", List.of(), "csv")), Map.entry("injured_only", new Param("injured_only", "query", false, "boolean", List.of(), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of(), "csv")), Map.entry("position", new Param("position", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-team-schedule", new Operation("fanduel-sportsbook-team-schedule", "GET", "/fanduel/sportsbook/team/schedule", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv")), Map.entry("team", new Param("team", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-team-stats", new Operation("fanduel-sportsbook-team-stats", "GET", "/fanduel/sportsbook/team/stats", Map.ofEntries(Map.entry("league", new Param("league", "query", true, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv")), Map.entry("team", new Param("team", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-teams", new Operation("fanduel-sportsbook-teams", "GET", "/fanduel/sportsbook/teams", Map.ofEntries(Map.entry("league", new Param("league", "query", false, "string", List.of("nfl", "nba", "mlb", "college-football", "college-basketball"), "csv"))), List.of("application/json")));
        operations.put("fanduel-sportsbook-trending", new Operation("fanduel-sportsbook-trending", "GET", "/fanduel/sportsbook/trending", Map.ofEntries(Map.entry("enriched", new Param("enriched", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown FanDuel operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object casinoCategories(Map<String, ?> params) { return request("fanduel-casino-categories", params); }
    public Object casinoCategory(Map<String, ?> params) { return request("fanduel-casino-category", params); }
    public Object casinoGame(Map<String, ?> params) { return request("fanduel-casino-game", params); }
    public Object racingCarryoverPools(Map<String, ?> params) { return request("fanduel-racing-carryover-pools", params); }
    public Object racingFilters(Map<String, ?> params) { return request("fanduel-racing-filters", params); }
    public Object racingHorse(Map<String, ?> params) { return request("fanduel-racing-horse", params); }
    public Object racingPastRace(Map<String, ?> params) { return request("fanduel-racing-past-race", params); }
    public Object racingPastRaces(Map<String, ?> params) { return request("fanduel-racing-past-races", params); }
    public Object racingPastTracks(Map<String, ?> params) { return request("fanduel-racing-past-tracks", params); }
    public Object racingRace(Map<String, ?> params) { return request("fanduel-racing-race", params); }
    public Object racingRaces(Map<String, ?> params) { return request("fanduel-racing-races", params); }
    public Object racingResults(Map<String, ?> params) { return request("fanduel-racing-results", params); }
    public Object racingSearch(Map<String, ?> params) { return request("fanduel-racing-search", params); }
    public Object racingTrack(Map<String, ?> params) { return request("fanduel-racing-track", params); }
    public Object racingTracks(Map<String, ?> params) { return request("fanduel-racing-tracks", params); }
    public Object racingWagerTypes(Map<String, ?> params) { return request("fanduel-racing-wager-types", params); }
    public Object research(Map<String, ?> params) { return request("fanduel-research", params); }
    public Object researchArticle(Map<String, ?> params) { return request("fanduel-research-article", params); }
    public Object researchArticles(Map<String, ?> params) { return request("fanduel-research-articles", params); }
    public Object researchAuthor(Map<String, ?> params) { return request("fanduel-research-author", params); }
    public Object researchAuthors(Map<String, ?> params) { return request("fanduel-research-authors", params); }
    public Object researchFeaturedArticles(Map<String, ?> params) { return request("fanduel-research-featured-articles", params); }
    public Object researchFixtures(Map<String, ?> params) { return request("fanduel-research-fixtures", params); }
    public Object researchNflSchedule(Map<String, ?> params) { return request("fanduel-research-nfl-schedule", params); }
    public Object researchPlayerNews(Map<String, ?> params) { return request("fanduel-research-player-news", params); }
    public Object researchQuickPicksDaily(Map<String, ?> params) { return request("fanduel-research-quick-picks-daily", params); }
    public Object researchProjectionSlates(Map<String, ?> params) { return request("fanduel-research-projection-slates", params); }
    public Object researchProjectionTables(Map<String, ?> params) { return request("fanduel-research-projection-tables", params); }
    public Object researchProjections(Map<String, ?> params) { return request("fanduel-research-projections", params); }
    public Object researchSports(Map<String, ?> params) { return request("fanduel-research-sports", params); }
    public Object researchSubCategories(Map<String, ?> params) { return request("fanduel-research-sub-categories", params); }
    public Object sportsbookAutocomplete(Map<String, ?> params) { return request("fanduel-sportsbook-autocomplete", params); }
    public Object sportsbookBuilder(Map<String, ?> params) { return request("fanduel-sportsbook-builder", params); }
    public Object sportsbookBuilderEvents(Map<String, ?> params) { return request("fanduel-sportsbook-builder-events", params); }
    public Object sportsbookBuilderQuotes(Map<String, ?> params) { return request("fanduel-sportsbook-builder-quotes", params); }
    public Object sportsbookCompetition(Map<String, ?> params) { return request("fanduel-sportsbook-competition", params); }
    public Object sportsbookEvent(Map<String, ?> params) { return request("fanduel-sportsbook-event", params); }
    public Object sportsbookEventBoxScore(Map<String, ?> params) { return request("fanduel-sportsbook-event-box-score", params); }
    public Object sportsbookEventPlayByPlay(Map<String, ?> params) { return request("fanduel-sportsbook-event-play-by-play", params); }
    public Object sportsbookEventPlayers(Map<String, ?> params) { return request("fanduel-sportsbook-event-players", params); }
    public Object sportsbookEventScore(Map<String, ?> params) { return request("fanduel-sportsbook-event-score", params); }
    public Object sportsbookEventStats(Map<String, ?> params) { return request("fanduel-sportsbook-event-stats", params); }
    public Object sportsbookEventsStatus(Map<String, ?> params) { return request("fanduel-sportsbook-events-status", params); }
    public Object sportsbookHome(Map<String, ?> params) { return request("fanduel-sportsbook-home", params); }
    public Object sportsbookLeague(Map<String, ?> params) { return request("fanduel-sportsbook-league", params); }
    public Object sportsbookLive(Map<String, ?> params) { return request("fanduel-sportsbook-live", params); }
    public Object sportsbookLiveCount(Map<String, ?> params) { return request("fanduel-sportsbook-live-count", params); }
    public Object sportsbookLiveData(Map<String, ?> params) { return request("fanduel-sportsbook-live-data", params); }
    public Object sportsbookLiveScores(Map<String, ?> params) { return request("fanduel-sportsbook-live-scores", params); }
    public Object sportsbookMarketPrices(Map<String, ?> params) { return request("fanduel-sportsbook-market-prices", params); }
    public Object sportsbookParlays(Map<String, ?> params) { return request("fanduel-sportsbook-parlays", params); }
    public Object sportsbookPlayer(Map<String, ?> params) { return request("fanduel-sportsbook-player", params); }
    public Object sportsbookPlayerNews(Map<String, ?> params) { return request("fanduel-sportsbook-player-news", params); }
    public Object sportsbookPlayerProps(Map<String, ?> params) { return request("fanduel-sportsbook-player-props", params); }
    public Object sportsbookPlayerStats(Map<String, ?> params) { return request("fanduel-sportsbook-player-stats", params); }
    public Object sportsbookPlayers(Map<String, ?> params) { return request("fanduel-sportsbook-players", params); }
    public Object sportsbookPromotions(Map<String, ?> params) { return request("fanduel-sportsbook-promotions", params); }
    public Object sportsbookSchedule(Map<String, ?> params) { return request("fanduel-sportsbook-schedule", params); }
    public Object sportsbookSearch(Map<String, ?> params) { return request("fanduel-sportsbook-search", params); }
    public Object sportsbookSearchTabs(Map<String, ?> params) { return request("fanduel-sportsbook-search-tabs", params); }
    public Object sportsbookSport(Map<String, ?> params) { return request("fanduel-sportsbook-sport", params); }
    public Object sportsbookSports(Map<String, ?> params) { return request("fanduel-sportsbook-sports", params); }
    public Object sportsbookStandings(Map<String, ?> params) { return request("fanduel-sportsbook-standings", params); }
    public Object sportsbookStats(Map<String, ?> params) { return request("fanduel-sportsbook-stats", params); }
    public Object sportsbookTeamDepthChart(Map<String, ?> params) { return request("fanduel-sportsbook-team-depth-chart", params); }
    public Object sportsbookTeamNews(Map<String, ?> params) { return request("fanduel-sportsbook-team-news", params); }
    public Object sportsbookTeamOdds(Map<String, ?> params) { return request("fanduel-sportsbook-team-odds", params); }
    public Object sportsbookTeamRoster(Map<String, ?> params) { return request("fanduel-sportsbook-team-roster", params); }
    public Object sportsbookTeamSchedule(Map<String, ?> params) { return request("fanduel-sportsbook-team-schedule", params); }
    public Object sportsbookTeamStats(Map<String, ?> params) { return request("fanduel-sportsbook-team-stats", params); }
    public Object sportsbookTeams(Map<String, ?> params) { return request("fanduel-sportsbook-teams", params); }
    public Object sportsbookTrending(Map<String, ?> params) { return request("fanduel-sportsbook-trending", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
