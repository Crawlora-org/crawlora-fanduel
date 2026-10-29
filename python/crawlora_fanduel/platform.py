"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class FanDuelClient(CrawloraClient):
    """Synchronous FanDuel API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fanduel-python/0.1.0')
        super().__init__(*args, **kwargs)

    def casino_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-casino-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def casino_category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-casino-category', params, response_type=response_type, timeout=timeout, headers=headers)

    def casino_game(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-casino-game', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_carryover_pools(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-carryover-pools', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_horse(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-horse', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_past_race(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-past-race', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_past_races(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-past-races', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_past_tracks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-past-tracks', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_race(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-race', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_races(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-races', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-results', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_track(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-track', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_tracks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-tracks', params, response_type=response_type, timeout=timeout, headers=headers)

    def racing_wager_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-racing-wager-types', params, response_type=response_type, timeout=timeout, headers=headers)

    def research(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-article', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_author(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-author', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_authors(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-authors', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_featured_articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-featured-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_fixtures(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-fixtures', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_nfl_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-nfl-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_player_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-player-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_quick_picks_daily(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-quick-picks-daily', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_projection_slates(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-projection-slates', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_projection_tables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-projection-tables', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_projections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-projections', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    def research_sub_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-research-sub-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_autocomplete(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-autocomplete', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_builder(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-builder', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_builder_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-builder-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_builder_quotes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-builder-quotes', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_competition(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-competition', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-event', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_event_box_score(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-event-box-score', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_event_play_by_play(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-event-play-by-play', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_event_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-event-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_event_score(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-event-score', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_event_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-event-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_events_status(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-events-status', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-home', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_league(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-league', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-live', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_live_count(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-live-count', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_live_data(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-live-data', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_live_scores(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-live-scores', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_market_prices(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-market-prices', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_parlays(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-parlays', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_player_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-player-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_player_props(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-player-props', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_promotions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-promotions', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_search_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-search-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_sport(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-sport', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_team_depth_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-team-depth-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_team_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-team-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_team_odds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-team-odds', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_team_roster(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-team-roster', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_team_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-team-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_team_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-team-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    def sportsbook_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fanduel-sportsbook-trending', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncFanDuelClient(AsyncCrawloraClient):
    """Asynchronous FanDuel API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fanduel-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def casino_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-casino-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def casino_category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-casino-category', params, response_type=response_type, timeout=timeout, headers=headers)

    async def casino_game(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-casino-game', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_carryover_pools(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-carryover-pools', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_horse(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-horse', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_past_race(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-past-race', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_past_races(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-past-races', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_past_tracks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-past-tracks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_race(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-race', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_races(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-races', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-results', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_track(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-track', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_tracks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-tracks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def racing_wager_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-racing-wager-types', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-article', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_author(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-author', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_authors(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-authors', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_featured_articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-featured-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_fixtures(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-fixtures', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_nfl_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-nfl-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_player_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-player-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_quick_picks_daily(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-quick-picks-daily', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_projection_slates(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-projection-slates', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_projection_tables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-projection-tables', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_projections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-projections', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    async def research_sub_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-research-sub-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_autocomplete(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-autocomplete', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_builder(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-builder', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_builder_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-builder-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_builder_quotes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-builder-quotes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_competition(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-competition', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-event', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_event_box_score(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-event-box-score', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_event_play_by_play(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-event-play-by-play', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_event_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-event-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_event_score(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-event-score', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_event_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-event-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_events_status(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-events-status', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-home', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_league(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-league', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-live', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_live_count(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-live-count', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_live_data(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-live-data', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_live_scores(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-live-scores', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_market_prices(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-market-prices', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_parlays(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-parlays', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_player_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-player-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_player_props(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-player-props', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_promotions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-promotions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_search_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-search-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_sport(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-sport', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_team_depth_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-team-depth-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_team_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-team-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_team_odds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-team-odds', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_team_roster(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-team-roster', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_team_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-team-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_team_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-team-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sportsbook_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fanduel-sportsbook-trending', params, response_type=response_type, timeout=timeout, headers=headers)
