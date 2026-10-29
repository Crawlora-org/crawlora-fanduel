# Crawlora FanDuel API client for PHP (`crawlora/fanduel`)

This PHP package calls Crawlora's hosted FanDuel API at `https://api.crawlora.net/api/v1`. It exposes 72 endpoints covering public racing, casino catalogue, and research data. It does not call or scrape FanDuel directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/fanduel
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fanduel-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fanduel-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Fanduel\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("fanduel-racing-search", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 72 API operations.

## Supported FanDuel API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fanduel/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/fanduel/casino/categories` | `fanduel-casino-categories` | FanDuel Casino categories |
| `GET` | `/fanduel/casino/category` | `fanduel-casino-category` | FanDuel Casino category games |
| `GET` | `/fanduel/casino/game` | `fanduel-casino-game` | FanDuel Casino game detail |
| `GET` | `/fanduel/racing/carryover-pools` | `fanduel-racing-carryover-pools` | FanDuel Racing carry-over pools |
| `GET` | `/fanduel/racing/filters` | `fanduel-racing-filters` | FanDuel Racing filter values |
| `GET` | `/fanduel/racing/horse` | `fanduel-racing-horse` | FanDuel Racing horse career |
| `GET` | `/fanduel/racing/past-race` | `fanduel-racing-past-race` | FanDuel Racing past race result |
| `GET` | `/fanduel/racing/past-races` | `fanduel-racing-past-races` | FanDuel Racing past races of a day |
| `GET` | `/fanduel/racing/past-tracks` | `fanduel-racing-past-tracks` | FanDuel Racing tracks with past results |
| `GET` | `/fanduel/racing/race` | `fanduel-racing-race` | FanDuel Racing race detail |
| `GET` | `/fanduel/racing/races` | `fanduel-racing-races` | FanDuel Racing races |
| `GET` | `/fanduel/racing/results` | `fanduel-racing-results` | FanDuel Racing results |
| `GET` | `/fanduel/racing/search` | `fanduel-racing-search` | FanDuel Racing search by name |
| `GET` | `/fanduel/racing/track` | `fanduel-racing-track` | FanDuel Racing track and its races |
| `GET` | `/fanduel/racing/tracks` | `fanduel-racing-tracks` | FanDuel Racing tracks today |
| `GET` | `/fanduel/racing/wager-types` | `fanduel-racing-wager-types` | FanDuel Racing wager types |
| `GET` | `/fanduel/research` | `fanduel-research` | FanDuel Research recent RSS items |
| `GET` | `/fanduel/research/article` | `fanduel-research-article` | FanDuel Research article |
| `GET` | `/fanduel/research/articles` | `fanduel-research-articles` | FanDuel Research articles |
| `GET` | `/fanduel/research/author` | `fanduel-research-author` | FanDuel Research author |
| `GET` | `/fanduel/research/authors` | `fanduel-research-authors` | FanDuel Research authors |
| `GET` | `/fanduel/research/featured-articles` | `fanduel-research-featured-articles` | FanDuel Research featured articles |
| `GET` | `/fanduel/research/fixtures` | `fanduel-research-fixtures` | FanDuel Research live fixtures |
| `GET` | `/fanduel/research/nfl-schedule` | `fanduel-research-nfl-schedule` | FanDuel Research NFL schedule |
| `GET` | `/fanduel/research/player-news` | `fanduel-research-player-news` | FanDuel Research player news and injuries |
| `GET` | `/fanduel/research/podcasts/quick-picks-daily` | `fanduel-research-quick-picks-daily` | FanDuel Research Quick Picks Daily episode archive |
| `GET` | `/fanduel/research/projection-slates` | `fanduel-research-projection-slates` | FanDuel Research projection slates |
| `GET` | `/fanduel/research/projection-tables` | `fanduel-research-projection-tables` | FanDuel Research projection tables |
| `GET` | `/fanduel/research/projections` | `fanduel-research-projections` | FanDuel Research fantasy projections |
| `GET` | `/fanduel/research/sports` | `fanduel-research-sports` | FanDuel Research sports and topics |
| `GET` | `/fanduel/research/sub-categories` | `fanduel-research-sub-categories` | FanDuel Research topics |
| `GET` | `/fanduel/sportsbook/autocomplete` | `fanduel-sportsbook-autocomplete` | FanDuel Sportsbook search suggestions |
| `GET` | `/fanduel/sportsbook/builder` | `fanduel-sportsbook-builder` | FanDuel Sportsbook bet builder |
| `GET` | `/fanduel/sportsbook/builder/events` | `fanduel-sportsbook-builder-events` | FanDuel Sportsbook bet builder events |
| `GET` | `/fanduel/sportsbook/builder/quotes` | `fanduel-sportsbook-builder-quotes` | FanDuel Sportsbook bet builder quotes |
| `GET` | `/fanduel/sportsbook/competition` | `fanduel-sportsbook-competition` | FanDuel Sportsbook competition schedule and futures |
| `GET` | `/fanduel/sportsbook/event` | `fanduel-sportsbook-event` | FanDuel Sportsbook event markets |
| `GET` | `/fanduel/sportsbook/event/box-score` | `fanduel-sportsbook-event-box-score` | FanDuel Sportsbook live box score |
| `GET` | `/fanduel/sportsbook/event/play-by-play` | `fanduel-sportsbook-event-play-by-play` | FanDuel Sportsbook live play-by-play |
| `GET` | `/fanduel/sportsbook/event/players` | `fanduel-sportsbook-event-players` | FanDuel Sportsbook event teams and player roster |
| `GET` | `/fanduel/sportsbook/event/score` | `fanduel-sportsbook-event-score` | FanDuel Sportsbook live score and status |
| `GET` | `/fanduel/sportsbook/event/stats` | `fanduel-sportsbook-event-stats` | FanDuel Sportsbook event betting splits and form |
| `GET` | `/fanduel/sportsbook/events/status` | `fanduel-sportsbook-events-status` | FanDuel Sportsbook events status |
| `GET` | `/fanduel/sportsbook/home` | `fanduel-sportsbook-home` | FanDuel Sportsbook homepage odds |
| `GET` | `/fanduel/sportsbook/league` | `fanduel-sportsbook-league` | FanDuel Sportsbook league page odds |
| `GET` | `/fanduel/sportsbook/live` | `fanduel-sportsbook-live` | FanDuel Sportsbook live betting events |
| `GET` | `/fanduel/sportsbook/live-count` | `fanduel-sportsbook-live-count` | FanDuel Sportsbook live event count |
| `GET` | `/fanduel/sportsbook/live-data` | `fanduel-sportsbook-live-data` | FanDuel Sportsbook live state for any sport |
| `GET` | `/fanduel/sportsbook/live-scores` | `fanduel-sportsbook-live-scores` | FanDuel Sportsbook live scores and stats for many events |
| `GET` | `/fanduel/sportsbook/market-prices` | `fanduel-sportsbook-market-prices` | FanDuel Sportsbook current market prices |
| `GET` | `/fanduel/sportsbook/parlays` | `fanduel-sportsbook-parlays` | FanDuel Sportsbook Parlay Hub |
| `GET` | `/fanduel/sportsbook/player` | `fanduel-sportsbook-player` | FanDuel Sportsbook player overview |
| `GET` | `/fanduel/sportsbook/player/news` | `fanduel-sportsbook-player-news` | FanDuel Sportsbook player news |
| `GET` | `/fanduel/sportsbook/player/props` | `fanduel-sportsbook-player-props` | FanDuel Sportsbook player props |
| `GET` | `/fanduel/sportsbook/player/stats` | `fanduel-sportsbook-player-stats` | FanDuel Sportsbook player statistics |
| `GET` | `/fanduel/sportsbook/players` | `fanduel-sportsbook-players` | FanDuel Sportsbook player directory |
| `GET` | `/fanduel/sportsbook/promotions` | `fanduel-sportsbook-promotions` | FanDuel Sportsbook promotions |
| `GET` | `/fanduel/sportsbook/schedule` | `fanduel-sportsbook-schedule` | FanDuel Sportsbook league schedule |
| `GET` | `/fanduel/sportsbook/search` | `fanduel-sportsbook-search` | FanDuel Sportsbook search |
| `GET` | `/fanduel/sportsbook/search/tabs` | `fanduel-sportsbook-search-tabs` | FanDuel Sportsbook grouped search |
| `GET` | `/fanduel/sportsbook/sport` | `fanduel-sportsbook-sport` | FanDuel Sportsbook sport page odds |
| `GET` | `/fanduel/sportsbook/sports` | `fanduel-sportsbook-sports` | FanDuel Sportsbook sports and league pages |
| `GET` | `/fanduel/sportsbook/standings` | `fanduel-sportsbook-standings` | FanDuel Sportsbook league standings |
| `GET` | `/fanduel/sportsbook/stats` | `fanduel-sportsbook-stats` | FanDuel Sportsbook betting splits and form for upcoming events |
| `GET` | `/fanduel/sportsbook/team/depth-chart` | `fanduel-sportsbook-team-depth-chart` | FanDuel Sportsbook team depth chart |
| `GET` | `/fanduel/sportsbook/team/news` | `fanduel-sportsbook-team-news` | FanDuel Sportsbook team news |
| `GET` | `/fanduel/sportsbook/team/odds` | `fanduel-sportsbook-team-odds` | FanDuel Sportsbook team odds page |
| `GET` | `/fanduel/sportsbook/team/roster` | `fanduel-sportsbook-team-roster` | FanDuel Sportsbook team roster and injuries |
| `GET` | `/fanduel/sportsbook/team/schedule` | `fanduel-sportsbook-team-schedule` | FanDuel Sportsbook team schedule and results |
| `GET` | `/fanduel/sportsbook/team/stats` | `fanduel-sportsbook-team-stats` | FanDuel Sportsbook team statistics |
| `GET` | `/fanduel/sportsbook/teams` | `fanduel-sportsbook-teams` | FanDuel Sportsbook team index |
| `GET` | `/fanduel/sportsbook/trending` | `fanduel-sportsbook-trending` | FanDuel Sportsbook trending searches |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fanduel-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fanduel-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-fanduel). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-fanduel/blob/main/docs/usage.md).
