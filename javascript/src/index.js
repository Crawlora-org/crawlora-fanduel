import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class FanDuelClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-fanduel-js/0.1.0" });
    this["casinoCategories"] = (...args) => this.request("fanduel-casino-categories", ...args);
    this["casinoCategory"] = (...args) => this.request("fanduel-casino-category", ...args);
    this["casinoGame"] = (...args) => this.request("fanduel-casino-game", ...args);
    this["racingCarryoverPools"] = (...args) => this.request("fanduel-racing-carryover-pools", ...args);
    this["racingFilters"] = (...args) => this.request("fanduel-racing-filters", ...args);
    this["racingHorse"] = (...args) => this.request("fanduel-racing-horse", ...args);
    this["racingPastRace"] = (...args) => this.request("fanduel-racing-past-race", ...args);
    this["racingPastRaces"] = (...args) => this.request("fanduel-racing-past-races", ...args);
    this["racingPastTracks"] = (...args) => this.request("fanduel-racing-past-tracks", ...args);
    this["racingRace"] = (...args) => this.request("fanduel-racing-race", ...args);
    this["racingRaces"] = (...args) => this.request("fanduel-racing-races", ...args);
    this["racingResults"] = (...args) => this.request("fanduel-racing-results", ...args);
    this["racingSearch"] = (...args) => this.request("fanduel-racing-search", ...args);
    this["racingTrack"] = (...args) => this.request("fanduel-racing-track", ...args);
    this["racingTracks"] = (...args) => this.request("fanduel-racing-tracks", ...args);
    this["racingWagerTypes"] = (...args) => this.request("fanduel-racing-wager-types", ...args);
    this["research"] = (...args) => this.request("fanduel-research", ...args);
    this["researchArticle"] = (...args) => this.request("fanduel-research-article", ...args);
    this["researchArticles"] = (...args) => this.request("fanduel-research-articles", ...args);
    this["researchAuthor"] = (...args) => this.request("fanduel-research-author", ...args);
    this["researchAuthors"] = (...args) => this.request("fanduel-research-authors", ...args);
    this["researchFeaturedArticles"] = (...args) => this.request("fanduel-research-featured-articles", ...args);
    this["researchFixtures"] = (...args) => this.request("fanduel-research-fixtures", ...args);
    this["researchNflSchedule"] = (...args) => this.request("fanduel-research-nfl-schedule", ...args);
    this["researchPlayerNews"] = (...args) => this.request("fanduel-research-player-news", ...args);
    this["researchQuickPicksDaily"] = (...args) => this.request("fanduel-research-quick-picks-daily", ...args);
    this["researchProjectionSlates"] = (...args) => this.request("fanduel-research-projection-slates", ...args);
    this["researchProjectionTables"] = (...args) => this.request("fanduel-research-projection-tables", ...args);
    this["researchProjections"] = (...args) => this.request("fanduel-research-projections", ...args);
    this["researchSports"] = (...args) => this.request("fanduel-research-sports", ...args);
    this["researchSubCategories"] = (...args) => this.request("fanduel-research-sub-categories", ...args);
    this["sportsbookAutocomplete"] = (...args) => this.request("fanduel-sportsbook-autocomplete", ...args);
    this["sportsbookBuilder"] = (...args) => this.request("fanduel-sportsbook-builder", ...args);
    this["sportsbookBuilderEvents"] = (...args) => this.request("fanduel-sportsbook-builder-events", ...args);
    this["sportsbookBuilderQuotes"] = (...args) => this.request("fanduel-sportsbook-builder-quotes", ...args);
    this["sportsbookCompetition"] = (...args) => this.request("fanduel-sportsbook-competition", ...args);
    this["sportsbookEvent"] = (...args) => this.request("fanduel-sportsbook-event", ...args);
    this["sportsbookEventBoxScore"] = (...args) => this.request("fanduel-sportsbook-event-box-score", ...args);
    this["sportsbookEventPlayByPlay"] = (...args) => this.request("fanduel-sportsbook-event-play-by-play", ...args);
    this["sportsbookEventPlayers"] = (...args) => this.request("fanduel-sportsbook-event-players", ...args);
    this["sportsbookEventScore"] = (...args) => this.request("fanduel-sportsbook-event-score", ...args);
    this["sportsbookEventStats"] = (...args) => this.request("fanduel-sportsbook-event-stats", ...args);
    this["sportsbookEventsStatus"] = (...args) => this.request("fanduel-sportsbook-events-status", ...args);
    this["sportsbookHome"] = (...args) => this.request("fanduel-sportsbook-home", ...args);
    this["sportsbookLeague"] = (...args) => this.request("fanduel-sportsbook-league", ...args);
    this["sportsbookLive"] = (...args) => this.request("fanduel-sportsbook-live", ...args);
    this["sportsbookLiveCount"] = (...args) => this.request("fanduel-sportsbook-live-count", ...args);
    this["sportsbookLiveData"] = (...args) => this.request("fanduel-sportsbook-live-data", ...args);
    this["sportsbookLiveScores"] = (...args) => this.request("fanduel-sportsbook-live-scores", ...args);
    this["sportsbookMarketPrices"] = (...args) => this.request("fanduel-sportsbook-market-prices", ...args);
    this["sportsbookParlays"] = (...args) => this.request("fanduel-sportsbook-parlays", ...args);
    this["sportsbookPlayer"] = (...args) => this.request("fanduel-sportsbook-player", ...args);
    this["sportsbookPlayerNews"] = (...args) => this.request("fanduel-sportsbook-player-news", ...args);
    this["sportsbookPlayerProps"] = (...args) => this.request("fanduel-sportsbook-player-props", ...args);
    this["sportsbookPlayerStats"] = (...args) => this.request("fanduel-sportsbook-player-stats", ...args);
    this["sportsbookPlayers"] = (...args) => this.request("fanduel-sportsbook-players", ...args);
    this["sportsbookPromotions"] = (...args) => this.request("fanduel-sportsbook-promotions", ...args);
    this["sportsbookSchedule"] = (...args) => this.request("fanduel-sportsbook-schedule", ...args);
    this["sportsbookSearch"] = (...args) => this.request("fanduel-sportsbook-search", ...args);
    this["sportsbookSearchTabs"] = (...args) => this.request("fanduel-sportsbook-search-tabs", ...args);
    this["sportsbookSport"] = (...args) => this.request("fanduel-sportsbook-sport", ...args);
    this["sportsbookSports"] = (...args) => this.request("fanduel-sportsbook-sports", ...args);
    this["sportsbookStandings"] = (...args) => this.request("fanduel-sportsbook-standings", ...args);
    this["sportsbookStats"] = (...args) => this.request("fanduel-sportsbook-stats", ...args);
    this["sportsbookTeamDepthChart"] = (...args) => this.request("fanduel-sportsbook-team-depth-chart", ...args);
    this["sportsbookTeamNews"] = (...args) => this.request("fanduel-sportsbook-team-news", ...args);
    this["sportsbookTeamOdds"] = (...args) => this.request("fanduel-sportsbook-team-odds", ...args);
    this["sportsbookTeamRoster"] = (...args) => this.request("fanduel-sportsbook-team-roster", ...args);
    this["sportsbookTeamSchedule"] = (...args) => this.request("fanduel-sportsbook-team-schedule", ...args);
    this["sportsbookTeamStats"] = (...args) => this.request("fanduel-sportsbook-team-stats", ...args);
    this["sportsbookTeams"] = (...args) => this.request("fanduel-sportsbook-teams", ...args);
    this["sportsbookTrending"] = (...args) => this.request("fanduel-sportsbook-trending", ...args);
  }
}

export { FanDuelClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default FanDuelClient;
