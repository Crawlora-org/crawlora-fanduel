import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class FanDuelClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  casinoCategories(params?: OperationParamsMap["fanduel-casino-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  casinoCategory(params: OperationParamsMap["fanduel-casino-category"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  casinoGame(params: OperationParamsMap["fanduel-casino-game"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingCarryoverPools(params?: OperationParamsMap["fanduel-racing-carryover-pools"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingFilters(params?: OperationParamsMap["fanduel-racing-filters"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingHorse(params: OperationParamsMap["fanduel-racing-horse"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingPastRace(params: OperationParamsMap["fanduel-racing-past-race"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingPastRaces(params: OperationParamsMap["fanduel-racing-past-races"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingPastTracks(params?: OperationParamsMap["fanduel-racing-past-tracks"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingRace(params: OperationParamsMap["fanduel-racing-race"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingRaces(params?: OperationParamsMap["fanduel-racing-races"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingResults(params?: OperationParamsMap["fanduel-racing-results"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingSearch(params: OperationParamsMap["fanduel-racing-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingTrack(params: OperationParamsMap["fanduel-racing-track"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingTracks(params?: OperationParamsMap["fanduel-racing-tracks"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  racingWagerTypes(params?: OperationParamsMap["fanduel-racing-wager-types"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  research(params?: OperationParamsMap["fanduel-research"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchArticle(params: OperationParamsMap["fanduel-research-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchArticles(params?: OperationParamsMap["fanduel-research-articles"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchAuthor(params: OperationParamsMap["fanduel-research-author"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchAuthors(params?: OperationParamsMap["fanduel-research-authors"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchFeaturedArticles(params: OperationParamsMap["fanduel-research-featured-articles"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchFixtures(params?: OperationParamsMap["fanduel-research-fixtures"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchNflSchedule(params: OperationParamsMap["fanduel-research-nfl-schedule"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchPlayerNews(params: OperationParamsMap["fanduel-research-player-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchQuickPicksDaily(params?: OperationParamsMap["fanduel-research-quick-picks-daily"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchProjectionSlates(params: OperationParamsMap["fanduel-research-projection-slates"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchProjectionTables(params?: OperationParamsMap["fanduel-research-projection-tables"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchProjections(params: OperationParamsMap["fanduel-research-projections"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchSports(params?: OperationParamsMap["fanduel-research-sports"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  researchSubCategories(params?: OperationParamsMap["fanduel-research-sub-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookAutocomplete(params: OperationParamsMap["fanduel-sportsbook-autocomplete"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookBuilder(params: OperationParamsMap["fanduel-sportsbook-builder"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookBuilderEvents(params?: OperationParamsMap["fanduel-sportsbook-builder-events"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookBuilderQuotes(params: OperationParamsMap["fanduel-sportsbook-builder-quotes"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookCompetition(params: OperationParamsMap["fanduel-sportsbook-competition"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEvent(params: OperationParamsMap["fanduel-sportsbook-event"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEventBoxScore(params: OperationParamsMap["fanduel-sportsbook-event-box-score"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEventPlayByPlay(params: OperationParamsMap["fanduel-sportsbook-event-play-by-play"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEventPlayers(params: OperationParamsMap["fanduel-sportsbook-event-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEventScore(params: OperationParamsMap["fanduel-sportsbook-event-score"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEventStats(params: OperationParamsMap["fanduel-sportsbook-event-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookEventsStatus(params: OperationParamsMap["fanduel-sportsbook-events-status"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookHome(params?: OperationParamsMap["fanduel-sportsbook-home"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookLeague(params: OperationParamsMap["fanduel-sportsbook-league"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookLive(params?: OperationParamsMap["fanduel-sportsbook-live"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookLiveCount(params?: OperationParamsMap["fanduel-sportsbook-live-count"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookLiveData(params: OperationParamsMap["fanduel-sportsbook-live-data"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookLiveScores(params: OperationParamsMap["fanduel-sportsbook-live-scores"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookMarketPrices(params: OperationParamsMap["fanduel-sportsbook-market-prices"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookParlays(params?: OperationParamsMap["fanduel-sportsbook-parlays"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookPlayer(params: OperationParamsMap["fanduel-sportsbook-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookPlayerNews(params: OperationParamsMap["fanduel-sportsbook-player-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookPlayerProps(params: OperationParamsMap["fanduel-sportsbook-player-props"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookPlayerStats(params: OperationParamsMap["fanduel-sportsbook-player-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookPlayers(params: OperationParamsMap["fanduel-sportsbook-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookPromotions(params?: OperationParamsMap["fanduel-sportsbook-promotions"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookSchedule(params: OperationParamsMap["fanduel-sportsbook-schedule"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookSearch(params: OperationParamsMap["fanduel-sportsbook-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookSearchTabs(params: OperationParamsMap["fanduel-sportsbook-search-tabs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookSport(params: OperationParamsMap["fanduel-sportsbook-sport"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookSports(params?: OperationParamsMap["fanduel-sportsbook-sports"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookStandings(params: OperationParamsMap["fanduel-sportsbook-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookStats(params?: OperationParamsMap["fanduel-sportsbook-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeamDepthChart(params: OperationParamsMap["fanduel-sportsbook-team-depth-chart"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeamNews(params: OperationParamsMap["fanduel-sportsbook-team-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeamOdds(params: OperationParamsMap["fanduel-sportsbook-team-odds"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeamRoster(params: OperationParamsMap["fanduel-sportsbook-team-roster"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeamSchedule(params: OperationParamsMap["fanduel-sportsbook-team-schedule"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeamStats(params: OperationParamsMap["fanduel-sportsbook-team-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTeams(params?: OperationParamsMap["fanduel-sportsbook-teams"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sportsbookTrending(params?: OperationParamsMap["fanduel-sportsbook-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  casinoCategories(params?: OperationParamsMap["fanduel-casino-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  casinoCategory(params: OperationParamsMap["fanduel-casino-category"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  casinoGame(params: OperationParamsMap["fanduel-casino-game"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingCarryoverPools(params?: OperationParamsMap["fanduel-racing-carryover-pools"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingFilters(params?: OperationParamsMap["fanduel-racing-filters"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingHorse(params: OperationParamsMap["fanduel-racing-horse"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingPastRace(params: OperationParamsMap["fanduel-racing-past-race"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingPastRaces(params: OperationParamsMap["fanduel-racing-past-races"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingPastTracks(params?: OperationParamsMap["fanduel-racing-past-tracks"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingRace(params: OperationParamsMap["fanduel-racing-race"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingRaces(params?: OperationParamsMap["fanduel-racing-races"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingResults(params?: OperationParamsMap["fanduel-racing-results"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingSearch(params: OperationParamsMap["fanduel-racing-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingTrack(params: OperationParamsMap["fanduel-racing-track"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingTracks(params?: OperationParamsMap["fanduel-racing-tracks"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  racingWagerTypes(params?: OperationParamsMap["fanduel-racing-wager-types"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  research(params?: OperationParamsMap["fanduel-research"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchArticle(params: OperationParamsMap["fanduel-research-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchArticles(params?: OperationParamsMap["fanduel-research-articles"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchAuthor(params: OperationParamsMap["fanduel-research-author"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchAuthors(params?: OperationParamsMap["fanduel-research-authors"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchFeaturedArticles(params: OperationParamsMap["fanduel-research-featured-articles"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchFixtures(params?: OperationParamsMap["fanduel-research-fixtures"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchNflSchedule(params: OperationParamsMap["fanduel-research-nfl-schedule"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchPlayerNews(params: OperationParamsMap["fanduel-research-player-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchQuickPicksDaily(params?: OperationParamsMap["fanduel-research-quick-picks-daily"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchProjectionSlates(params: OperationParamsMap["fanduel-research-projection-slates"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchProjectionTables(params?: OperationParamsMap["fanduel-research-projection-tables"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchProjections(params: OperationParamsMap["fanduel-research-projections"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchSports(params?: OperationParamsMap["fanduel-research-sports"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  researchSubCategories(params?: OperationParamsMap["fanduel-research-sub-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookAutocomplete(params: OperationParamsMap["fanduel-sportsbook-autocomplete"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookBuilder(params: OperationParamsMap["fanduel-sportsbook-builder"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookBuilderEvents(params?: OperationParamsMap["fanduel-sportsbook-builder-events"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookBuilderQuotes(params: OperationParamsMap["fanduel-sportsbook-builder-quotes"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookCompetition(params: OperationParamsMap["fanduel-sportsbook-competition"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEvent(params: OperationParamsMap["fanduel-sportsbook-event"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEventBoxScore(params: OperationParamsMap["fanduel-sportsbook-event-box-score"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEventPlayByPlay(params: OperationParamsMap["fanduel-sportsbook-event-play-by-play"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEventPlayers(params: OperationParamsMap["fanduel-sportsbook-event-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEventScore(params: OperationParamsMap["fanduel-sportsbook-event-score"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEventStats(params: OperationParamsMap["fanduel-sportsbook-event-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookEventsStatus(params: OperationParamsMap["fanduel-sportsbook-events-status"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookHome(params?: OperationParamsMap["fanduel-sportsbook-home"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookLeague(params: OperationParamsMap["fanduel-sportsbook-league"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookLive(params?: OperationParamsMap["fanduel-sportsbook-live"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookLiveCount(params?: OperationParamsMap["fanduel-sportsbook-live-count"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookLiveData(params: OperationParamsMap["fanduel-sportsbook-live-data"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookLiveScores(params: OperationParamsMap["fanduel-sportsbook-live-scores"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookMarketPrices(params: OperationParamsMap["fanduel-sportsbook-market-prices"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookParlays(params?: OperationParamsMap["fanduel-sportsbook-parlays"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookPlayer(params: OperationParamsMap["fanduel-sportsbook-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookPlayerNews(params: OperationParamsMap["fanduel-sportsbook-player-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookPlayerProps(params: OperationParamsMap["fanduel-sportsbook-player-props"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookPlayerStats(params: OperationParamsMap["fanduel-sportsbook-player-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookPlayers(params: OperationParamsMap["fanduel-sportsbook-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookPromotions(params?: OperationParamsMap["fanduel-sportsbook-promotions"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookSchedule(params: OperationParamsMap["fanduel-sportsbook-schedule"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookSearch(params: OperationParamsMap["fanduel-sportsbook-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookSearchTabs(params: OperationParamsMap["fanduel-sportsbook-search-tabs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookSport(params: OperationParamsMap["fanduel-sportsbook-sport"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookSports(params?: OperationParamsMap["fanduel-sportsbook-sports"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookStandings(params: OperationParamsMap["fanduel-sportsbook-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookStats(params?: OperationParamsMap["fanduel-sportsbook-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeamDepthChart(params: OperationParamsMap["fanduel-sportsbook-team-depth-chart"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeamNews(params: OperationParamsMap["fanduel-sportsbook-team-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeamOdds(params: OperationParamsMap["fanduel-sportsbook-team-odds"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeamRoster(params: OperationParamsMap["fanduel-sportsbook-team-roster"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeamSchedule(params: OperationParamsMap["fanduel-sportsbook-team-schedule"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeamStats(params: OperationParamsMap["fanduel-sportsbook-team-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTeams(params?: OperationParamsMap["fanduel-sportsbook-teams"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sportsbookTrending(params?: OperationParamsMap["fanduel-sportsbook-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  casinoCategories(...args: OperationRequestArgs<"fanduel-casino-categories">): Promise<OperationResponseMap["fanduel-casino-categories"]>;
  casinoCategory(...args: OperationRequestArgs<"fanduel-casino-category">): Promise<OperationResponseMap["fanduel-casino-category"]>;
  casinoGame(...args: OperationRequestArgs<"fanduel-casino-game">): Promise<OperationResponseMap["fanduel-casino-game"]>;
  racingCarryoverPools(...args: OperationRequestArgs<"fanduel-racing-carryover-pools">): Promise<OperationResponseMap["fanduel-racing-carryover-pools"]>;
  racingFilters(...args: OperationRequestArgs<"fanduel-racing-filters">): Promise<OperationResponseMap["fanduel-racing-filters"]>;
  racingHorse(...args: OperationRequestArgs<"fanduel-racing-horse">): Promise<OperationResponseMap["fanduel-racing-horse"]>;
  racingPastRace(...args: OperationRequestArgs<"fanduel-racing-past-race">): Promise<OperationResponseMap["fanduel-racing-past-race"]>;
  racingPastRaces(...args: OperationRequestArgs<"fanduel-racing-past-races">): Promise<OperationResponseMap["fanduel-racing-past-races"]>;
  racingPastTracks(...args: OperationRequestArgs<"fanduel-racing-past-tracks">): Promise<OperationResponseMap["fanduel-racing-past-tracks"]>;
  racingRace(...args: OperationRequestArgs<"fanduel-racing-race">): Promise<OperationResponseMap["fanduel-racing-race"]>;
  racingRaces(...args: OperationRequestArgs<"fanduel-racing-races">): Promise<OperationResponseMap["fanduel-racing-races"]>;
  racingResults(...args: OperationRequestArgs<"fanduel-racing-results">): Promise<OperationResponseMap["fanduel-racing-results"]>;
  racingSearch(...args: OperationRequestArgs<"fanduel-racing-search">): Promise<OperationResponseMap["fanduel-racing-search"]>;
  racingTrack(...args: OperationRequestArgs<"fanduel-racing-track">): Promise<OperationResponseMap["fanduel-racing-track"]>;
  racingTracks(...args: OperationRequestArgs<"fanduel-racing-tracks">): Promise<OperationResponseMap["fanduel-racing-tracks"]>;
  racingWagerTypes(...args: OperationRequestArgs<"fanduel-racing-wager-types">): Promise<OperationResponseMap["fanduel-racing-wager-types"]>;
  research(...args: OperationRequestArgs<"fanduel-research">): Promise<OperationResponseMap["fanduel-research"]>;
  researchArticle(...args: OperationRequestArgs<"fanduel-research-article">): Promise<OperationResponseMap["fanduel-research-article"]>;
  researchArticles(...args: OperationRequestArgs<"fanduel-research-articles">): Promise<OperationResponseMap["fanduel-research-articles"]>;
  researchAuthor(...args: OperationRequestArgs<"fanduel-research-author">): Promise<OperationResponseMap["fanduel-research-author"]>;
  researchAuthors(...args: OperationRequestArgs<"fanduel-research-authors">): Promise<OperationResponseMap["fanduel-research-authors"]>;
  researchFeaturedArticles(...args: OperationRequestArgs<"fanduel-research-featured-articles">): Promise<OperationResponseMap["fanduel-research-featured-articles"]>;
  researchFixtures(...args: OperationRequestArgs<"fanduel-research-fixtures">): Promise<OperationResponseMap["fanduel-research-fixtures"]>;
  researchNflSchedule(...args: OperationRequestArgs<"fanduel-research-nfl-schedule">): Promise<OperationResponseMap["fanduel-research-nfl-schedule"]>;
  researchPlayerNews(...args: OperationRequestArgs<"fanduel-research-player-news">): Promise<OperationResponseMap["fanduel-research-player-news"]>;
  researchQuickPicksDaily(...args: OperationRequestArgs<"fanduel-research-quick-picks-daily">): Promise<OperationResponseMap["fanduel-research-quick-picks-daily"]>;
  researchProjectionSlates(...args: OperationRequestArgs<"fanduel-research-projection-slates">): Promise<OperationResponseMap["fanduel-research-projection-slates"]>;
  researchProjectionTables(...args: OperationRequestArgs<"fanduel-research-projection-tables">): Promise<OperationResponseMap["fanduel-research-projection-tables"]>;
  researchProjections(...args: OperationRequestArgs<"fanduel-research-projections">): Promise<OperationResponseMap["fanduel-research-projections"]>;
  researchSports(...args: OperationRequestArgs<"fanduel-research-sports">): Promise<OperationResponseMap["fanduel-research-sports"]>;
  researchSubCategories(...args: OperationRequestArgs<"fanduel-research-sub-categories">): Promise<OperationResponseMap["fanduel-research-sub-categories"]>;
  sportsbookAutocomplete(...args: OperationRequestArgs<"fanduel-sportsbook-autocomplete">): Promise<OperationResponseMap["fanduel-sportsbook-autocomplete"]>;
  sportsbookBuilder(...args: OperationRequestArgs<"fanduel-sportsbook-builder">): Promise<OperationResponseMap["fanduel-sportsbook-builder"]>;
  sportsbookBuilderEvents(...args: OperationRequestArgs<"fanduel-sportsbook-builder-events">): Promise<OperationResponseMap["fanduel-sportsbook-builder-events"]>;
  sportsbookBuilderQuotes(...args: OperationRequestArgs<"fanduel-sportsbook-builder-quotes">): Promise<OperationResponseMap["fanduel-sportsbook-builder-quotes"]>;
  sportsbookCompetition(...args: OperationRequestArgs<"fanduel-sportsbook-competition">): Promise<OperationResponseMap["fanduel-sportsbook-competition"]>;
  sportsbookEvent(...args: OperationRequestArgs<"fanduel-sportsbook-event">): Promise<OperationResponseMap["fanduel-sportsbook-event"]>;
  sportsbookEventBoxScore(...args: OperationRequestArgs<"fanduel-sportsbook-event-box-score">): Promise<OperationResponseMap["fanduel-sportsbook-event-box-score"]>;
  sportsbookEventPlayByPlay(...args: OperationRequestArgs<"fanduel-sportsbook-event-play-by-play">): Promise<OperationResponseMap["fanduel-sportsbook-event-play-by-play"]>;
  sportsbookEventPlayers(...args: OperationRequestArgs<"fanduel-sportsbook-event-players">): Promise<OperationResponseMap["fanduel-sportsbook-event-players"]>;
  sportsbookEventScore(...args: OperationRequestArgs<"fanduel-sportsbook-event-score">): Promise<OperationResponseMap["fanduel-sportsbook-event-score"]>;
  sportsbookEventStats(...args: OperationRequestArgs<"fanduel-sportsbook-event-stats">): Promise<OperationResponseMap["fanduel-sportsbook-event-stats"]>;
  sportsbookEventsStatus(...args: OperationRequestArgs<"fanduel-sportsbook-events-status">): Promise<OperationResponseMap["fanduel-sportsbook-events-status"]>;
  sportsbookHome(...args: OperationRequestArgs<"fanduel-sportsbook-home">): Promise<OperationResponseMap["fanduel-sportsbook-home"]>;
  sportsbookLeague(...args: OperationRequestArgs<"fanduel-sportsbook-league">): Promise<OperationResponseMap["fanduel-sportsbook-league"]>;
  sportsbookLive(...args: OperationRequestArgs<"fanduel-sportsbook-live">): Promise<OperationResponseMap["fanduel-sportsbook-live"]>;
  sportsbookLiveCount(...args: OperationRequestArgs<"fanduel-sportsbook-live-count">): Promise<OperationResponseMap["fanduel-sportsbook-live-count"]>;
  sportsbookLiveData(...args: OperationRequestArgs<"fanduel-sportsbook-live-data">): Promise<OperationResponseMap["fanduel-sportsbook-live-data"]>;
  sportsbookLiveScores(...args: OperationRequestArgs<"fanduel-sportsbook-live-scores">): Promise<OperationResponseMap["fanduel-sportsbook-live-scores"]>;
  sportsbookMarketPrices(...args: OperationRequestArgs<"fanduel-sportsbook-market-prices">): Promise<OperationResponseMap["fanduel-sportsbook-market-prices"]>;
  sportsbookParlays(...args: OperationRequestArgs<"fanduel-sportsbook-parlays">): Promise<OperationResponseMap["fanduel-sportsbook-parlays"]>;
  sportsbookPlayer(...args: OperationRequestArgs<"fanduel-sportsbook-player">): Promise<OperationResponseMap["fanduel-sportsbook-player"]>;
  sportsbookPlayerNews(...args: OperationRequestArgs<"fanduel-sportsbook-player-news">): Promise<OperationResponseMap["fanduel-sportsbook-player-news"]>;
  sportsbookPlayerProps(...args: OperationRequestArgs<"fanduel-sportsbook-player-props">): Promise<OperationResponseMap["fanduel-sportsbook-player-props"]>;
  sportsbookPlayerStats(...args: OperationRequestArgs<"fanduel-sportsbook-player-stats">): Promise<OperationResponseMap["fanduel-sportsbook-player-stats"]>;
  sportsbookPlayers(...args: OperationRequestArgs<"fanduel-sportsbook-players">): Promise<OperationResponseMap["fanduel-sportsbook-players"]>;
  sportsbookPromotions(...args: OperationRequestArgs<"fanduel-sportsbook-promotions">): Promise<OperationResponseMap["fanduel-sportsbook-promotions"]>;
  sportsbookSchedule(...args: OperationRequestArgs<"fanduel-sportsbook-schedule">): Promise<OperationResponseMap["fanduel-sportsbook-schedule"]>;
  sportsbookSearch(...args: OperationRequestArgs<"fanduel-sportsbook-search">): Promise<OperationResponseMap["fanduel-sportsbook-search"]>;
  sportsbookSearchTabs(...args: OperationRequestArgs<"fanduel-sportsbook-search-tabs">): Promise<OperationResponseMap["fanduel-sportsbook-search-tabs"]>;
  sportsbookSport(...args: OperationRequestArgs<"fanduel-sportsbook-sport">): Promise<OperationResponseMap["fanduel-sportsbook-sport"]>;
  sportsbookSports(...args: OperationRequestArgs<"fanduel-sportsbook-sports">): Promise<OperationResponseMap["fanduel-sportsbook-sports"]>;
  sportsbookStandings(...args: OperationRequestArgs<"fanduel-sportsbook-standings">): Promise<OperationResponseMap["fanduel-sportsbook-standings"]>;
  sportsbookStats(...args: OperationRequestArgs<"fanduel-sportsbook-stats">): Promise<OperationResponseMap["fanduel-sportsbook-stats"]>;
  sportsbookTeamDepthChart(...args: OperationRequestArgs<"fanduel-sportsbook-team-depth-chart">): Promise<OperationResponseMap["fanduel-sportsbook-team-depth-chart"]>;
  sportsbookTeamNews(...args: OperationRequestArgs<"fanduel-sportsbook-team-news">): Promise<OperationResponseMap["fanduel-sportsbook-team-news"]>;
  sportsbookTeamOdds(...args: OperationRequestArgs<"fanduel-sportsbook-team-odds">): Promise<OperationResponseMap["fanduel-sportsbook-team-odds"]>;
  sportsbookTeamRoster(...args: OperationRequestArgs<"fanduel-sportsbook-team-roster">): Promise<OperationResponseMap["fanduel-sportsbook-team-roster"]>;
  sportsbookTeamSchedule(...args: OperationRequestArgs<"fanduel-sportsbook-team-schedule">): Promise<OperationResponseMap["fanduel-sportsbook-team-schedule"]>;
  sportsbookTeamStats(...args: OperationRequestArgs<"fanduel-sportsbook-team-stats">): Promise<OperationResponseMap["fanduel-sportsbook-team-stats"]>;
  sportsbookTeams(...args: OperationRequestArgs<"fanduel-sportsbook-teams">): Promise<OperationResponseMap["fanduel-sportsbook-teams"]>;
  sportsbookTrending(...args: OperationRequestArgs<"fanduel-sportsbook-trending">): Promise<OperationResponseMap["fanduel-sportsbook-trending"]>;
}
export { FanDuelClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default FanDuelClient;
