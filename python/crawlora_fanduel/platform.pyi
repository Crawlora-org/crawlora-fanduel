from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelFanduelSportsbookTrendingResponseDoc = TypedDict('ModelFanduelSportsbookTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookTrendingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTrendingResponse = TypedDict('ModelFanduelSportsbookTrendingResponse', {
    'enriched': NotRequired[bool],
    'fetched_at': NotRequired[str],
    'results': NotRequired[list[ModelFanduelSportsbookTrendingItem]],
    'terms': NotRequired[list[str]],
}, total=False)

ModelFanduelSportsbookTrendingItem = TypedDict('ModelFanduelSportsbookTrendingItem', {
    'competition': NotRequired[str],
    'display_name': NotRequired[str],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'expires_at': NotRequired[str],
    'metadata': NotRequired[dict[str, Any]],
    'term': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamsResponseDoc = TypedDict('ModelFanduelSportsbookTeamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookTeamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamsResponse = TypedDict('ModelFanduelSportsbookTeamsResponse', {
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelFanduelSportsbookTeamGroup]],
    'league': NotRequired[str],
    'sections': NotRequired[list[str]],
    'team_count': NotRequired[int],
}, total=False)

ModelFanduelSportsbookTeamGroup = TypedDict('ModelFanduelSportsbookTeamGroup', {
    'teams': NotRequired[list[ModelFanduelSportsbookTeamSummary]],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamSummary = TypedDict('ModelFanduelSportsbookTeamSummary', {
    'bet_records': NotRequired[ModelFanduelSportsbookBetRecords],
    'code': NotRequired[str],
    'conference': NotRequired[str],
    'division': NotRequired[str],
    'head_coach': NotRequired[str],
    'logo_url': NotRequired[str],
    'market': NotRequired[str],
    'name': NotRequired[str],
    'next_game': NotRequired[ModelFanduelSportsbookTeamGameRef],
    'primary_color': NotRequired[str],
    'secondary_color': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'sub_division': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamGameRef = TypedDict('ModelFanduelSportsbookTeamGameRef', {
    'event_url': NotRequired[str],
    'home_game': NotRequired[bool],
    'opponent': NotRequired[str],
    'scheduled_time': NotRequired[str],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBetRecords = TypedDict('ModelFanduelSportsbookBetRecords', {
    'against_spread': NotRequired[ModelFanduelSportsbookWinLoss],
    'money_line': NotRequired[ModelFanduelSportsbookWinLoss],
    'over_under': NotRequired[ModelFanduelSportsbookWinLoss],
}, total=False)

ModelFanduelSportsbookWinLoss = TypedDict('ModelFanduelSportsbookWinLoss', {
    'losses': NotRequired[int],
    'ties': NotRequired[int],
    'wins': NotRequired[int],
}, total=False)

ModelFanduelSportsbookTeamStatsResponseDoc = TypedDict('ModelFanduelSportsbookTeamStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookTeamStatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamStatsResponse = TypedDict('ModelFanduelSportsbookTeamStatsResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'stats': NotRequired[dict[str, Any]],
    'team': NotRequired[str],
}, total=False)

ModelFanduelSportsbookScheduleResponseDoc = TypedDict('ModelFanduelSportsbookScheduleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookScheduleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookScheduleResponse = TypedDict('ModelFanduelSportsbookScheduleResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'next_game': NotRequired[ModelFanduelSportsbookGameSummary],
    'previous_game': NotRequired[ModelFanduelSportsbookGameSummary],
    'seasons': NotRequired[list[ModelFanduelSportsbookScheduleSeason]],
    'team': NotRequired[str],
}, total=False)

ModelFanduelSportsbookScheduleSeason = TypedDict('ModelFanduelSportsbookScheduleSeason', {
    'games': NotRequired[list[ModelFanduelSportsbookScheduleGame]],
    'season_type': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookScheduleGame = TypedDict('ModelFanduelSportsbookScheduleGame', {
    'bye_week': NotRequired[bool],
    'cancelled': NotRequired[bool],
    'date': NotRequired[str],
    'location': NotRequired[str],
    'opponent': NotRequired[ModelFanduelSportsbookTeamRef],
    'opponent_record': NotRequired[str],
    'opponent_score': NotRequired[int],
    'postponed': NotRequired[bool],
    'team_score': NotRequired[int],
    'venue': NotRequired[str],
    'week': NotRequired[int],
}, total=False)

ModelFanduelSportsbookTeamRef = TypedDict('ModelFanduelSportsbookTeamRef', {
    'code': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelSportsbookGameSummary = TypedDict('ModelFanduelSportsbookGameSummary', {
    'away_score': NotRequired[int],
    'away_slug': NotRequired[str],
    'away_team': NotRequired[str],
    'date': NotRequired[str],
    'home_score': NotRequired[int],
    'home_slug': NotRequired[str],
    'home_team': NotRequired[str],
    'title': NotRequired[str],
    'venue': NotRequired[str],
}, total=False)

ModelFanduelSportsbookRosterResponseDoc = TypedDict('ModelFanduelSportsbookRosterResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookRosterResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookRosterResponse = TypedDict('ModelFanduelSportsbookRosterResponse', {
    'fetched_at': NotRequired[str],
    'injury_statuses': NotRequired[list[ModelFanduelSportsbookValueCount]],
    'league': NotRequired[str],
    'players': NotRequired[list[ModelFanduelSportsbookRosterPlayer]],
    'positions': NotRequired[list[ModelFanduelSportsbookValueCount]],
    'statuses': NotRequired[list[ModelFanduelSportsbookValueCount]],
    'team': NotRequired[str],
}, total=False)

ModelFanduelSportsbookValueCount = TypedDict('ModelFanduelSportsbookValueCount', {
    'count': NotRequired[int],
    'value': NotRequired[str],
}, total=False)

ModelFanduelSportsbookRosterPlayer = TypedDict('ModelFanduelSportsbookRosterPlayer', {
    'college': NotRequired[str],
    'experience': NotRequired[str],
    'height': NotRequired[str],
    'injury_status': NotRequired[str],
    'name': NotRequired[str],
    'number': NotRequired[str],
    'photo_url': NotRequired[str],
    'position': NotRequired[str],
    'slug': NotRequired[str],
    'status': NotRequired[str],
    'weight': NotRequired[int],
}, total=False)

ModelFanduelSportsbookTeamOddsResponseDoc = TypedDict('ModelFanduelSportsbookTeamOddsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookTeamOddsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamOddsResponse = TypedDict('ModelFanduelSportsbookTeamOddsResponse', {
    'championship': NotRequired[str],
    'championship_tab': NotRequired[str],
    'fetched_at': NotRequired[str],
    'future_odds': NotRequired[list[ModelFanduelSportsbookFutureOdd]],
    'league': NotRequired[str],
    'next_games': NotRequired[list[ModelFanduelSportsbookUpcomingGame]],
    'player_props': NotRequired[list[ModelFanduelSportsbookPlayerProps]],
    'team': NotRequired[ModelFanduelSportsbookTeamRef],
}, total=False)

ModelFanduelSportsbookPlayerProps = TypedDict('ModelFanduelSportsbookPlayerProps', {
    'events': NotRequired[list[ModelFanduelSportsbookPlayerPropEvent]],
    'player': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerPropEvent = TypedDict('ModelFanduelSportsbookPlayerPropEvent', {
    'date': NotRequired[str],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'markets': NotRequired[list[ModelFanduelSportsbookPlayerPropMarket]],
}, total=False)

ModelFanduelSportsbookPlayerPropMarket = TypedDict('ModelFanduelSportsbookPlayerPropMarket', {
    'market_id': NotRequired[str],
    'market_type': NotRequired[str],
    'name': NotRequired[str],
    'selections': NotRequired[list[ModelFanduelSportsbookPlayerPropSelection]],
}, total=False)

ModelFanduelSportsbookPlayerPropSelection = TypedDict('ModelFanduelSportsbookPlayerPropSelection', {
    'handicap': NotRequired[float],
    'odds': NotRequired[str],
    'runner': NotRequired[str],
    'selection_id': NotRequired[int],
}, total=False)

ModelFanduelSportsbookUpcomingGame = TypedDict('ModelFanduelSportsbookUpcomingGame', {
    'away_odds': NotRequired[ModelFanduelSportsbookTeamGameOdds],
    'event_url': NotRequired[str],
    'home_game': NotRequired[bool],
    'home_odds': NotRequired[ModelFanduelSportsbookTeamGameOdds],
    'opponent': NotRequired[str],
    'opponent_team': NotRequired[ModelFanduelSportsbookTeamRef],
    'scheduled_time': NotRequired[str],
    'status': NotRequired[str],
    'venue': NotRequired[str],
    'venue_type': NotRequired[str],
    'week': NotRequired[int],
}, total=False)

ModelFanduelSportsbookTeamGameOdds = TypedDict('ModelFanduelSportsbookTeamGameOdds', {
    'money_line': NotRequired[ModelFanduelSportsbookGameLine],
    'spread': NotRequired[ModelFanduelSportsbookGameLine],
    'total': NotRequired[ModelFanduelSportsbookGameLine],
}, total=False)

ModelFanduelSportsbookGameLine = TypedDict('ModelFanduelSportsbookGameLine', {
    'odds': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelFanduelSportsbookFutureOdd = TypedDict('ModelFanduelSportsbookFutureOdd', {
    'description': NotRequired[str],
    'market_type': NotRequired[str],
    'odds': NotRequired[str],
    'team': NotRequired[str],
    'team_slug': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamNewsResponseDoc = TypedDict('ModelFanduelSportsbookTeamNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookTeamNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamNewsResponse = TypedDict('ModelFanduelSportsbookTeamNewsResponse', {
    'articles': NotRequired[list[ModelFanduelSportsbookTeamArticle]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'league': NotRequired[str],
    'next_cursor': NotRequired[str],
    'player_updates': NotRequired[list[dict[str, Any]]],
    'team': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeamArticle = TypedDict('ModelFanduelSportsbookTeamArticle', {
    'author': NotRequired[str],
    'id': NotRequired[str],
    'published_at': NotRequired[str],
    'source': NotRequired[str],
    'summary': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelSportsbookDepthChartResponseDoc = TypedDict('ModelFanduelSportsbookDepthChartResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookDepthChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookDepthChartResponse = TypedDict('ModelFanduelSportsbookDepthChartResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'players': NotRequired[list[ModelFanduelSportsbookDepthChartPlayer]],
    'team': NotRequired[str],
    'team_leaders': NotRequired[dict[str, Any]],
}, total=False)

ModelFanduelSportsbookDepthChartPlayer = TypedDict('ModelFanduelSportsbookDepthChartPlayer', {
    'age': NotRequired[int],
    'college': NotRequired[str],
    'draft_pick': NotRequired[str],
    'draft_round': NotRequired[str],
    'draft_year': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'rank': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelSportsbookStatsListResponseDoc = TypedDict('ModelFanduelSportsbookStatsListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookStatsListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookStatsListResponse = TypedDict('ModelFanduelSportsbookStatsListResponse', {
    'events': NotRequired[list[ModelFanduelSportsbookEventStats]],
    'fetched_at': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventStats = TypedDict('ModelFanduelSportsbookEventStats', {
    'competition': NotRequired[str],
    'competition_id': NotRequired[int],
    'event_id': NotRequired[int],
    'last_five_games': NotRequired[list[ModelFanduelSportsbookFormLine]],
    'other_widgets': NotRequired[dict[str, Any]],
    'spread_bets_percent': NotRequired[list[ModelFanduelSportsbookSplit]],
    'spread_money_percent': NotRequired[list[ModelFanduelSportsbookSplit]],
    'teams': NotRequired[list[ModelFanduelSportsbookStatsTeam]],
}, total=False)

ModelFanduelSportsbookStatsTeam = TypedDict('ModelFanduelSportsbookStatsTeam', {
    'name': NotRequired[str],
    'primary_color': NotRequired[str],
    'secondary_color': NotRequired[str],
    'selection_id': NotRequired[int],
    'side': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSplit = TypedDict('ModelFanduelSportsbookSplit', {
    'name': NotRequired[str],
    'percent': NotRequired[int],
    'selection_id': NotRequired[int],
}, total=False)

ModelFanduelSportsbookFormLine = TypedDict('ModelFanduelSportsbookFormLine', {
    'name': NotRequired[str],
    'results': NotRequired[list[str]],
    'selection_id': NotRequired[int],
}, total=False)

ModelFanduelSportsbookStandingsResponseDoc = TypedDict('ModelFanduelSportsbookStandingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookStandingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookStandingsResponse = TypedDict('ModelFanduelSportsbookStandingsResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'team_count': NotRequired[int],
    'teams': NotRequired[list[ModelFanduelSportsbookStandingsTeam]],
}, total=False)

ModelFanduelSportsbookStandingsTeam = TypedDict('ModelFanduelSportsbookStandingsTeam', {
    'code': NotRequired[str],
    'conference': NotRequired[str],
    'division': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'standing': NotRequired[dict[str, Any]],
}, total=False)

ModelFanduelSportsbookSportsResponseDoc = TypedDict('ModelFanduelSportsbookSportsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookSportsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSportsResponse = TypedDict('ModelFanduelSportsbookSportsResponse', {
    'fetched_at': NotRequired[str],
    'popular_links': NotRequired[list[ModelFanduelSportsbookNavLink]],
    'quick_links': NotRequired[list[ModelFanduelSportsbookNavLink]],
    'sports': NotRequired[list[ModelFanduelSportsbookSport]],
    'state': NotRequired[str],
    'states': NotRequired[list[ModelFanduelSportsbookState]],
    'teaser_competitions': NotRequired[list[ModelFanduelSportsbookTeaserCompetition]],
}, total=False)

ModelFanduelSportsbookTeaserCompetition = TypedDict('ModelFanduelSportsbookTeaserCompetition', {
    'competition_id': NotRequired[int],
    'icon': NotRequired[str],
    'name': NotRequired[str],
    'starting_spread': NotRequired[float],
}, total=False)

ModelFanduelSportsbookState = TypedDict('ModelFanduelSportsbookState', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSport = TypedDict('ModelFanduelSportsbookSport', {
    'event_type_id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelFanduelSportsbookNavLink = TypedDict('ModelFanduelSportsbookNavLink', {
    'custom_page_id': NotRequired[str],
    'display_order': NotRequired[int],
    'icon': NotRequired[str],
    'id': NotRequired[int],
    'kind': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPageResponseDoc = TypedDict('ModelFanduelSportsbookPageResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPageResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPageResponse = TypedDict('ModelFanduelSportsbookPageResponse', {
    'competition_id': NotRequired[int],
    'competitions': NotRequired[list[ModelFanduelSportsbookCompetition]],
    'custom_page_id': NotRequired[str],
    'default_tab': NotRequired[str],
    'description': NotRequired[str],
    'event_type_id': NotRequired[int],
    'events': NotRequired[list[ModelFanduelSportsbookEvent]],
    'fetched_at': NotRequired[str],
    'market_types': NotRequired[list[ModelFanduelSportsbookMarketTypeCount]],
    'page_type': NotRequired[str],
    'selected_tab': NotRequired[str],
    'state': NotRequired[str],
    'tabs': NotRequired[list[ModelFanduelSportsbookTab]],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTab = TypedDict('ModelFanduelSportsbookTab', {
    'event_count': NotRequired[int],
    'id': NotRequired[str],
    'live_count': NotRequired[int],
    'market_count': NotRequired[int],
    'slug': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookMarketTypeCount = TypedDict('ModelFanduelSportsbookMarketTypeCount', {
    'count': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEvent = TypedDict('ModelFanduelSportsbookEvent', {
    'competition_id': NotRequired[int],
    'event_id': NotRequired[int],
    'event_type_id': NotRequired[int],
    'in_play': NotRequired[bool],
    'markets': NotRequired[list[ModelFanduelSportsbookMarket]],
    'name': NotRequired[str],
    'open_date': NotRequired[str],
    'video_available': NotRequired[bool],
}, total=False)

ModelFanduelSportsbookMarket = TypedDict('ModelFanduelSportsbookMarket', {
    'betting_type': NotRequired[str],
    'in_play': NotRequired[bool],
    'market_id': NotRequired[str],
    'market_time': NotRequired[str],
    'name': NotRequired[str],
    'runners': NotRequired[list[ModelFanduelSportsbookRunner]],
    'same_game_parlay_eligible': NotRequired[bool],
    'status': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookRunner = TypedDict('ModelFanduelSportsbookRunner', {
    'abbreviation': NotRequired[str],
    'american_odds': NotRequired[int],
    'decimal_odds': NotRequired[float],
    'fractional_odds': NotRequired[str],
    'handicap': NotRequired[float],
    'is_player': NotRequired[bool],
    'jersey_number': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'previous_american_odds': NotRequired[int],
    'previous_decimal_odds': NotRequired[float],
    'selection_id': NotRequired[int],
    'side': NotRequired[str],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookCompetition = TypedDict('ModelFanduelSportsbookCompetition', {
    'competition_id': NotRequired[int],
    'event_type_id': NotRequired[int],
    'name': NotRequired[str],
    'region': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchTabsResponseDoc = TypedDict('ModelFanduelSportsbookSearchTabsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookSearchTabsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchTabsResponse = TypedDict('ModelFanduelSportsbookSearchTabsResponse', {
    'fetched_at': NotRequired[str],
    'found': NotRequired[int],
    'next_start_index': NotRequired[int],
    'page_size': NotRequired[int],
    'pill': NotRequired[str],
    'pills': NotRequired[list[ModelFanduelSportsbookSearchPill]],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelFanduelSportsbookSearchHit]],
    'start_index': NotRequired[int],
    'state': NotRequired[str],
    'tab': NotRequired[str],
    'tabs': NotRequired[list[ModelFanduelSportsbookSearchTab]],
    'total_results': NotRequired[int],
}, total=False)

ModelFanduelSportsbookSearchTab = TypedDict('ModelFanduelSportsbookSearchTab', {
    'id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchHit = TypedDict('ModelFanduelSportsbookSearchHit', {
    'ancestry': NotRequired[list[ModelFanduelSportsbookSearchAncestor]],
    'competition': NotRequired[str],
    'competition_id': NotRequired[str],
    'event_category': NotRequired[int],
    'exchange_id': NotRequired[int],
    'result_id': NotRequired[str],
    'sport': NotRequired[str],
    'sport_id': NotRequired[str],
    'start_date': NotRequired[str],
    'subtype': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchAncestor = TypedDict('ModelFanduelSportsbookSearchAncestor', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchPill = TypedDict('ModelFanduelSportsbookSearchPill', {
    'id': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchResponseDoc = TypedDict('ModelFanduelSportsbookSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchResponse = TypedDict('ModelFanduelSportsbookSearchResponse', {
    'competitions': NotRequired[list[ModelFanduelSportsbookSearchCompetition]],
    'events': NotRequired[list[ModelFanduelSportsbookSearchEvent]],
    'fetched_at': NotRequired[str],
    'query': NotRequired[str],
    'state': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchEvent = TypedDict('ModelFanduelSportsbookSearchEvent', {
    'competition_id': NotRequired[int],
    'competition_name': NotRequired[str],
    'event_id': NotRequired[int],
    'event_type_id': NotRequired[int],
    'event_type_name': NotRequired[str],
    'in_play': NotRequired[bool],
    'name': NotRequired[str],
    'open_date': NotRequired[str],
}, total=False)

ModelFanduelSportsbookSearchCompetition = TypedDict('ModelFanduelSportsbookSearchCompetition', {
    'competition_id': NotRequired[int],
    'event_type_id': NotRequired[int],
    'event_type_name': NotRequired[str],
    'match_count': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLeagueScheduleResponseDoc = TypedDict('ModelFanduelSportsbookLeagueScheduleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookLeagueScheduleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLeagueScheduleResponse = TypedDict('ModelFanduelSportsbookLeagueScheduleResponse', {
    'date': NotRequired[str],
    'end_date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game_count': NotRequired[int],
    'groups': NotRequired[list[ModelFanduelSportsbookScheduleGroup]],
    'league': NotRequired[str],
    'week': NotRequired[ModelFanduelSportsbookScheduleWeek],
    'weeks': NotRequired[list[ModelFanduelSportsbookScheduleWeek]],
}, total=False)

ModelFanduelSportsbookScheduleWeek = TypedDict('ModelFanduelSportsbookScheduleWeek', {
    'current_week': NotRequired[bool],
    'end_date': NotRequired[str],
    'id': NotRequired[int],
    'label': NotRequired[str],
    'season_type': NotRequired[str],
    'start_date': NotRequired[str],
}, total=False)

ModelFanduelSportsbookScheduleGroup = TypedDict('ModelFanduelSportsbookScheduleGroup', {
    'games': NotRequired[list[ModelFanduelSportsbookLeagueGame]],
    'season_type': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLeagueGame = TypedDict('ModelFanduelSportsbookLeagueGame', {
    'away_code': NotRequired[str],
    'away_score': NotRequired[int],
    'away_slug': NotRequired[str],
    'away_team': NotRequired[str],
    'broadcast': NotRequired[str],
    'bye_week': NotRequired[bool],
    'conference_game': NotRequired[bool],
    'home_code': NotRequired[str],
    'home_score': NotRequired[int],
    'home_slug': NotRequired[str],
    'home_team': NotRequired[str],
    'scheduled_time': NotRequired[str],
    'status': NotRequired[str],
    'title': NotRequired[str],
    'venue': NotRequired[str],
    'week': NotRequired[int],
}, total=False)

ModelFanduelSportsbookPromotionsResponseDoc = TypedDict('ModelFanduelSportsbookPromotionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPromotionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPromotionsResponse = TypedDict('ModelFanduelSportsbookPromotionsResponse', {
    'context': NotRequired[str],
    'custom_page_id': NotRequired[str],
    'event_type_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'placements': NotRequired[list[ModelFanduelSportsbookPlacement]],
    'promotions': NotRequired[list[ModelFanduelSportsbookPromotion]],
    'state': NotRequired[str],
    'tags': NotRequired[list[ModelFanduelSportsbookTagCount]],
}, total=False)

ModelFanduelSportsbookTagCount = TypedDict('ModelFanduelSportsbookTagCount', {
    'count': NotRequired[int],
    'tag': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPromotion = TypedDict('ModelFanduelSportsbookPromotion', {
    'button_text': NotRequired[str],
    'button_url': NotRequired[str],
    'ends_at': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'products': NotRequired[list[str]],
    'promo_code': NotRequired[str],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlacement = TypedDict('ModelFanduelSportsbookPlacement', {
    'placement': NotRequired[str],
    'promo_codes': NotRequired[list[str]],
}, total=False)

ModelFanduelSportsbookPlayersResponseDoc = TypedDict('ModelFanduelSportsbookPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayersResponse = TypedDict('ModelFanduelSportsbookPlayersResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'players': NotRequired[list[ModelFanduelSportsbookDirectoryPlayer]],
    'total': NotRequired[int],
}, total=False)

ModelFanduelSportsbookDirectoryPlayer = TypedDict('ModelFanduelSportsbookDirectoryPlayer', {
    'name': NotRequired[str],
    'player_id': NotRequired[int],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerStatsResponseDoc = TypedDict('ModelFanduelSportsbookPlayerStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPlayerStatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerStatsResponse = TypedDict('ModelFanduelSportsbookPlayerStatsResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'name': NotRequired[str],
    'player': NotRequired[str],
    'position': NotRequired[str],
    'stats': NotRequired[dict[str, Any]],
}, total=False)

ModelFanduelSportsbookPlayerPropsResponseDoc = TypedDict('ModelFanduelSportsbookPlayerPropsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPlayerPropsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerPropsResponse = TypedDict('ModelFanduelSportsbookPlayerPropsResponse', {
    'content_text': NotRequired[str],
    'events': NotRequired[list[ModelFanduelSportsbookPlayerPropEvent]],
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'name': NotRequired[str],
    'player': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerNewsResponseDoc = TypedDict('ModelFanduelSportsbookPlayerNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPlayerNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerNewsResponse = TypedDict('ModelFanduelSportsbookPlayerNewsResponse', {
    'articles': NotRequired[list[ModelFanduelSportsbookTeamArticle]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'league': NotRequired[str],
    'name': NotRequired[str],
    'next_cursor': NotRequired[str],
    'player': NotRequired[str],
    'player_updates': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelFanduelSportsbookPlayerResponseDoc = TypedDict('ModelFanduelSportsbookPlayerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPlayerResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayerResponse = TypedDict('ModelFanduelSportsbookPlayerResponse', {
    'fetched_at': NotRequired[str],
    'game_log': NotRequired[Any],
    'league': NotRequired[str],
    'name': NotRequired[str],
    'news': NotRequired[list[ModelFanduelSportsbookTeamArticle]],
    'player': NotRequired[str],
    'player_updates': NotRequired[list[dict[str, Any]]],
    'position': NotRequired[str],
    'projections': NotRequired[Any],
    'season': NotRequired[dict[str, Any]],
    'season_totals': NotRequired[Any],
    'stats': NotRequired[dict[str, Any]],
    'team': NotRequired[str],
    'team_slug': NotRequired[str],
}, total=False)

ModelFanduelSportsbookParlaysResponseDoc = TypedDict('ModelFanduelSportsbookParlaysResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookParlaysResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookParlaysResponse = TypedDict('ModelFanduelSportsbookParlaysResponse', {
    'card_cap': NotRequired[int],
    'event_groups': NotRequired[list[ModelFanduelSportsbookParlayEventGroup]],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'filters': NotRequired[list[ModelFanduelSportsbookParlayFilter]],
    'parlays': NotRequired[list[ModelFanduelSportsbookParlay]],
    'state': NotRequired[str],
    'truncated': NotRequired[bool],
    'types': NotRequired[list[ModelFanduelSportsbookParlayTypeCount]],
    'view': NotRequired[str],
}, total=False)

ModelFanduelSportsbookParlayTypeCount = TypedDict('ModelFanduelSportsbookParlayTypeCount', {
    'count': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookParlay = TypedDict('ModelFanduelSportsbookParlay', {
    'american_odds': NotRequired[int],
    'away_team': NotRequired[str],
    'competition_id': NotRequired[int],
    'competition_name': NotRequired[str],
    'decimal_odds': NotRequired[float],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'featured_by': NotRequired[str],
    'home_team': NotRequired[str],
    'id': NotRequired[str],
    'is_editable': NotRequired[bool],
    'is_manually_created': NotRequired[bool],
    'legs': NotRequired[list[ModelFanduelSportsbookParlayLeg]],
    'narrative': NotRequired[str],
    'total_bets': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookParlayLeg = TypedDict('ModelFanduelSportsbookParlayLeg', {
    'competition_id': NotRequired[int],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'market': NotRequired[str],
    'market_id': NotRequired[str],
    'market_type': NotRequired[str],
    'selection': NotRequired[str],
    'selection_id': NotRequired[int],
}, total=False)

ModelFanduelSportsbookParlayFilter = TypedDict('ModelFanduelSportsbookParlayFilter', {
    'competition_ids': NotRequired[list[int]],
    'id': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelFanduelSportsbookParlayEventGroup = TypedDict('ModelFanduelSportsbookParlayEventGroup', {
    'away_team': NotRequired[str],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'home_team': NotRequired[str],
    'open_date': NotRequired[str],
    'parlay_ids': NotRequired[list[str]],
}, total=False)

ModelFanduelSportsbookMarketPricesResponseDoc = TypedDict('ModelFanduelSportsbookMarketPricesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookMarketPricesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookMarketPricesResponse = TypedDict('ModelFanduelSportsbookMarketPricesResponse', {
    'fetched_at': NotRequired[str],
    'markets': NotRequired[list[ModelFanduelSportsbookMarketPrice]],
    'missing': NotRequired[list[str]],
    'state': NotRequired[str],
}, total=False)

ModelFanduelSportsbookMarketPrice = TypedDict('ModelFanduelSportsbookMarketPrice', {
    'bet_delay_seconds': NotRequired[int],
    'betting_type': NotRequired[str],
    'in_play': NotRequired[bool],
    'market_id': NotRequired[str],
    'runners': NotRequired[list[ModelFanduelSportsbookPriceRunner]],
    'same_game_parlay_eligible': NotRequired[bool],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPriceRunner = TypedDict('ModelFanduelSportsbookPriceRunner', {
    'american_odds': NotRequired[int],
    'decimal_odds': NotRequired[float],
    'fractional_odds': NotRequired[str],
    'handicap': NotRequired[float],
    'previous_american_odds': NotRequired[int],
    'previous_decimal_odds': NotRequired[float],
    'selection_id': NotRequired[int],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveScoresResponseDoc = TypedDict('ModelFanduelSportsbookLiveScoresResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookLiveScoresResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveScoresResponse = TypedDict('ModelFanduelSportsbookLiveScoresResponse', {
    'events': NotRequired[list[ModelFanduelSportsbookLiveScore]],
    'fetched_at': NotRequired[str],
    'not_found': NotRequired[list[int]],
    'state': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveScore = TypedDict('ModelFanduelSportsbookLiveScore', {
    'away_score': NotRequired[int],
    'current_period': NotRequired[int],
    'details': NotRequired[dict[str, Any]],
    'event_id': NotRequired[int],
    'home_score': NotRequired[int],
    'media_types': NotRequired[list[str]],
    'model_type': NotRequired[str],
    'period': NotRequired[str],
    'period_remaining_milliseconds': NotRequired[int],
    'provider': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveDataResponseDoc = TypedDict('ModelFanduelSportsbookLiveDataResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookLiveDataResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveDataResponse = TypedDict('ModelFanduelSportsbookLiveDataResponse', {
    'events': NotRequired[list[ModelFanduelSportsbookLiveEvent]],
    'fetched_at': NotRequired[str],
    'missing': NotRequired[list[int]],
}, total=False)

ModelFanduelSportsbookLiveEvent = TypedDict('ModelFanduelSportsbookLiveEvent', {
    'away_score': NotRequired[int],
    'details': NotRequired[dict[str, Any]],
    'event_id': NotRequired[int],
    'home_score': NotRequired[int],
    'live': NotRequired[bool],
    'media_types': NotRequired[list[str]],
    'player_progress': NotRequired[dict[str, Any]],
    'player_stats': NotRequired[dict[str, Any]],
    'provider': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveCountResponseDoc = TypedDict('ModelFanduelSportsbookLiveCountResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookLiveCountResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveCountResponse = TypedDict('ModelFanduelSportsbookLiveCountResponse', {
    'fetched_at': NotRequired[str],
    'live_events': NotRequired[int],
    'state': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventsStatusResponseDoc = TypedDict('ModelFanduelSportsbookEventsStatusResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookEventsStatusResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventsStatusResponse = TypedDict('ModelFanduelSportsbookEventsStatusResponse', {
    'events': NotRequired[list[ModelFanduelSportsbookEventStatus]],
    'fetched_at': NotRequired[str],
    'not_found': NotRequired[list[int]],
    'state': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventStatus = TypedDict('ModelFanduelSportsbookEventStatus', {
    'event_id': NotRequired[int],
    'game_phase': NotRequired[str],
    'price_clock': NotRequired[str],
    'status': NotRequired[str],
    'status_clock': NotRequired[str],
    'structure_clock': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventStatsResponseDoc = TypedDict('ModelFanduelSportsbookEventStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookEventStatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventStatsResponse = TypedDict('ModelFanduelSportsbookEventStatsResponse', {
    'fetched_at': NotRequired[str],
    'stats': NotRequired[ModelFanduelSportsbookEventStats],
}, total=False)

ModelFanduelSportsbookEventScoreResponseDoc = TypedDict('ModelFanduelSportsbookEventScoreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookEventScoreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventScoreResponse = TypedDict('ModelFanduelSportsbookEventScoreResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'live': NotRequired[ModelFanduelSportsbookLiveStatus],
    'media_types': NotRequired[list[str]],
    'score': NotRequired[ModelFanduelSportsbookScore],
}, total=False)

ModelFanduelSportsbookScore = TypedDict('ModelFanduelSportsbookScore', {
    'away': NotRequired[int],
    'clock': NotRequired[str],
    'home': NotRequired[int],
    'period_scores': NotRequired[list[ModelFanduelSportsbookPeriodScore]],
}, total=False)

ModelFanduelSportsbookPeriodScore = TypedDict('ModelFanduelSportsbookPeriodScore', {
    'away': NotRequired[int],
    'home': NotRequired[int],
    'period': NotRequired[str],
}, total=False)

ModelFanduelSportsbookLiveStatus = TypedDict('ModelFanduelSportsbookLiveStatus', {
    'box_score_available': NotRequired[bool],
    'competition': NotRequired[str],
    'play_by_play_available': NotRequired[bool],
    'provider': NotRequired[str],
    'quick_bets_available': NotRequired[bool],
    'score_available': NotRequired[bool],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventPlayersResponseDoc = TypedDict('ModelFanduelSportsbookEventPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookEventPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventPlayersResponse = TypedDict('ModelFanduelSportsbookEventPlayersResponse', {
    'away_team': NotRequired[ModelFanduelSportsbookTeam],
    'competition': NotRequired[str],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'fetched_at': NotRequired[str],
    'home_team': NotRequired[ModelFanduelSportsbookTeam],
    'players': NotRequired[list[ModelFanduelSportsbookPlayer]],
    'scheduled_at': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayer = TypedDict('ModelFanduelSportsbookPlayer', {
    'abbreviated_name': NotRequired[str],
    'name': NotRequired[str],
    'number': NotRequired[str],
    'player_id': NotRequired[str],
    'position': NotRequired[str],
    'team': NotRequired[str],
}, total=False)

ModelFanduelSportsbookTeam = TypedDict('ModelFanduelSportsbookTeam', {
    'abbreviation': NotRequired[str],
    'color': NotRequired[str],
    'conference': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayByPlayResponseDoc = TypedDict('ModelFanduelSportsbookPlayByPlayResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookPlayByPlayResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookPlayByPlayResponse = TypedDict('ModelFanduelSportsbookPlayByPlayResponse', {
    'available': NotRequired[bool],
    'current': NotRequired[bool],
    'event_id': NotRequired[int],
    'feed': NotRequired[dict[str, Any]],
    'fetched_at': NotRequired[str],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBoxScoreResponseDoc = TypedDict('ModelFanduelSportsbookBoxScoreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookBoxScoreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBoxScoreResponse = TypedDict('ModelFanduelSportsbookBoxScoreResponse', {
    'available': NotRequired[bool],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelFanduelSportsbookBoxScoreGroup]],
    'score': NotRequired[ModelFanduelSportsbookScore],
    'status': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBoxScoreGroup = TypedDict('ModelFanduelSportsbookBoxScoreGroup', {
    'columns': NotRequired[list[ModelFanduelSportsbookBoxScoreColumn]],
    'key': NotRequired[str],
    'label': NotRequired[str],
    'rows': NotRequired[list[ModelFanduelSportsbookBoxScoreRow]],
}, total=False)

ModelFanduelSportsbookBoxScoreRow = TypedDict('ModelFanduelSportsbookBoxScoreRow', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'position': NotRequired[str],
    'stats': NotRequired[dict[str, str]],
    'team': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBoxScoreColumn = TypedDict('ModelFanduelSportsbookBoxScoreColumn', {
    'key': NotRequired[str],
    'label': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventResponseDoc = TypedDict('ModelFanduelSportsbookEventResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookEventResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookEventResponse = TypedDict('ModelFanduelSportsbookEventResponse', {
    'competition': NotRequired[ModelFanduelSportsbookCompetition],
    'default_tab': NotRequired[str],
    'event': NotRequired[ModelFanduelSportsbookEvent],
    'fetched_at': NotRequired[str],
    'market_types': NotRequired[list[ModelFanduelSportsbookMarketTypeCount]],
    'notes': NotRequired[list[str]],
    'selected_tab': NotRequired[str],
    'state': NotRequired[str],
    'tabs': NotRequired[list[ModelFanduelSportsbookTab]],
}, total=False)

ModelFanduelSportsbookChoiceQuotesResponseDoc = TypedDict('ModelFanduelSportsbookChoiceQuotesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookChoiceQuotesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookChoiceQuotesResponse = TypedDict('ModelFanduelSportsbookChoiceQuotesResponse', {
    'failures': NotRequired[list[ModelFanduelSportsbookChoiceFailure]],
    'fetched_at': NotRequired[str],
    'quotes': NotRequired[list[ModelFanduelSportsbookChoiceQuote]],
    'ramp_event_id': NotRequired[int],
    'state': NotRequired[str],
}, total=False)

ModelFanduelSportsbookChoiceQuote = TypedDict('ModelFanduelSportsbookChoiceQuote', {
    'american_odds': NotRequired[int],
    'bet_type': NotRequired[str],
    'choice_id': NotRequired[str],
    'decimal_odds': NotRequired[float],
    'display_decimal_odds': NotRequired[float],
    'features': NotRequired[list[str]],
    'fractional_odds': NotRequired[str],
    'same_game_multi': NotRequired[bool],
}, total=False)

ModelFanduelSportsbookChoiceFailure = TypedDict('ModelFanduelSportsbookChoiceFailure', {
    'choice_id': NotRequired[str],
    'code': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderEventsResponseDoc = TypedDict('ModelFanduelSportsbookBuilderEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookBuilderEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderEventsResponse = TypedDict('ModelFanduelSportsbookBuilderEventsResponse', {
    'competitions': NotRequired[list[ModelFanduelSportsbookBuilderCompetition]],
    'events': NotRequired[list[ModelFanduelSportsbookBuilderEvent]],
    'experience': NotRequired[str],
    'fetched_at': NotRequired[str],
    'first_event_id': NotRequired[int],
    'state': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderEvent = TypedDict('ModelFanduelSportsbookBuilderEvent', {
    'abbreviation': NotRequired[str],
    'away_logo_url': NotRequired[str],
    'competition': NotRequired[str],
    'competition_id': NotRequired[int],
    'event_id': NotRequired[int],
    'home_logo_url': NotRequired[str],
    'name': NotRequired[str],
    'start_time': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderCompetition = TypedDict('ModelFanduelSportsbookBuilderCompetition', {
    'competition_id': NotRequired[int],
    'event_ids': NotRequired[list[int]],
    'first_event_id': NotRequired[int],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderResponseDoc = TypedDict('ModelFanduelSportsbookBuilderResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookBuilderResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderResponse = TypedDict('ModelFanduelSportsbookBuilderResponse', {
    'cards': NotRequired[list[ModelFanduelSportsbookBuilderCard]],
    'choices': NotRequired[list[ModelFanduelSportsbookBuilderChoice]],
    'competition': NotRequired[str],
    'competition_id': NotRequired[int],
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'experience': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game_status': NotRequired[str],
    'groups': NotRequired[list[ModelFanduelSportsbookBuilderGroup]],
    'layout': NotRequired[list[str]],
    'periods': NotRequired[list[str]],
    'players': NotRequired[list[ModelFanduelSportsbookBuilderPlayer]],
    'ramp_event_id': NotRequired[int],
    'start_time': NotRequired[str],
    'state': NotRequired[str],
    'status': NotRequired[str],
    'teams': NotRequired[list[ModelFanduelSportsbookBuilderTeam]],
}, total=False)

ModelFanduelSportsbookBuilderTeam = TypedDict('ModelFanduelSportsbookBuilderTeam', {
    'abbr': NotRequired[str],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'side': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderPlayer = TypedDict('ModelFanduelSportsbookBuilderPlayer', {
    'headshot_url': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderGroup = TypedDict('ModelFanduelSportsbookBuilderGroup', {
    'card_ids': NotRequired[list[str]],
    'id': NotRequired[str],
    'layout_type': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderChoice = TypedDict('ModelFanduelSportsbookBuilderChoice', {
    'choice_id': NotRequired[str],
    'description': NotRequired[str],
    'status': NotRequired[str],
    'template_id': NotRequired[str],
}, total=False)

ModelFanduelSportsbookBuilderCard = TypedDict('ModelFanduelSportsbookBuilderCard', {
    'available_options': NotRequired[dict[str, Any]],
    'description_template': NotRequired[str],
    'id': NotRequired[str],
    'legs': NotRequired[list[dict[str, Any]]],
    'prop_key': NotRequired[str],
    'props': NotRequired[list[str]],
    'selected_options': NotRequired[dict[str, Any]],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelSportsbookAutocompleteResponseDoc = TypedDict('ModelFanduelSportsbookAutocompleteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelSportsbookAutocompleteResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelSportsbookAutocompleteResponse = TypedDict('ModelFanduelSportsbookAutocompleteResponse', {
    'fetched_at': NotRequired[str],
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelFanduelSportsbookSuggestion]],
}, total=False)

ModelFanduelSportsbookSuggestion = TypedDict('ModelFanduelSportsbookSuggestion', {
    'highlighted': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelFanduelResearchSubCategoriesResponseDoc = TypedDict('ModelFanduelResearchSubCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchSubCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchSubCategoriesResponse = TypedDict('ModelFanduelResearchSubCategoriesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'sub_categories': NotRequired[list[ModelFanduelResearchSubCategory]],
}, total=False)

ModelFanduelResearchSubCategory = TypedDict('ModelFanduelResearchSubCategory', {
    'slug': NotRequired[str],
    'sport': NotRequired[ModelFanduelResearchSportRef],
    'title': NotRequired[str],
}, total=False)

ModelFanduelResearchSportRef = TypedDict('ModelFanduelResearchSportRef', {
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelResearchSportsResponseDoc = TypedDict('ModelFanduelResearchSportsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchSportsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchSportsResponse = TypedDict('ModelFanduelResearchSportsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'sports': NotRequired[list[ModelFanduelResearchSport]],
}, total=False)

ModelFanduelResearchSport = TypedDict('ModelFanduelResearchSport', {
    'content_sport': NotRequired[str],
    'has_live_scoring': NotRequired[bool],
    'has_player_updates': NotRequired[bool],
    'name': NotRequired[str],
    'player_news_types': NotRequired[list[str]],
    'positions': NotRequired[list[str]],
    'show_authors': NotRequired[bool],
    'slug': NotRequired[str],
    'team_count': NotRequired[int],
    'teams': NotRequired[list[ModelFanduelResearchTeam]],
}, total=False)

ModelFanduelResearchTeam = TypedDict('ModelFanduelResearchTeam', {
    'abbreviation': NotRequired[str],
    'identifier': NotRequired[str],
    'name': NotRequired[str],
    'number_fire_id': NotRequired[int],
}, total=False)

ModelFanduelResearchProjectionsResponseDoc = TypedDict('ModelFanduelResearchProjectionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchProjectionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionsResponse = TypedDict('ModelFanduelResearchProjectionsResponse', {
    'event_id': NotRequired[str],
    'event_name': NotRequired[str],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'position': NotRequired[str],
    'position_label': NotRequired[str],
    'rows': NotRequired[list[ModelFanduelResearchProjectionRow]],
    'scope': NotRequired[str],
    'slate_id': NotRequired[str],
    'slate_name': NotRequired[str],
    'sport': NotRequired[str],
    'table': NotRequired[str],
    'table_name': NotRequired[str],
    'total': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionRow = TypedDict('ModelFanduelResearchProjectionRow', {
    'game': NotRequired[ModelFanduelResearchProjectionGame],
    'player': NotRequired[ModelFanduelResearchProjectionPlayer],
    'salary': NotRequired[int],
    'stats': NotRequired[dict[str, Any]],
    'team': NotRequired[ModelFanduelResearchProjectionTeam],
    'value': NotRequired[float],
}, total=False)

ModelFanduelResearchProjectionTeam = TypedDict('ModelFanduelResearchProjectionTeam', {
    'abbreviation': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionPlayer = TypedDict('ModelFanduelResearchProjectionPlayer', {
    'handedness': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'page_url': NotRequired[str],
    'position': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionGame = TypedDict('ModelFanduelResearchProjectionGame', {
    'away_team': NotRequired[ModelFanduelResearchProjectionTeam],
    'game_time': NotRequired[str],
    'home_team': NotRequired[ModelFanduelResearchProjectionTeam],
}, total=False)

ModelFanduelResearchProjectionTablesResponseDoc = TypedDict('ModelFanduelResearchProjectionTablesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchProjectionTablesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionTablesResponse = TypedDict('ModelFanduelResearchProjectionTablesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'sports': NotRequired[list[str]],
    'tables': NotRequired[list[ModelFanduelResearchProjectionTable]],
    'types': NotRequired[list[str]],
}, total=False)

ModelFanduelResearchProjectionTable = TypedDict('ModelFanduelResearchProjectionTable', {
    'name': NotRequired[str],
    'needs_event': NotRequired[bool],
    'needs_slate': NotRequired[bool],
    'positions': NotRequired[list[ModelFanduelResearchProjectionPosition]],
    'scopes': NotRequired[list[str]],
    'sport': NotRequired[str],
    'table': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionPosition = TypedDict('ModelFanduelResearchProjectionPosition', {
    'default': NotRequired[bool],
    'label': NotRequired[str],
    'matches': NotRequired[list[str]],
    'player_kind': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionSlatesResponseDoc = TypedDict('ModelFanduelResearchProjectionSlatesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchProjectionSlatesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionSlatesResponse = TypedDict('ModelFanduelResearchProjectionSlatesResponse', {
    'count': NotRequired[int],
    'date': NotRequired[str],
    'events': NotRequired[list[ModelFanduelResearchProjectionEvent]],
    'fetched_at': NotRequired[str],
    'season': NotRequired[int],
    'slates': NotRequired[list[ModelFanduelResearchProjectionSlate]],
    'sport': NotRequired[str],
    'week': NotRequired[int],
}, total=False)

ModelFanduelResearchProjectionSlate = TypedDict('ModelFanduelResearchProjectionSlate', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelResearchProjectionEvent = TypedDict('ModelFanduelResearchProjectionEvent', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelQuickPicksDailyResponseDoc = TypedDict('ModelFanduelQuickPicksDailyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelQuickPicksDailyResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelQuickPicksDailyResponse = TypedDict('ModelFanduelQuickPicksDailyResponse', {
    'episodes': NotRequired[list[ModelFanduelQuickPicksDailyEpisode]],
    'fetched_at': NotRequired[str],
    'next_cursor': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'podcast': NotRequired[str],
    'publisher': NotRequired[str],
    'show_url': NotRequired[str],
    'source_url': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelFanduelQuickPicksDailyEpisode = TypedDict('ModelFanduelQuickPicksDailyEpisode', {
    'duration_seconds': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'in_rss_playlist': NotRequired[bool],
    'published_at': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelResearchPlayerNewsResponseDoc = TypedDict('ModelFanduelResearchPlayerNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchPlayerNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchPlayerNewsResponse = TypedDict('ModelFanduelResearchPlayerNewsResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[ModelFanduelResearchPlayerNewsItem]],
    'next_cursor': NotRequired[str],
}, total=False)

ModelFanduelResearchPlayerNewsItem = TypedDict('ModelFanduelResearchPlayerNewsItem', {
    'analysis': NotRequired[str],
    'attribution': NotRequired[str],
    'author': NotRequired[ModelFanduelResearchAuthorRef],
    'fact': NotRequired[str],
    'id': NotRequired[str],
    'news_type': NotRequired[ModelFanduelResearchNewsType],
    'published_at': NotRequired[str],
    'quant': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[ModelFanduelResearchSportRef],
    'subject': NotRequired[ModelFanduelResearchSubject],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelFanduelResearchSubject = TypedDict('ModelFanduelResearchSubject', {
    'abbreviation': NotRequired[str],
    'name': NotRequired[str],
    'number': NotRequired[int],
    'number_fire_id': NotRequired[int],
    'page_url': NotRequired[str],
    'position': NotRequired[str],
    'slug': NotRequired[str],
    'team': NotRequired[ModelFanduelResearchPlayerTeam],
    'type': NotRequired[str],
}, total=False)

ModelFanduelResearchPlayerTeam = TypedDict('ModelFanduelResearchPlayerTeam', {
    'abbreviation': NotRequired[str],
    'name': NotRequired[str],
    'number_fire_id': NotRequired[int],
}, total=False)

ModelFanduelResearchNewsType = TypedDict('ModelFanduelResearchNewsType', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelResearchAuthorRef = TypedDict('ModelFanduelResearchAuthorRef', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelResearchNflScheduleResponseDoc = TypedDict('ModelFanduelResearchNflScheduleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchNflScheduleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchNflScheduleResponse = TypedDict('ModelFanduelResearchNflScheduleResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelFanduelResearchNflGame]],
    'season_type': NotRequired[str],
    'week': NotRequired[int],
}, total=False)

ModelFanduelResearchNflGame = TypedDict('ModelFanduelResearchNflGame', {
    'away_team': NotRequired[ModelFanduelResearchNflTeam],
    'clock': NotRequired[str],
    'closing_lines': NotRequired[ModelFanduelResearchClosingLines],
    'head_to_head_slug': NotRequired[str],
    'home_team': NotRequired[ModelFanduelResearchNflTeam],
    'id': NotRequired[str],
    'network': NotRequired[str],
    'number_fire_id': NotRequired[int],
    'odds': NotRequired[ModelFanduelResearchNflOdds],
    'quarter': NotRequired[str],
    'scheduled_time': NotRequired[str],
    'season_type': NotRequired[str],
    'status': NotRequired[str],
    'venue': NotRequired[str],
    'venue_type': NotRequired[str],
    'weather': NotRequired[ModelFanduelResearchWeather],
    'week': NotRequired[int],
}, total=False)

ModelFanduelResearchWeather = TypedDict('ModelFanduelResearchWeather', {
    'condition': NotRequired[str],
    'humidity_pct': NotRequired[int],
    'temp_f': NotRequired[int],
    'wind_direction': NotRequired[str],
    'wind_mph': NotRequired[int],
}, total=False)

ModelFanduelResearchNflOdds = TypedDict('ModelFanduelResearchNflOdds', {
    'away': NotRequired[ModelFanduelResearchNflSideOdds],
    'event_id': NotRequired[int],
    'home': NotRequired[ModelFanduelResearchNflSideOdds],
    'scheduled_time': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelResearchNflSideOdds = TypedDict('ModelFanduelResearchNflSideOdds', {
    'money_line': NotRequired[ModelFanduelResearchBetLine],
    'spread': NotRequired[ModelFanduelResearchBetLine],
    'team_code': NotRequired[str],
    'total': NotRequired[ModelFanduelResearchBetLine],
}, total=False)

ModelFanduelResearchBetLine = TypedDict('ModelFanduelResearchBetLine', {
    'market_id': NotRequired[str],
    'odds': NotRequired[str],
    'selection_id': NotRequired[str],
    'url': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelFanduelResearchNflTeam = TypedDict('ModelFanduelResearchNflTeam', {
    'average_passing_yards_per_game': NotRequired[float],
    'average_rushing_yards_per_game': NotRequired[float],
    'code': NotRequired[str],
    'conference': NotRequired[str],
    'division': NotRequired[str],
    'game_stats': NotRequired[ModelFanduelResearchNflGameStats],
    'leaders': NotRequired[ModelFanduelResearchNflLeaders],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'number_fire_id': NotRequired[int],
    'primary_color': NotRequired[str],
    'ranks': NotRequired[ModelFanduelResearchNflRanks],
    'record': NotRequired[ModelFanduelResearchNflRecord],
    'secondary_color': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'sportsbook_link': NotRequired[str],
    'win_probability': NotRequired[float],
}, total=False)

ModelFanduelResearchNflRecord = TypedDict('ModelFanduelResearchNflRecord', {
    'losses': NotRequired[int],
    'ties': NotRequired[int],
    'wins': NotRequired[int],
}, total=False)

ModelFanduelResearchNflRanks = TypedDict('ModelFanduelResearchNflRanks', {
    'defense': NotRequired[int],
    'offense': NotRequired[int],
    'passing_yards_per_game': NotRequired[int],
    'rushing_yards_per_game': NotRequired[int],
}, total=False)

ModelFanduelResearchNflLeaders = TypedDict('ModelFanduelResearchNflLeaders', {
    'passing': NotRequired[ModelFanduelResearchNflLeader],
    'receiving': NotRequired[ModelFanduelResearchNflLeader],
    'rushing': NotRequired[ModelFanduelResearchNflLeader],
}, total=False)

ModelFanduelResearchNflLeader = TypedDict('ModelFanduelResearchNflLeader', {
    'attempts': NotRequired[int],
    'carries': NotRequired[int],
    'completions': NotRequired[int],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'receptions': NotRequired[int],
    'targets': NotRequired[int],
    'touchdowns': NotRequired[int],
    'yards': NotRequired[int],
}, total=False)

ModelFanduelResearchNflGameStats = TypedDict('ModelFanduelResearchNflGameStats', {
    'fumbles_forced': NotRequired[int],
    'interceptions_thrown': NotRequired[int],
    'passing_yards': NotRequired[int],
    'points': NotRequired[int],
    'rushing_yards': NotRequired[int],
}, total=False)

ModelFanduelResearchClosingLines = TypedDict('ModelFanduelResearchClosingLines', {
    'spread': NotRequired[float],
    'total': NotRequired[float],
}, total=False)

ModelFanduelResearchFixturesResponseDoc = TypedDict('ModelFanduelResearchFixturesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchFixturesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchFixturesResponse = TypedDict('ModelFanduelResearchFixturesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'fixtures': NotRequired[list[ModelFanduelResearchFixture]],
    'sport': NotRequired[str],
}, total=False)

ModelFanduelResearchFixture = TypedDict('ModelFanduelResearchFixture', {
    'event_url': NotRequired[str],
    'game_clock': NotRequired[str],
    'head_to_head_slug': NotRequired[str],
    'id': NotRequired[str],
    'network': NotRequired[str],
    'scheduled_end': NotRequired[str],
    'scheduled_start': NotRequired[str],
    'sport': NotRequired[ModelFanduelResearchSportRef],
    'status': NotRequired[str],
    'teams': NotRequired[list[ModelFanduelResearchFixtureTeam]],
}, total=False)

ModelFanduelResearchFixtureTeam = TypedDict('ModelFanduelResearchFixtureTeam', {
    'abbreviation': NotRequired[str],
    'id': NotRequired[str],
    'money_line': NotRequired[ModelFanduelResearchFixtureLine],
    'name': NotRequired[str],
    'number_fire_id': NotRequired[int],
    'score': NotRequired[int],
    'side': NotRequired[str],
    'spread': NotRequired[ModelFanduelResearchFixtureLine],
    'total': NotRequired[ModelFanduelResearchFixtureLine],
    'win_probability': NotRequired[float],
}, total=False)

ModelFanduelResearchFixtureLine = TypedDict('ModelFanduelResearchFixtureLine', {
    'market_id': NotRequired[str],
    'odds': NotRequired[int],
    'points': NotRequired[float],
    'selection_id': NotRequired[str],
    'side': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelResearchFeaturedArticlesResponseDoc = TypedDict('ModelFanduelResearchFeaturedArticlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchFeaturedArticlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchFeaturedArticlesResponse = TypedDict('ModelFanduelResearchFeaturedArticlesResponse', {
    'articles': NotRequired[list[ModelFanduelResearchArticleSummary]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'sport': NotRequired[ModelFanduelResearchSportRef],
}, total=False)

ModelFanduelResearchArticleSummary = TypedDict('ModelFanduelResearchArticleSummary', {
    'author': NotRequired[ModelFanduelResearchAuthorRef],
    'description': NotRequired[str],
    'hero_type': NotRequired[str],
    'id': NotRequired[str],
    'published_at': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[ModelFanduelResearchSportRef],
    'sub_heading': NotRequired[str],
    'tags': NotRequired[list[ModelFanduelResearchTag]],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelResearchTag = TypedDict('ModelFanduelResearchTag', {
    'name': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelResearchAuthorsResponseDoc = TypedDict('ModelFanduelResearchAuthorsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchAuthorsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchAuthorsResponse = TypedDict('ModelFanduelResearchAuthorsResponse', {
    'authors': NotRequired[list[ModelFanduelResearchAuthor]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'next_cursor': NotRequired[str],
}, total=False)

ModelFanduelResearchAuthor = TypedDict('ModelFanduelResearchAuthor', {
    'bio': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'profile_image_url': NotRequired[str],
    'slug': NotRequired[str],
    'social': NotRequired[list[ModelFanduelResearchSocial]],
    'sports': NotRequired[list[str]],
    'sub_categories': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
}, total=False)

ModelFanduelResearchSocial = TypedDict('ModelFanduelResearchSocial', {
    'account': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelResearchAuthorResponseDoc = TypedDict('ModelFanduelResearchAuthorResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchAuthorResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchAuthorResponse = TypedDict('ModelFanduelResearchAuthorResponse', {
    'bio': NotRequired[str],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'profile_image_url': NotRequired[str],
    'slug': NotRequired[str],
    'social': NotRequired[list[ModelFanduelResearchSocial]],
    'sports': NotRequired[list[str]],
    'sub_categories': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
}, total=False)

ModelFanduelResearchArticlesResponseDoc = TypedDict('ModelFanduelResearchArticlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchArticlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchArticlesResponse = TypedDict('ModelFanduelResearchArticlesResponse', {
    'articles': NotRequired[list[ModelFanduelResearchArticleSummary]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'next_cursor': NotRequired[str],
}, total=False)

ModelFanduelResearchArticleResponseDoc = TypedDict('ModelFanduelResearchArticleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchArticleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchArticleResponse = TypedDict('ModelFanduelResearchArticleResponse', {
    'author': NotRequired[ModelFanduelResearchAuthorRef],
    'blocks': NotRequired[list[ModelFanduelResearchBlock]],
    'description': NotRequired[str],
    'fetched_at': NotRequired[str],
    'hero_type': NotRequired[str],
    'id': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'omitted_blocks': NotRequired[dict[str, int]],
    'published_at': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[ModelFanduelResearchSportRef],
    'sub_heading': NotRequired[str],
    'tags': NotRequired[list[ModelFanduelResearchTag]],
    'text': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelResearchBlock = TypedDict('ModelFanduelResearchBlock', {
    'event_id': NotRequired[int],
    'event_name': NotRequired[str],
    'headers': NotRequired[list[str]],
    'league': NotRequired[str],
    'level': NotRequired[int],
    'market_id': NotRequired[str],
    'market_name': NotRequired[str],
    'rows': NotRequired[list[list[str]]],
    'selection_ids': NotRequired[list[int]],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelResearchResponseDoc = TypedDict('ModelFanduelResearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelResearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelResearchResponse = TypedDict('ModelFanduelResearchResponse', {
    'copyright': NotRequired[str],
    'description': NotRequired[str],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFanduelResearchItem]],
    'language': NotRequired[str],
    'last_build_date': NotRequired[str],
    'site_url': NotRequired[str],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFanduelResearchItem = TypedDict('ModelFanduelResearchItem', {
    'guid': NotRequired[str],
    'image_url': NotRequired[str],
    'published_at': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFanduelRacingWagerTypesResponseDoc = TypedDict('ModelFanduelRacingWagerTypesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingWagerTypesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingWagerTypesResponse = TypedDict('ModelFanduelRacingWagerTypesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'wager_types': NotRequired[list[ModelFanduelRacingWagerType]],
}, total=False)

ModelFanduelRacingWagerType = TypedDict('ModelFanduelRacingWagerType', {
    'code': NotRequired[str],
    'column_count': NotRequired[int],
    'column_type': NotRequired[str],
    'description': NotRequired[str],
    'group': NotRequired[ModelFanduelRacingCodeName],
    'id': NotRequired[int],
    'is_box': NotRequired[bool],
    'is_key': NotRequired[bool],
    'is_wheel': NotRequired[bool],
    'leg_count': NotRequired[int],
    'max_wager': NotRequired[float],
    'min_wager': NotRequired[float],
    'name': NotRequired[str],
    'pools_per_entry': NotRequired[int],
    'position_count': NotRequired[int],
}, total=False)

ModelFanduelRacingCodeName = TypedDict('ModelFanduelRacingCodeName', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFanduelRacingTracksResponseDoc = TypedDict('ModelFanduelRacingTracksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingTracksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingTracksResponse = TypedDict('ModelFanduelRacingTracksResponse', {
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'race_date': NotRequired[str],
    'total': NotRequired[int],
    'tracks': NotRequired[list[ModelFanduelRacingTrack]],
}, total=False)

ModelFanduelRacingTrack = TypedDict('ModelFanduelRacingTrack', {
    'city': NotRequired[str],
    'code': NotRequired[str],
    'country': NotRequired[str],
    'current_race': NotRequired[ModelFanduelRacingNextRace],
    'featured': NotRequired[bool],
    'is_finished': NotRequired[bool],
    'ivr_code': NotRequired[int],
    'name': NotRequired[str],
    'number_of_races': NotRequired[int],
    'race_types': NotRequired[list[str]],
    'short_name': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

ModelFanduelRacingNextRace = TypedDict('ModelFanduelRacingNextRace', {
    'mtp': NotRequired[int],
    'number': NotRequired[str],
    'post_time': NotRequired[str],
    'status': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingTrackResponseDoc = TypedDict('ModelFanduelRacingTrackResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingTrackResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingTrackResponse = TypedDict('ModelFanduelRacingTrackResponse', {
    'city': NotRequired[str],
    'code': NotRequired[str],
    'country': NotRequired[str],
    'current_race': NotRequired[ModelFanduelRacingNextRace],
    'featured': NotRequired[bool],
    'fetched_at': NotRequired[str],
    'is_finished': NotRequired[bool],
    'ivr_code': NotRequired[int],
    'name': NotRequired[str],
    'number_of_races': NotRequired[int],
    'race_types': NotRequired[list[str]],
    'races': NotRequired[list[ModelFanduelRacingRaceSummary]],
    'short_name': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

ModelFanduelRacingRaceSummary = TypedDict('ModelFanduelRacingRaceSummary', {
    'country': NotRequired[str],
    'distance': NotRequired[str],
    'id': NotRequired[str],
    'live_streaming': NotRequired[bool],
    'mtp': NotRequired[int],
    'number': NotRequired[str],
    'post_time': NotRequired[str],
    'purse': NotRequired[float],
    'race_class': NotRequired[ModelFanduelRacingCodeName],
    'race_date': NotRequired[str],
    'race_type': NotRequired[ModelFanduelRacingCodeName],
    'runner_count': NotRequired[int],
    'status': NotRequired[ModelFanduelRacingCodeName],
    'surface': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_name': NotRequired[str],
}, total=False)

ModelFanduelRacingSearchResponseDoc = TypedDict('ModelFanduelRacingSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingSearchResponse = TypedDict('ModelFanduelRacingSearchResponse', {
    'counts': NotRequired[ModelFanduelRacingSearchCounts],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFanduelRacingSearchItem]],
    'limit': NotRequired[int],
    'order': NotRequired[str],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'total': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFanduelRacingSearchItem = TypedDict('ModelFanduelRacingSearchItem', {
    'birth_year': NotRequired[int],
    'id': NotRequired[int],
    'last_event': NotRequired[ModelFanduelRacingLastEvent],
    'name': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFanduelRacingLastEvent = TypedDict('ModelFanduelRacingLastEvent', {
    'date': NotRequired[str],
    'race': NotRequired[int],
    'track': NotRequired[str],
}, total=False)

ModelFanduelRacingSearchCounts = TypedDict('ModelFanduelRacingSearchCounts', {
    'jockey': NotRequired[int],
    'owner': NotRequired[int],
    'runner': NotRequired[int],
    'trainer': NotRequired[int],
}, total=False)

ModelFanduelRacingResultsResponseDoc = TypedDict('ModelFanduelRacingResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingResultsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingResultsResponse = TypedDict('ModelFanduelRacingResultsResponse', {
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'race_date': NotRequired[str],
    'results': NotRequired[list[ModelFanduelRacingResultEntry]],
    'total': NotRequired[int],
}, total=False)

ModelFanduelRacingResultEntry = TypedDict('ModelFanduelRacingResultEntry', {
    'country': NotRequired[str],
    'distance': NotRequired[str],
    'id': NotRequired[str],
    'live_streaming': NotRequired[bool],
    'mtp': NotRequired[int],
    'number': NotRequired[str],
    'post_time': NotRequired[str],
    'purse': NotRequired[float],
    'race_class': NotRequired[ModelFanduelRacingCodeName],
    'race_date': NotRequired[str],
    'race_type': NotRequired[ModelFanduelRacingCodeName],
    'results': NotRequired[ModelFanduelRacingResults],
    'runner_count': NotRequired[int],
    'status': NotRequired[ModelFanduelRacingCodeName],
    'surface': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_name': NotRequired[str],
}, total=False)

ModelFanduelRacingResults = TypedDict('ModelFanduelRacingResults', {
    'finishers': NotRequired[list[ModelFanduelRacingFinisher]],
    'payoffs': NotRequired[list[ModelFanduelRacingPayoff]],
    'winning_time': NotRequired[float],
}, total=False)

ModelFanduelRacingPayoff = TypedDict('ModelFanduelRacingPayoff', {
    'selections': NotRequired[list[ModelFanduelRacingPayoffSelection]],
    'wager_amount': NotRequired[float],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingPayoffSelection = TypedDict('ModelFanduelRacingPayoffSelection', {
    'payout': NotRequired[float],
    'qualifier': NotRequired[str],
    'selection': NotRequired[str],
}, total=False)

ModelFanduelRacingFinisher = TypedDict('ModelFanduelRacingFinisher', {
    'entry': NotRequired[int],
    'finish_status': NotRequired[str],
    'number': NotRequired[str],
    'place_payoff': NotRequired[float],
    'position': NotRequired[int],
    'runner': NotRequired[str],
    'show_payoff': NotRequired[float],
    'silk_url': NotRequired[str],
    'timeform': NotRequired[ModelFanduelRacingFinisherTimeform],
    'win_payoff': NotRequired[float],
}, total=False)

ModelFanduelRacingFinisherTimeform = TypedDict('ModelFanduelRacingFinisherTimeform', {
    'beaten_lengths': NotRequired[float],
    'beaten_text': NotRequired[str],
    'post_race_report': NotRequired[str],
    'starting_price': NotRequired[float],
    'total_beaten_lengths': NotRequired[float],
    'total_beaten_text': NotRequired[str],
}, total=False)

ModelFanduelRacingRacesResponseDoc = TypedDict('ModelFanduelRacingRacesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingRacesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingRacesResponse = TypedDict('ModelFanduelRacingRacesResponse', {
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'race_date': NotRequired[str],
    'races': NotRequired[list[ModelFanduelRacingRaceSummary]],
    'total': NotRequired[int],
}, total=False)

ModelFanduelRacingRaceResponseDoc = TypedDict('ModelFanduelRacingRaceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingRaceResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingRaceResponse = TypedDict('ModelFanduelRacingRaceResponse', {
    'age_restriction': NotRequired[str],
    'analyst_verdict': NotRequired[str],
    'claiming_price': NotRequired[float],
    'country': NotRequired[str],
    'description': NotRequired[str],
    'distance': NotRequired[str],
    'entries': NotRequired[list[ModelFanduelRacingEntry]],
    'fetched_at': NotRequired[str],
    'has_replay': NotRequired[bool],
    'id': NotRequired[str],
    'included': NotRequired[list[str]],
    'last_updated_ms': NotRequired[int],
    'live_streaming': NotRequired[bool],
    'mtp': NotRequired[int],
    'number': NotRequired[str],
    'pools': NotRequired[list[ModelFanduelRacingPool]],
    'post_time': NotRequired[str],
    'probables': NotRequired[list[ModelFanduelRacingProbable]],
    'purse': NotRequired[float],
    'race_class': NotRequired[ModelFanduelRacingCodeName],
    'race_date': NotRequired[str],
    'race_type': NotRequired[ModelFanduelRacingCodeName],
    'results': NotRequired[ModelFanduelRacingResults],
    'runner_count': NotRequired[int],
    'status': NotRequired[ModelFanduelRacingCodeName],
    'surface': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_condition': NotRequired[str],
    'track_name': NotRequired[str],
    'tvg_race_id': NotRequired[int],
    'wagerable_runner_count': NotRequired[int],
    'wagers': NotRequired[list[ModelFanduelRacingWager]],
    'will_pays': NotRequired[list[ModelFanduelRacingWillPay]],
}, total=False)

ModelFanduelRacingWillPay = TypedDict('ModelFanduelRacingWillPay', {
    'leg_results': NotRequired[list[ModelFanduelRacingLegResult]],
    'payoff_type': NotRequired[str],
    'payouts': NotRequired[list[ModelFanduelRacingWillPayment]],
    'wager_amount': NotRequired[float],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingWillPayment = TypedDict('ModelFanduelRacingWillPayment', {
    'entry': NotRequired[int],
    'payout': NotRequired[float],
    'required': NotRequired[float],
}, total=False)

ModelFanduelRacingLegResult = TypedDict('ModelFanduelRacingLegResult', {
    'leg': NotRequired[int],
    'winning_entry': NotRequired[int],
}, total=False)

ModelFanduelRacingWager = TypedDict('ModelFanduelRacingWager', {
    'max_wager': NotRequired[float],
    'min_wager': NotRequired[float],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingProbable = TypedDict('ModelFanduelRacingProbable', {
    'amount': NotRequired[float],
    'combos': NotRequired[list[ModelFanduelRacingCombo]],
    'min_wager': NotRequired[float],
    'pool_amount_total': NotRequired[float],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingCombo = TypedDict('ModelFanduelRacingCombo', {
    'payout': NotRequired[str],
    'runner1': NotRequired[str],
    'runner2': NotRequired[str],
}, total=False)

ModelFanduelRacingPool = TypedDict('ModelFanduelRacingPool', {
    'amount': NotRequired[float],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingEntry = TypedDict('ModelFanduelRacingEntry', {
    'current_odds': NotRequired[ModelFanduelRacingOdds],
    'favorite': NotRequired[bool],
    'morning_line': NotRequired[ModelFanduelRacingOdds],
    'number': NotRequired[int],
    'number_color': NotRequired[str],
    'pool_grids': NotRequired[list[ModelFanduelRacingPoolGrid]],
    'recent_odds': NotRequired[list[ModelFanduelRacingRecentOdd]],
    'runners': NotRequired[list[ModelFanduelRacingRunner]],
    'saddle_color': NotRequired[str],
}, total=False)

ModelFanduelRacingRunner = TypedDict('ModelFanduelRacingRunner', {
    'age': NotRequired[int],
    'dam': NotRequired[str],
    'dam_sire': NotRequired[str],
    'favorite_rank': NotRequired[ModelFanduelRacingFavoriteRank],
    'form_figures': NotRequired[str],
    'handicapping': NotRequired[ModelFanduelRacingHandicapping],
    'jockey': NotRequired[str],
    'jockey_changed': NotRequired[bool],
    'medication': NotRequired[str],
    'name': NotRequired[str],
    'owner': NotRequired[str],
    'rating_stars': NotRequired[int],
    'runner_id': NotRequired[str],
    'scratched': NotRequired[bool],
    'sex': NotRequired[str],
    'sire': NotRequired[str],
    'timeform': NotRequired[ModelFanduelRacingRunnerTimeform],
    'trainer': NotRequired[str],
    'weight': NotRequired[int],
    'win_probability': NotRequired[float],
}, total=False)

ModelFanduelRacingRunnerTimeform = TypedDict('ModelFanduelRacingRunnerTimeform', {
    'analyst_comment': NotRequired[str],
    'flags': NotRequired[list[str]],
    'free_pick': NotRequired[ModelFanduelRacingFreePick],
    'production_comment': NotRequired[str],
    'tissue_price': NotRequired[float],
}, total=False)

ModelFanduelRacingFreePick = TypedDict('ModelFanduelRacingFreePick', {
    'info': NotRequired[str],
    'number': NotRequired[int],
}, total=False)

ModelFanduelRacingHandicapping = TypedDict('ModelFanduelRacingHandicapping', {
    'average_pace': NotRequired[ModelFanduelRacingAveragePace],
    'free_pick': NotRequired[ModelFanduelRacingFreePick],
    'jockey_trainer': NotRequired[ModelFanduelRacingJockeyTrainer],
    'past_results': NotRequired[ModelFanduelRacingPastResults],
    'snapshot': NotRequired[ModelFanduelRacingSnapshot],
    'speed_and_class': NotRequired[ModelFanduelRacingSpeedAndClass],
}, total=False)

ModelFanduelRacingSpeedAndClass = TypedDict('ModelFanduelRacingSpeedAndClass', {
    'avg_class_rating': NotRequired[float],
    'avg_distance': NotRequired[float],
    'avg_speed': NotRequired[float],
    'high_speed': NotRequired[float],
    'high_speed_ranking': NotRequired[str],
    'last_class_rating': NotRequired[float],
    'normalised_speed_rating': NotRequired[float],
}, total=False)

ModelFanduelRacingSnapshot = TypedDict('ModelFanduelRacingSnapshot', {
    'days_off': NotRequired[int],
    'horse_starts': NotRequired[int],
    'horse_wins': NotRequired[int],
    'normalised_power_rating': NotRequired[float],
    'power_rating': NotRequired[float],
    'power_rating_ranking': NotRequired[str],
}, total=False)

ModelFanduelRacingPastResults = TypedDict('ModelFanduelRacingPastResults', {
    'first': NotRequired[int],
    'second': NotRequired[int],
    'starts': NotRequired[int],
    'third': NotRequired[int],
    'top3_percentage': NotRequired[float],
    'top3_percentage_ranking': NotRequired[str],
    'win_percentage': NotRequired[float],
    'win_percentage_ranking': NotRequired[str],
}, total=False)

ModelFanduelRacingJockeyTrainer = TypedDict('ModelFanduelRacingJockeyTrainer', {
    'jockey_entity_id': NotRequired[int],
    'jockey_name': NotRequired[str],
    'places': NotRequired[int],
    'shows': NotRequired[int],
    'starts': NotRequired[int],
    'trainer_entity_id': NotRequired[int],
    'trainer_name': NotRequired[str],
    'wins': NotRequired[int],
}, total=False)

ModelFanduelRacingAveragePace = TypedDict('ModelFanduelRacingAveragePace', {
    'early': NotRequired[float],
    'finish': NotRequired[float],
    'middle': NotRequired[float],
    'races': NotRequired[int],
}, total=False)

ModelFanduelRacingFavoriteRank = TypedDict('ModelFanduelRacingFavoriteRank', {
    'current_odds': NotRequired[int],
    'high_speed': NotRequired[int],
    'morning_line': NotRequired[int],
    'power_rating': NotRequired[int],
}, total=False)

ModelFanduelRacingRecentOdd = TypedDict('ModelFanduelRacingRecentOdd', {
    'odds': NotRequired[str],
    'trending': NotRequired[bool],
}, total=False)

ModelFanduelRacingPoolGrid = TypedDict('ModelFanduelRacingPoolGrid', {
    'cells': NotRequired[list[ModelFanduelRacingPoolCell]],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelRacingPoolCell = TypedDict('ModelFanduelRacingPoolCell', {
    'amount': NotRequired[float],
    'status': NotRequired[str],
    'target': NotRequired[int],
}, total=False)

ModelFanduelRacingOdds = TypedDict('ModelFanduelRacingOdds', {
    'decimal': NotRequired[float],
    'fractional': NotRequired[str],
}, total=False)

ModelFanduelRacingPastTracksResponseDoc = TypedDict('ModelFanduelRacingPastTracksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingPastTracksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingPastTracksResponse = TypedDict('ModelFanduelRacingPastTracksResponse', {
    'date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'total': NotRequired[int],
    'track': NotRequired[str],
    'tracks': NotRequired[list[ModelFanduelRacingPastTrack]],
}, total=False)

ModelFanduelRacingPastTrack = TypedDict('ModelFanduelRacingPastTrack', {
    'city': NotRequired[str],
    'code': NotRequired[str],
    'country': NotRequired[str],
    'dates': NotRequired[list[str]],
    'dates_total': NotRequired[int],
    'name': NotRequired[str],
    'race_types': NotRequired[list[str]],
    'races_on_date': NotRequired[int],
    'state': NotRequired[str],
}, total=False)

ModelFanduelRacingPastRacesResponseDoc = TypedDict('ModelFanduelRacingPastRacesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingPastRacesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingPastRacesResponse = TypedDict('ModelFanduelRacingPastRacesResponse', {
    'date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'races': NotRequired[list[ModelFanduelRacingPastRaceSummary]],
    'total': NotRequired[int],
    'track': NotRequired[str],
}, total=False)

ModelFanduelRacingPastRaceSummary = TypedDict('ModelFanduelRacingPastRaceSummary', {
    'claiming_price': NotRequired[float],
    'date': NotRequired[str],
    'description': NotRequired[str],
    'distance': NotRequired[ModelFanduelRacingPastDistance],
    'id': NotRequired[str],
    'number': NotRequired[str],
    'post_time': NotRequired[str],
    'purse': NotRequired[float],
    'race_class': NotRequired[ModelFanduelRacingCodeName],
    'race_type': NotRequired[ModelFanduelRacingCodeName],
    'runner_count': NotRequired[int],
    'surface': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_condition': NotRequired[str],
    'track_name': NotRequired[str],
}, total=False)

ModelFanduelRacingPastDistance = TypedDict('ModelFanduelRacingPastDistance', {
    'code': NotRequired[str],
    'unit': NotRequired[str],
    'value': NotRequired[float],
}, total=False)

ModelFanduelRacingPastRaceResponseDoc = TypedDict('ModelFanduelRacingPastRaceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingPastRaceResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingPastRaceResponse = TypedDict('ModelFanduelRacingPastRaceResponse', {
    'claiming_price': NotRequired[float],
    'date': NotRequired[str],
    'description': NotRequired[str],
    'distance': NotRequired[ModelFanduelRacingPastDistance],
    'entries': NotRequired[list[ModelFanduelRacingPastEntry]],
    'fetched_at': NotRequired[str],
    'has_replay': NotRequired[bool],
    'id': NotRequired[str],
    'number': NotRequired[str],
    'post_time': NotRequired[str],
    'purse': NotRequired[float],
    'race_class': NotRequired[ModelFanduelRacingCodeName],
    'race_type': NotRequired[ModelFanduelRacingCodeName],
    'results': NotRequired[ModelFanduelRacingResults],
    'runner_count': NotRequired[int],
    'surface': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_condition': NotRequired[str],
    'track_name': NotRequired[str],
}, total=False)

ModelFanduelRacingPastEntry = TypedDict('ModelFanduelRacingPastEntry', {
    'favorite': NotRequired[bool],
    'final_odds': NotRequired[ModelFanduelRacingOdds],
    'morning_line': NotRequired[ModelFanduelRacingOdds],
    'number': NotRequired[int],
    'number_color': NotRequired[str],
    'runners': NotRequired[list[ModelFanduelRacingPastRunner]],
    'saddle_color': NotRequired[str],
}, total=False)

ModelFanduelRacingPastRunner = TypedDict('ModelFanduelRacingPastRunner', {
    'age': NotRequired[int],
    'birth_year': NotRequired[int],
    'dam': NotRequired[str],
    'dam_sire': NotRequired[str],
    'entity_id': NotRequired[str],
    'jockey': NotRequired[str],
    'medication': NotRequired[str],
    'name': NotRequired[str],
    'owner': NotRequired[str],
    'runner_id': NotRequired[str],
    'scratched': NotRequired[bool],
    'sex': NotRequired[str],
    'sire': NotRequired[str],
    'trainer': NotRequired[str],
    'weight': NotRequired[int],
}, total=False)

ModelFanduelRacingHorseResponseDoc = TypedDict('ModelFanduelRacingHorseResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingHorseResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingHorseResponse = TypedDict('ModelFanduelRacingHorseResponse', {
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'races': NotRequired[list[ModelFanduelRacingHorseRace]],
    'starts': NotRequired[int],
    'top3': NotRequired[int],
    'total': NotRequired[int],
    'win_percentage': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelFanduelRacingHorseRace = TypedDict('ModelFanduelRacingHorseRace', {
    'claiming_price': NotRequired[float],
    'date': NotRequired[str],
    'description': NotRequired[str],
    'distance': NotRequired[ModelFanduelRacingPastDistance],
    'id': NotRequired[str],
    'number': NotRequired[str],
    'post_time': NotRequired[str],
    'purse': NotRequired[float],
    'race_class': NotRequired[ModelFanduelRacingCodeName],
    'race_type': NotRequired[ModelFanduelRacingCodeName],
    'result': NotRequired[ModelFanduelRacingFinisher],
    'runner_count': NotRequired[int],
    'surface': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_condition': NotRequired[str],
    'track_name': NotRequired[str],
    'winning_time': NotRequired[float],
}, total=False)

ModelFanduelRacingFiltersResponseDoc = TypedDict('ModelFanduelRacingFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingFiltersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingFiltersResponse = TypedDict('ModelFanduelRacingFiltersResponse', {
    'classes': NotRequired[list[ModelFanduelRacingCount]],
    'countries': NotRequired[list[ModelFanduelRacingCount]],
    'fetched_at': NotRequired[str],
    'race_count': NotRequired[int],
    'race_date': NotRequired[str],
    'race_sorts': NotRequired[list[str]],
    'race_types': NotRequired[list[ModelFanduelRacingCount]],
    'statuses': NotRequired[list[ModelFanduelRacingCount]],
    'surfaces': NotRequired[list[ModelFanduelRacingCount]],
    'track_count': NotRequired[int],
    'track_sorts': NotRequired[list[str]],
}, total=False)

ModelFanduelRacingCount = TypedDict('ModelFanduelRacingCount', {
    'code': NotRequired[str],
    'count': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelFanduelRacingCarryoverResponseDoc = TypedDict('ModelFanduelRacingCarryoverResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelRacingCarryoverResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelRacingCarryoverResponse = TypedDict('ModelFanduelRacingCarryoverResponse', {
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'pools': NotRequired[list[ModelFanduelRacingCarryoverPool]],
    'total': NotRequired[int],
}, total=False)

ModelFanduelRacingCarryoverPool = TypedDict('ModelFanduelRacingCarryoverPool', {
    'amount': NotRequired[float],
    'mtp': NotRequired[int],
    'pool_type': NotRequired[str],
    'post_time': NotRequired[str],
    'race_number': NotRequired[int],
    'race_status': NotRequired[ModelFanduelRacingCodeName],
    'track_code': NotRequired[str],
    'track_name': NotRequired[str],
    'wager_type': NotRequired[ModelFanduelRacingCodeName],
}, total=False)

ModelFanduelCasinoGameResponseDoc = TypedDict('ModelFanduelCasinoGameResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelCasinoGameResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelCasinoGameResponse = TypedDict('ModelFanduelCasinoGameResponse', {
    'badge': NotRequired[str],
    'bet_range': NotRequired[str],
    'category': NotRequired[str],
    'description': NotRequired[str],
    'features': NotRequired[list[str]],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[str],
    'max_bet': NotRequired[float],
    'min_bet': NotRequired[float],
    'name': NotRequired[str],
    'players_now': NotRequired[int],
    'provider_name': NotRequired[str],
    'provider_ref': NotRequired[str],
    'region': NotRequired[str],
    'slug': NotRequired[str],
    'studio': NotRequired[str],
    'summary_tag': NotRequired[str],
    'themes': NotRequired[list[str]],
    'trend': NotRequired[str],
    'url': NotRequired[str],
    'volatility': NotRequired[str],
}, total=False)

ModelFanduelCasinoCategoryResponseDoc = TypedDict('ModelFanduelCasinoCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelCasinoCategoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelCasinoCategoryResponse = TypedDict('ModelFanduelCasinoCategoryResponse', {
    'badges': NotRequired[list[ModelFanduelCasinoCount]],
    'cached_at': NotRequired[str],
    'category': NotRequired[ModelFanduelCasinoCategory],
    'category_total': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelFanduelCasinoGame]],
    'limit': NotRequired[int],
    'lobby': NotRequired[str],
    'offset': NotRequired[int],
    'providers': NotRequired[list[ModelFanduelCasinoCount]],
    'region': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelFanduelCasinoCount = TypedDict('ModelFanduelCasinoCount', {
    'count': NotRequired[int],
    'value': NotRequired[str],
}, total=False)

ModelFanduelCasinoGame = TypedDict('ModelFanduelCasinoGame', {
    'badge': NotRequired[str],
    'game_url': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[int],
    'provider': NotRequired[str],
    'site_wide_jackpot': NotRequired[bool],
    'slug': NotRequired[str],
}, total=False)

ModelFanduelCasinoCategory = TypedDict('ModelFanduelCasinoCategory', {
    'note': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFanduelCasinoCategoriesResponseDoc = TypedDict('ModelFanduelCasinoCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFanduelCasinoCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFanduelCasinoCategoriesResponse = TypedDict('ModelFanduelCasinoCategoriesResponse', {
    'categories': NotRequired[list[ModelFanduelCasinoCategory]],
    'fetched_at': NotRequired[str],
    'lobby': NotRequired[str],
    'region': NotRequired[str],
    'regions': NotRequired[list[str]],
}, total=False)

FanduelCasinoCategoriesResponse = ModelFanduelCasinoCategoriesResponseDoc
FanduelCasinoCategoriesParams = TypedDict('FanduelCasinoCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'region': NotRequired[Literal['mi', 'on']],
}, total=False)

FanduelCasinoCategoryResponse = ModelFanduelCasinoCategoryResponseDoc
FanduelCasinoCategoryParams = TypedDict('FanduelCasinoCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'region': NotRequired[Literal['mi', 'on']],
    'category': Required[Literal['all-games', 'new', 'slots', 'double-your-bet-category', 'jackpots', 'daily-jackpots', 'hot-slots', 'classic-reels-category', 'bonus-buy-category', 'high-limit-category', 'spooky-slots-category', 'exclusives', 'pick-play', 'arcade', 'blackjack', 'baccarat', 'roulette', 'table', 'livecasino', 'online-casino-favorites', 'explore-videos', 'motorcity-favorites', 'fallsview-favourites-category', 'the-wolf-den-category', 'sports-central']],
    'q': NotRequired[str],
    'provider': NotRequired[str],
    'badge': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelCasinoGameResponse = ModelFanduelCasinoGameResponseDoc
FanduelCasinoGameParams = TypedDict('FanduelCasinoGameParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'region': NotRequired[Literal['mi', 'on']],
    'game': Required[str],
}, total=False)

FanduelRacingCarryoverPoolsResponse = ModelFanduelRacingCarryoverResponseDoc
FanduelRacingCarryoverPoolsParams = TypedDict('FanduelRacingCarryoverPoolsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingFiltersResponse = ModelFanduelRacingFiltersResponseDoc
FanduelRacingFiltersParams = TypedDict('FanduelRacingFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FanduelRacingHorseResponse = ModelFanduelRacingHorseResponseDoc
FanduelRacingHorseParams = TypedDict('FanduelRacingHorseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastRaceResponse = ModelFanduelRacingPastRaceResponseDoc
FanduelRacingPastRaceParams = TypedDict('FanduelRacingPastRaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'date': Required[str],
    'track': Required[str],
    'number': Required[str],
}, total=False)

FanduelRacingPastRacesResponse = ModelFanduelRacingPastRacesResponseDoc
FanduelRacingPastRacesParams = TypedDict('FanduelRacingPastRacesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'date': Required[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastTracksResponse = ModelFanduelRacingPastTracksResponseDoc
FanduelRacingPastTracksParams = TypedDict('FanduelRacingPastTracksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'date': NotRequired[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingRaceResponse = ModelFanduelRacingRaceResponseDoc
FanduelRacingRaceParams = TypedDict('FanduelRacingRaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'track': Required[str],
    'number': Required[str],
    'include': NotRequired[Literal['handicapping', 'timeform', 'pool_grids']],
}, total=False)

FanduelRacingRacesResponse = ModelFanduelRacingRacesResponseDoc
FanduelRacingRacesParams = TypedDict('FanduelRacingRacesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'open': NotRequired[bool],
    'within_minutes': NotRequired[int],
    'sort': NotRequired[Literal['mtp', 'post_time', 'race_number']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingResultsResponse = ModelFanduelRacingResultsResponseDoc
FanduelRacingResultsParams = TypedDict('FanduelRacingResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingSearchResponse = ModelFanduelRacingSearchResponseDoc
FanduelRacingSearchParams = TypedDict('FanduelRacingSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'type': NotRequired[Literal['runner', 'jockey', 'trainer', 'owner']],
    'sort': NotRequired[Literal['name', 'last_event']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingTrackResponse = ModelFanduelRacingTrackResponseDoc
FanduelRacingTrackParams = TypedDict('FanduelRacingTrackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'code': Required[str],
}, total=False)

FanduelRacingTracksResponse = ModelFanduelRacingTracksResponseDoc
FanduelRacingTracksParams = TypedDict('FanduelRacingTracksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'code': NotRequired[str],
    'finished': NotRequired[bool],
    'featured': NotRequired[bool],
    'sort': NotRequired[Literal['name', 'mtp', 'wagerable_mtp', 'ivr']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingWagerTypesResponse = ModelFanduelRacingWagerTypesResponseDoc
FanduelRacingWagerTypesParams = TypedDict('FanduelRacingWagerTypesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FanduelResearchResponse = ModelFanduelResearchResponseDoc
FanduelResearchParams = TypedDict('FanduelResearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FanduelResearchArticleResponse = ModelFanduelResearchArticleResponseDoc
FanduelResearchArticleParams = TypedDict('FanduelResearchArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'article': Required[str],
}, total=False)

FanduelResearchArticlesResponse = ModelFanduelResearchArticlesResponseDoc
FanduelResearchArticlesParams = TypedDict('FanduelResearchArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'exclude_sport': NotRequired[str],
    'sub_category': NotRequired[str],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'author': NotRequired[str],
    'hero_type': NotRequired[Literal['IMAGE', 'JWPLAYER']],
    'published_after': NotRequired[str],
    'published_before': NotRequired[str],
    'hide_deprioritized': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchAuthorResponse = ModelFanduelResearchAuthorResponseDoc
FanduelResearchAuthorParams = TypedDict('FanduelResearchAuthorParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'author': Required[str],
}, total=False)

FanduelResearchAuthorsResponse = ModelFanduelResearchAuthorsResponseDoc
FanduelResearchAuthorsParams = TypedDict('FanduelResearchAuthorsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchFeaturedArticlesResponse = ModelFanduelResearchFeaturedArticlesResponseDoc
FanduelResearchFeaturedArticlesParams = TypedDict('FanduelResearchFeaturedArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchFixturesResponse = ModelFanduelResearchFixturesResponseDoc
FanduelResearchFixturesParams = TypedDict('FanduelResearchFixturesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['nba', 'nfl', 'nhl', 'mlb']],
}, total=False)

FanduelResearchNflScheduleResponse = ModelFanduelResearchNflScheduleResponseDoc
FanduelResearchNflScheduleParams = TypedDict('FanduelResearchNflScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'week': Required[int],
    'season_type': NotRequired[Literal['PRE', 'REGULAR', 'POST']],
}, total=False)

FanduelResearchPlayerNewsResponse = ModelFanduelResearchPlayerNewsResponseDoc
FanduelResearchPlayerNewsParams = TypedDict('FanduelResearchPlayerNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['nfl', 'nba', 'mlb', 'nhl']],
    'news_type': NotRequired[Literal['INJURY', 'RECAP', 'TRANSACTION', 'LINEUP', 'GAME_UPDATE', 'OUTLOOK']],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'position': NotRequired[Literal['G', 'F', 'C', 'W', 'D', 'QB', 'DB', 'DL', 'K', 'LB', 'OL', 'P', 'RB', 'TE', 'WR', 'IF', 'OF', 'DH']],
    'include_non_primary': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchQuickPicksDailyResponse = ModelFanduelQuickPicksDailyResponseDoc
FanduelResearchQuickPicksDailyParams = TypedDict('FanduelResearchQuickPicksDailyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchProjectionSlatesResponse = ModelFanduelResearchProjectionSlatesResponseDoc
FanduelResearchProjectionSlatesParams = TypedDict('FanduelResearchProjectionSlatesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
}, total=False)

FanduelResearchProjectionTablesResponse = ModelFanduelResearchProjectionTablesResponseDoc
FanduelResearchProjectionTablesParams = TypedDict('FanduelResearchProjectionTablesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
}, total=False)

FanduelResearchProjectionsResponse = ModelFanduelResearchProjectionsResponseDoc
FanduelResearchProjectionsParams = TypedDict('FanduelResearchProjectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'type': Required[Literal['DAILY', 'WEEKLY', 'YEARLY', 'REMAINING', 'PPR', 'SEASON_STATS']],
    'position': NotRequired[Literal['batters', 'pitchers', 'c', '1b', '2b', '3b', 'ss', 'of', 'sp', 'rp', 'qb', 'rb', 'wr', 'te', 'flex', 'k', 'defense', 'all', 'pg', 'sg', 'guards', 'sf', 'pf', 'forwards', 'centers', 'skaters', 'goalies', 'wingers', 'd', 'idp']],
    'scope': NotRequired[Literal['TOTAL', 'PER_GAME']],
    'slate_id': NotRequired[str],
    'event_id': NotRequired[str],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelResearchSportsResponse = ModelFanduelResearchSportsResponseDoc
FanduelResearchSportsParams = TypedDict('FanduelResearchSportsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchSubCategoriesResponse = ModelFanduelResearchSubCategoriesResponseDoc
FanduelResearchSubCategoriesParams = TypedDict('FanduelResearchSubCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FanduelSportsbookAutocompleteResponse = ModelFanduelSportsbookAutocompleteResponseDoc
FanduelSportsbookAutocompleteParams = TypedDict('FanduelSportsbookAutocompleteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookBuilderResponse = ModelFanduelSportsbookBuilderResponseDoc
FanduelSportsbookBuilderParams = TypedDict('FanduelSportsbookBuilderParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderEventsResponse = ModelFanduelSportsbookBuilderEventsResponseDoc
FanduelSportsbookBuilderEventsParams = TypedDict('FanduelSportsbookBuilderEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderQuotesResponse = ModelFanduelSportsbookChoiceQuotesResponseDoc
FanduelSportsbookBuilderQuotesParams = TypedDict('FanduelSportsbookBuilderQuotesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ramp_event_id': Required[int],
    'choice_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookCompetitionResponse = ModelFanduelSportsbookPageResponseDoc
FanduelSportsbookCompetitionParams = TypedDict('FanduelSportsbookCompetitionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookEventResponse = ModelFanduelSportsbookEventResponseDoc
FanduelSportsbookEventParams = TypedDict('FanduelSportsbookEventParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
}, total=False)

FanduelSportsbookEventBoxScoreResponse = ModelFanduelSportsbookBoxScoreResponseDoc
FanduelSportsbookEventBoxScoreParams = TypedDict('FanduelSportsbookEventBoxScoreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventPlayByPlayResponse = ModelFanduelSportsbookPlayByPlayResponseDoc
FanduelSportsbookEventPlayByPlayParams = TypedDict('FanduelSportsbookEventPlayByPlayParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
    'current': NotRequired[bool],
}, total=False)

FanduelSportsbookEventPlayersResponse = ModelFanduelSportsbookEventPlayersResponseDoc
FanduelSportsbookEventPlayersParams = TypedDict('FanduelSportsbookEventPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventScoreResponse = ModelFanduelSportsbookEventScoreResponseDoc
FanduelSportsbookEventScoreParams = TypedDict('FanduelSportsbookEventScoreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventStatsResponse = ModelFanduelSportsbookEventStatsResponseDoc
FanduelSportsbookEventStatsParams = TypedDict('FanduelSportsbookEventStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventsStatusResponse = ModelFanduelSportsbookEventsStatusResponseDoc
FanduelSportsbookEventsStatusParams = TypedDict('FanduelSportsbookEventsStatusParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookHomeResponse = ModelFanduelSportsbookPageResponseDoc
FanduelSportsbookHomeParams = TypedDict('FanduelSportsbookHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLeagueResponse = ModelFanduelSportsbookPageResponseDoc
FanduelSportsbookLeagueParams = TypedDict('FanduelSportsbookLeagueParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'custom_page_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLiveResponse = ModelFanduelSportsbookPageResponseDoc
FanduelSportsbookLiveParams = TypedDict('FanduelSportsbookLiveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLiveCountResponse = ModelFanduelSportsbookLiveCountResponseDoc
FanduelSportsbookLiveCountParams = TypedDict('FanduelSportsbookLiveCountParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookLiveDataResponse = ModelFanduelSportsbookLiveDataResponseDoc
FanduelSportsbookLiveDataParams = TypedDict('FanduelSportsbookLiveDataParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[str],
}, total=False)

FanduelSportsbookLiveScoresResponse = ModelFanduelSportsbookLiveScoresResponseDoc
FanduelSportsbookLiveScoresParams = TypedDict('FanduelSportsbookLiveScoresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookMarketPricesResponse = ModelFanduelSportsbookMarketPricesResponseDoc
FanduelSportsbookMarketPricesParams = TypedDict('FanduelSportsbookMarketPricesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'market_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookParlaysResponse = ModelFanduelSportsbookParlaysResponseDoc
FanduelSportsbookParlaysParams = TypedDict('FanduelSportsbookParlaysParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'view': NotRequired[Literal['popular', 'all', 'next-to-start', 'event']],
    'event_id': NotRequired[int],
    'type': NotRequired[Literal['PARLAY', 'SGP', 'SGP_PLUS']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': NotRequired[str],
    'min_odds': NotRequired[float],
    'max_odds': NotRequired[float],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookPlayerResponse = ModelFanduelSportsbookPlayerResponseDoc
FanduelSportsbookPlayerParams = TypedDict('FanduelSportsbookPlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerNewsResponse = ModelFanduelSportsbookPlayerNewsResponseDoc
FanduelSportsbookPlayerNewsParams = TypedDict('FanduelSportsbookPlayerNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookPlayerPropsResponse = ModelFanduelSportsbookPlayerPropsResponseDoc
FanduelSportsbookPlayerPropsParams = TypedDict('FanduelSportsbookPlayerPropsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerStatsResponse = ModelFanduelSportsbookPlayerStatsResponseDoc
FanduelSportsbookPlayerStatsParams = TypedDict('FanduelSportsbookPlayerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayersResponse = ModelFanduelSportsbookPlayersResponseDoc
FanduelSportsbookPlayersParams = TypedDict('FanduelSportsbookPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba']],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelSportsbookPromotionsResponse = ModelFanduelSportsbookPromotionsResponseDoc
FanduelSportsbookPromotionsParams = TypedDict('FanduelSportsbookPromotionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'context': NotRequired[Literal['home', 'league', 'sport']],
    'custom_page_id': NotRequired[str],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'tag': NotRequired[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookScheduleResponse = ModelFanduelSportsbookLeagueScheduleResponseDoc
FanduelSportsbookScheduleParams = TypedDict('FanduelSportsbookScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
    'week': NotRequired[str],
    'date': NotRequired[str],
    'end_date': NotRequired[str],
}, total=False)

FanduelSportsbookSearchResponse = ModelFanduelSportsbookSearchResponseDoc
FanduelSportsbookSearchParams = TypedDict('FanduelSportsbookSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'event', 'competition']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'limit': NotRequired[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookSearchTabsResponse = ModelFanduelSportsbookSearchTabsResponseDoc
FanduelSportsbookSearchTabsParams = TypedDict('FanduelSportsbookSearchTabsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'tab': NotRequired[str],
    'pill': NotRequired[str],
    'start_index': NotRequired[int],
    'timezone': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookSportResponse = ModelFanduelSportsbookPageResponseDoc
FanduelSportsbookSportParams = TypedDict('FanduelSportsbookSportParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookSportsResponse = ModelFanduelSportsbookSportsResponseDoc
FanduelSportsbookSportsParams = TypedDict('FanduelSportsbookSportsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookStandingsResponse = ModelFanduelSportsbookStandingsResponseDoc
FanduelSportsbookStandingsParams = TypedDict('FanduelSportsbookStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
}, total=False)

FanduelSportsbookStatsResponse = ModelFanduelSportsbookStatsListResponseDoc
FanduelSportsbookStatsParams = TypedDict('FanduelSportsbookStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'competition_id': NotRequired[int],
}, total=False)

FanduelSportsbookTeamDepthChartResponse = ModelFanduelSportsbookDepthChartResponseDoc
FanduelSportsbookTeamDepthChartParams = TypedDict('FanduelSportsbookTeamDepthChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamNewsResponse = ModelFanduelSportsbookTeamNewsResponseDoc
FanduelSportsbookTeamNewsParams = TypedDict('FanduelSportsbookTeamNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookTeamOddsResponse = ModelFanduelSportsbookTeamOddsResponseDoc
FanduelSportsbookTeamOddsParams = TypedDict('FanduelSportsbookTeamOddsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamRosterResponse = ModelFanduelSportsbookRosterResponseDoc
FanduelSportsbookTeamRosterParams = TypedDict('FanduelSportsbookTeamRosterParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'injured_only': NotRequired[bool],
    'status': NotRequired[str],
    'position': NotRequired[str],
}, total=False)

FanduelSportsbookTeamScheduleResponse = ModelFanduelSportsbookScheduleResponseDoc
FanduelSportsbookTeamScheduleParams = TypedDict('FanduelSportsbookTeamScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamStatsResponse = ModelFanduelSportsbookTeamStatsResponseDoc
FanduelSportsbookTeamStatsParams = TypedDict('FanduelSportsbookTeamStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamsResponse = ModelFanduelSportsbookTeamsResponseDoc
FanduelSportsbookTeamsParams = TypedDict('FanduelSportsbookTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': NotRequired[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
}, total=False)

FanduelSportsbookTrendingResponse = ModelFanduelSportsbookTrendingResponseDoc
FanduelSportsbookTrendingParams = TypedDict('FanduelSportsbookTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'enriched': NotRequired[bool],
}, total=False)

class FanduelGroup:
    @overload
    def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesTextResponseParams]) -> str: ...
    @overload
    def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesDefaultParams]) -> FanduelCasinoCategoriesResponse: ...
    @overload
    def casino_category(self, **params: Unpack[FanduelCasinoCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def casino_category(self, **params: Unpack[FanduelCasinoCategoryTextResponseParams]) -> str: ...
    @overload
    def casino_category(self, **params: Unpack[FanduelCasinoCategoryDefaultParams]) -> FanduelCasinoCategoryResponse: ...
    @overload
    def casino_game(self, **params: Unpack[FanduelCasinoGameStreamParams]) -> BinaryIO: ...
    @overload
    def casino_game(self, **params: Unpack[FanduelCasinoGameTextResponseParams]) -> str: ...
    @overload
    def casino_game(self, **params: Unpack[FanduelCasinoGameDefaultParams]) -> FanduelCasinoGameResponse: ...
    @overload
    def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsStreamParams]) -> BinaryIO: ...
    @overload
    def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsTextResponseParams]) -> str: ...
    @overload
    def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsDefaultParams]) -> FanduelRacingCarryoverPoolsResponse: ...
    @overload
    def racing_filters(self, **params: Unpack[FanduelRacingFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def racing_filters(self, **params: Unpack[FanduelRacingFiltersTextResponseParams]) -> str: ...
    @overload
    def racing_filters(self, **params: Unpack[FanduelRacingFiltersDefaultParams]) -> FanduelRacingFiltersResponse: ...
    @overload
    def racing_horse(self, **params: Unpack[FanduelRacingHorseStreamParams]) -> BinaryIO: ...
    @overload
    def racing_horse(self, **params: Unpack[FanduelRacingHorseTextResponseParams]) -> str: ...
    @overload
    def racing_horse(self, **params: Unpack[FanduelRacingHorseDefaultParams]) -> FanduelRacingHorseResponse: ...
    @overload
    def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceStreamParams]) -> BinaryIO: ...
    @overload
    def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceTextResponseParams]) -> str: ...
    @overload
    def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceDefaultParams]) -> FanduelRacingPastRaceResponse: ...
    @overload
    def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesStreamParams]) -> BinaryIO: ...
    @overload
    def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesTextResponseParams]) -> str: ...
    @overload
    def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesDefaultParams]) -> FanduelRacingPastRacesResponse: ...
    @overload
    def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksStreamParams]) -> BinaryIO: ...
    @overload
    def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksTextResponseParams]) -> str: ...
    @overload
    def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksDefaultParams]) -> FanduelRacingPastTracksResponse: ...
    @overload
    def racing_race(self, **params: Unpack[FanduelRacingRaceStreamParams]) -> BinaryIO: ...
    @overload
    def racing_race(self, **params: Unpack[FanduelRacingRaceTextResponseParams]) -> str: ...
    @overload
    def racing_race(self, **params: Unpack[FanduelRacingRaceDefaultParams]) -> FanduelRacingRaceResponse: ...
    @overload
    def racing_races(self, **params: Unpack[FanduelRacingRacesStreamParams]) -> BinaryIO: ...
    @overload
    def racing_races(self, **params: Unpack[FanduelRacingRacesTextResponseParams]) -> str: ...
    @overload
    def racing_races(self, **params: Unpack[FanduelRacingRacesDefaultParams]) -> FanduelRacingRacesResponse: ...
    @overload
    def racing_results(self, **params: Unpack[FanduelRacingResultsStreamParams]) -> BinaryIO: ...
    @overload
    def racing_results(self, **params: Unpack[FanduelRacingResultsTextResponseParams]) -> str: ...
    @overload
    def racing_results(self, **params: Unpack[FanduelRacingResultsDefaultParams]) -> FanduelRacingResultsResponse: ...
    @overload
    def racing_search(self, **params: Unpack[FanduelRacingSearchStreamParams]) -> BinaryIO: ...
    @overload
    def racing_search(self, **params: Unpack[FanduelRacingSearchTextResponseParams]) -> str: ...
    @overload
    def racing_search(self, **params: Unpack[FanduelRacingSearchDefaultParams]) -> FanduelRacingSearchResponse: ...
    @overload
    def racing_track(self, **params: Unpack[FanduelRacingTrackStreamParams]) -> BinaryIO: ...
    @overload
    def racing_track(self, **params: Unpack[FanduelRacingTrackTextResponseParams]) -> str: ...
    @overload
    def racing_track(self, **params: Unpack[FanduelRacingTrackDefaultParams]) -> FanduelRacingTrackResponse: ...
    @overload
    def racing_tracks(self, **params: Unpack[FanduelRacingTracksStreamParams]) -> BinaryIO: ...
    @overload
    def racing_tracks(self, **params: Unpack[FanduelRacingTracksTextResponseParams]) -> str: ...
    @overload
    def racing_tracks(self, **params: Unpack[FanduelRacingTracksDefaultParams]) -> FanduelRacingTracksResponse: ...
    @overload
    def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesStreamParams]) -> BinaryIO: ...
    @overload
    def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesTextResponseParams]) -> str: ...
    @overload
    def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesDefaultParams]) -> FanduelRacingWagerTypesResponse: ...
    @overload
    def research(self, **params: Unpack[FanduelResearchStreamParams]) -> BinaryIO: ...
    @overload
    def research(self, **params: Unpack[FanduelResearchTextResponseParams]) -> str: ...
    @overload
    def research(self, **params: Unpack[FanduelResearchDefaultParams]) -> FanduelResearchResponse: ...
    @overload
    def research_article(self, **params: Unpack[FanduelResearchArticleStreamParams]) -> BinaryIO: ...
    @overload
    def research_article(self, **params: Unpack[FanduelResearchArticleTextResponseParams]) -> str: ...
    @overload
    def research_article(self, **params: Unpack[FanduelResearchArticleDefaultParams]) -> FanduelResearchArticleResponse: ...
    @overload
    def research_articles(self, **params: Unpack[FanduelResearchArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def research_articles(self, **params: Unpack[FanduelResearchArticlesTextResponseParams]) -> str: ...
    @overload
    def research_articles(self, **params: Unpack[FanduelResearchArticlesDefaultParams]) -> FanduelResearchArticlesResponse: ...
    @overload
    def research_author(self, **params: Unpack[FanduelResearchAuthorStreamParams]) -> BinaryIO: ...
    @overload
    def research_author(self, **params: Unpack[FanduelResearchAuthorTextResponseParams]) -> str: ...
    @overload
    def research_author(self, **params: Unpack[FanduelResearchAuthorDefaultParams]) -> FanduelResearchAuthorResponse: ...
    @overload
    def research_authors(self, **params: Unpack[FanduelResearchAuthorsStreamParams]) -> BinaryIO: ...
    @overload
    def research_authors(self, **params: Unpack[FanduelResearchAuthorsTextResponseParams]) -> str: ...
    @overload
    def research_authors(self, **params: Unpack[FanduelResearchAuthorsDefaultParams]) -> FanduelResearchAuthorsResponse: ...
    @overload
    def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesTextResponseParams]) -> str: ...
    @overload
    def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesDefaultParams]) -> FanduelResearchFeaturedArticlesResponse: ...
    @overload
    def research_fixtures(self, **params: Unpack[FanduelResearchFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def research_fixtures(self, **params: Unpack[FanduelResearchFixturesTextResponseParams]) -> str: ...
    @overload
    def research_fixtures(self, **params: Unpack[FanduelResearchFixturesDefaultParams]) -> FanduelResearchFixturesResponse: ...
    @overload
    def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleTextResponseParams]) -> str: ...
    @overload
    def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleDefaultParams]) -> FanduelResearchNflScheduleResponse: ...
    @overload
    def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsTextResponseParams]) -> str: ...
    @overload
    def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsDefaultParams]) -> FanduelResearchPlayerNewsResponse: ...
    @overload
    def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyStreamParams]) -> BinaryIO: ...
    @overload
    def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyTextResponseParams]) -> str: ...
    @overload
    def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyDefaultParams]) -> FanduelResearchQuickPicksDailyResponse: ...
    @overload
    def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesStreamParams]) -> BinaryIO: ...
    @overload
    def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesTextResponseParams]) -> str: ...
    @overload
    def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesDefaultParams]) -> FanduelResearchProjectionSlatesResponse: ...
    @overload
    def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesStreamParams]) -> BinaryIO: ...
    @overload
    def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesTextResponseParams]) -> str: ...
    @overload
    def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesDefaultParams]) -> FanduelResearchProjectionTablesResponse: ...
    @overload
    def research_projections(self, **params: Unpack[FanduelResearchProjectionsStreamParams]) -> BinaryIO: ...
    @overload
    def research_projections(self, **params: Unpack[FanduelResearchProjectionsTextResponseParams]) -> str: ...
    @overload
    def research_projections(self, **params: Unpack[FanduelResearchProjectionsDefaultParams]) -> FanduelResearchProjectionsResponse: ...
    @overload
    def research_sports(self, **params: Unpack[FanduelResearchSportsStreamParams]) -> BinaryIO: ...
    @overload
    def research_sports(self, **params: Unpack[FanduelResearchSportsTextResponseParams]) -> str: ...
    @overload
    def research_sports(self, **params: Unpack[FanduelResearchSportsDefaultParams]) -> FanduelResearchSportsResponse: ...
    @overload
    def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesTextResponseParams]) -> str: ...
    @overload
    def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesDefaultParams]) -> FanduelResearchSubCategoriesResponse: ...
    @overload
    def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteTextResponseParams]) -> str: ...
    @overload
    def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteDefaultParams]) -> FanduelSportsbookAutocompleteResponse: ...
    @overload
    def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderTextResponseParams]) -> str: ...
    @overload
    def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderDefaultParams]) -> FanduelSportsbookBuilderResponse: ...
    @overload
    def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsDefaultParams]) -> FanduelSportsbookBuilderEventsResponse: ...
    @overload
    def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesTextResponseParams]) -> str: ...
    @overload
    def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesDefaultParams]) -> FanduelSportsbookBuilderQuotesResponse: ...
    @overload
    def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionTextResponseParams]) -> str: ...
    @overload
    def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionDefaultParams]) -> FanduelSportsbookCompetitionResponse: ...
    @overload
    def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventDefaultParams]) -> FanduelSportsbookEventResponse: ...
    @overload
    def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreDefaultParams]) -> FanduelSportsbookEventBoxScoreResponse: ...
    @overload
    def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayDefaultParams]) -> FanduelSportsbookEventPlayByPlayResponse: ...
    @overload
    def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersDefaultParams]) -> FanduelSportsbookEventPlayersResponse: ...
    @overload
    def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreDefaultParams]) -> FanduelSportsbookEventScoreResponse: ...
    @overload
    def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsDefaultParams]) -> FanduelSportsbookEventStatsResponse: ...
    @overload
    def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusTextResponseParams]) -> str: ...
    @overload
    def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusDefaultParams]) -> FanduelSportsbookEventsStatusResponse: ...
    @overload
    def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeTextResponseParams]) -> str: ...
    @overload
    def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeDefaultParams]) -> FanduelSportsbookHomeResponse: ...
    @overload
    def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueTextResponseParams]) -> str: ...
    @overload
    def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueDefaultParams]) -> FanduelSportsbookLeagueResponse: ...
    @overload
    def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveDefaultParams]) -> FanduelSportsbookLiveResponse: ...
    @overload
    def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountDefaultParams]) -> FanduelSportsbookLiveCountResponse: ...
    @overload
    def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataDefaultParams]) -> FanduelSportsbookLiveDataResponse: ...
    @overload
    def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresDefaultParams]) -> FanduelSportsbookLiveScoresResponse: ...
    @overload
    def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesTextResponseParams]) -> str: ...
    @overload
    def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesDefaultParams]) -> FanduelSportsbookMarketPricesResponse: ...
    @overload
    def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysTextResponseParams]) -> str: ...
    @overload
    def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysDefaultParams]) -> FanduelSportsbookParlaysResponse: ...
    @overload
    def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerDefaultParams]) -> FanduelSportsbookPlayerResponse: ...
    @overload
    def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsDefaultParams]) -> FanduelSportsbookPlayerNewsResponse: ...
    @overload
    def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsDefaultParams]) -> FanduelSportsbookPlayerPropsResponse: ...
    @overload
    def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsDefaultParams]) -> FanduelSportsbookPlayerStatsResponse: ...
    @overload
    def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersTextResponseParams]) -> str: ...
    @overload
    def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersDefaultParams]) -> FanduelSportsbookPlayersResponse: ...
    @overload
    def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsDefaultParams]) -> FanduelSportsbookPromotionsResponse: ...
    @overload
    def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleTextResponseParams]) -> str: ...
    @overload
    def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleDefaultParams]) -> FanduelSportsbookScheduleResponse: ...
    @overload
    def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchTextResponseParams]) -> str: ...
    @overload
    def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchDefaultParams]) -> FanduelSportsbookSearchResponse: ...
    @overload
    def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsDefaultParams]) -> FanduelSportsbookSearchTabsResponse: ...
    @overload
    def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportTextResponseParams]) -> str: ...
    @overload
    def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportDefaultParams]) -> FanduelSportsbookSportResponse: ...
    @overload
    def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsDefaultParams]) -> FanduelSportsbookSportsResponse: ...
    @overload
    def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsDefaultParams]) -> FanduelSportsbookStandingsResponse: ...
    @overload
    def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsDefaultParams]) -> FanduelSportsbookStatsResponse: ...
    @overload
    def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartDefaultParams]) -> FanduelSportsbookTeamDepthChartResponse: ...
    @overload
    def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsDefaultParams]) -> FanduelSportsbookTeamNewsResponse: ...
    @overload
    def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsDefaultParams]) -> FanduelSportsbookTeamOddsResponse: ...
    @overload
    def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterDefaultParams]) -> FanduelSportsbookTeamRosterResponse: ...
    @overload
    def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleDefaultParams]) -> FanduelSportsbookTeamScheduleResponse: ...
    @overload
    def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsDefaultParams]) -> FanduelSportsbookTeamStatsResponse: ...
    @overload
    def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsDefaultParams]) -> FanduelSportsbookTeamsResponse: ...
    @overload
    def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingTextResponseParams]) -> str: ...
    @overload
    def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingDefaultParams]) -> FanduelSportsbookTrendingResponse: ...

OperationId = Literal[
    'fanduel-casino-categories',
    'fanduel-casino-category',
    'fanduel-casino-game',
    'fanduel-racing-carryover-pools',
    'fanduel-racing-filters',
    'fanduel-racing-horse',
    'fanduel-racing-past-race',
    'fanduel-racing-past-races',
    'fanduel-racing-past-tracks',
    'fanduel-racing-race',
    'fanduel-racing-races',
    'fanduel-racing-results',
    'fanduel-racing-search',
    'fanduel-racing-track',
    'fanduel-racing-tracks',
    'fanduel-racing-wager-types',
    'fanduel-research',
    'fanduel-research-article',
    'fanduel-research-articles',
    'fanduel-research-author',
    'fanduel-research-authors',
    'fanduel-research-featured-articles',
    'fanduel-research-fixtures',
    'fanduel-research-nfl-schedule',
    'fanduel-research-player-news',
    'fanduel-research-quick-picks-daily',
    'fanduel-research-projection-slates',
    'fanduel-research-projection-tables',
    'fanduel-research-projections',
    'fanduel-research-sports',
    'fanduel-research-sub-categories',
    'fanduel-sportsbook-autocomplete',
    'fanduel-sportsbook-builder',
    'fanduel-sportsbook-builder-events',
    'fanduel-sportsbook-builder-quotes',
    'fanduel-sportsbook-competition',
    'fanduel-sportsbook-event',
    'fanduel-sportsbook-event-box-score',
    'fanduel-sportsbook-event-play-by-play',
    'fanduel-sportsbook-event-players',
    'fanduel-sportsbook-event-score',
    'fanduel-sportsbook-event-stats',
    'fanduel-sportsbook-events-status',
    'fanduel-sportsbook-home',
    'fanduel-sportsbook-league',
    'fanduel-sportsbook-live',
    'fanduel-sportsbook-live-count',
    'fanduel-sportsbook-live-data',
    'fanduel-sportsbook-live-scores',
    'fanduel-sportsbook-market-prices',
    'fanduel-sportsbook-parlays',
    'fanduel-sportsbook-player',
    'fanduel-sportsbook-player-news',
    'fanduel-sportsbook-player-props',
    'fanduel-sportsbook-player-stats',
    'fanduel-sportsbook-players',
    'fanduel-sportsbook-promotions',
    'fanduel-sportsbook-schedule',
    'fanduel-sportsbook-search',
    'fanduel-sportsbook-search-tabs',
    'fanduel-sportsbook-sport',
    'fanduel-sportsbook-sports',
    'fanduel-sportsbook-standings',
    'fanduel-sportsbook-stats',
    'fanduel-sportsbook-team-depth-chart',
    'fanduel-sportsbook-team-news',
    'fanduel-sportsbook-team-odds',
    'fanduel-sportsbook-team-roster',
    'fanduel-sportsbook-team-schedule',
    'fanduel-sportsbook-team-stats',
    'fanduel-sportsbook-teams',
    'fanduel-sportsbook-trending',
]

class CrawloraClient:
    fanduel: FanduelGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-casino-categories'],
        params: FanduelCasinoCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelCasinoCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-casino-category'],
        params: FanduelCasinoCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelCasinoCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-casino-game'],
        params: FanduelCasinoGameParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelCasinoGameResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-carryover-pools'],
        params: FanduelRacingCarryoverPoolsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingCarryoverPoolsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-filters'],
        params: FanduelRacingFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-horse'],
        params: FanduelRacingHorseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingHorseResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-past-race'],
        params: FanduelRacingPastRaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingPastRaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-past-races'],
        params: FanduelRacingPastRacesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingPastRacesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-past-tracks'],
        params: FanduelRacingPastTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingPastTracksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-race'],
        params: FanduelRacingRaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingRaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-races'],
        params: FanduelRacingRacesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingRacesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-results'],
        params: FanduelRacingResultsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-search'],
        params: FanduelRacingSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-track'],
        params: FanduelRacingTrackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingTrackResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-tracks'],
        params: FanduelRacingTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingTracksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-racing-wager-types'],
        params: FanduelRacingWagerTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingWagerTypesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research'],
        params: FanduelResearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-article'],
        params: FanduelResearchArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-articles'],
        params: FanduelResearchArticlesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchArticlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-author'],
        params: FanduelResearchAuthorParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchAuthorResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-authors'],
        params: FanduelResearchAuthorsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchAuthorsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-featured-articles'],
        params: FanduelResearchFeaturedArticlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchFeaturedArticlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-fixtures'],
        params: FanduelResearchFixturesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchFixturesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-nfl-schedule'],
        params: FanduelResearchNflScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchNflScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-player-news'],
        params: FanduelResearchPlayerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchPlayerNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-quick-picks-daily'],
        params: FanduelResearchQuickPicksDailyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchQuickPicksDailyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-projection-slates'],
        params: FanduelResearchProjectionSlatesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchProjectionSlatesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-projection-tables'],
        params: FanduelResearchProjectionTablesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchProjectionTablesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-projections'],
        params: FanduelResearchProjectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchProjectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-sports'],
        params: FanduelResearchSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchSportsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-research-sub-categories'],
        params: FanduelResearchSubCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchSubCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-autocomplete'],
        params: FanduelSportsbookAutocompleteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookAutocompleteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-builder'],
        params: FanduelSportsbookBuilderParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookBuilderResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-builder-events'],
        params: FanduelSportsbookBuilderEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookBuilderEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-builder-quotes'],
        params: FanduelSportsbookBuilderQuotesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookBuilderQuotesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-competition'],
        params: FanduelSportsbookCompetitionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookCompetitionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-event'],
        params: FanduelSportsbookEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-event-box-score'],
        params: FanduelSportsbookEventBoxScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventBoxScoreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-event-play-by-play'],
        params: FanduelSportsbookEventPlayByPlayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventPlayByPlayResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-event-players'],
        params: FanduelSportsbookEventPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-event-score'],
        params: FanduelSportsbookEventScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventScoreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-event-stats'],
        params: FanduelSportsbookEventStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-events-status'],
        params: FanduelSportsbookEventsStatusParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventsStatusResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-home'],
        params: FanduelSportsbookHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-league'],
        params: FanduelSportsbookLeagueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLeagueResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-live'],
        params: FanduelSportsbookLiveParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-live-count'],
        params: FanduelSportsbookLiveCountParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveCountResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-live-data'],
        params: FanduelSportsbookLiveDataParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveDataResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-live-scores'],
        params: FanduelSportsbookLiveScoresParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveScoresResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-market-prices'],
        params: FanduelSportsbookMarketPricesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookMarketPricesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-parlays'],
        params: FanduelSportsbookParlaysParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookParlaysResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-player'],
        params: FanduelSportsbookPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-player-news'],
        params: FanduelSportsbookPlayerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-player-props'],
        params: FanduelSportsbookPlayerPropsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerPropsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-player-stats'],
        params: FanduelSportsbookPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-players'],
        params: FanduelSportsbookPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-promotions'],
        params: FanduelSportsbookPromotionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPromotionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-schedule'],
        params: FanduelSportsbookScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-search'],
        params: FanduelSportsbookSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-search-tabs'],
        params: FanduelSportsbookSearchTabsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSearchTabsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-sport'],
        params: FanduelSportsbookSportParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSportResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-sports'],
        params: FanduelSportsbookSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSportsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-standings'],
        params: FanduelSportsbookStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-stats'],
        params: FanduelSportsbookStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-team-depth-chart'],
        params: FanduelSportsbookTeamDepthChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamDepthChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-team-news'],
        params: FanduelSportsbookTeamNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-team-odds'],
        params: FanduelSportsbookTeamOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamOddsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-team-roster'],
        params: FanduelSportsbookTeamRosterParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamRosterResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-team-schedule'],
        params: FanduelSportsbookTeamScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-team-stats'],
        params: FanduelSportsbookTeamStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-teams'],
        params: FanduelSportsbookTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fanduel-sportsbook-trending'],
        params: FanduelSportsbookTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-casino-categories'],
        params: FanduelCasinoCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelCasinoCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-casino-category'],
        params: FanduelCasinoCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelCasinoCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-casino-game'],
        params: FanduelCasinoGameParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelCasinoGameResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-carryover-pools'],
        params: FanduelRacingCarryoverPoolsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingCarryoverPoolsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-filters'],
        params: FanduelRacingFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-horse'],
        params: FanduelRacingHorseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingHorseResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-past-race'],
        params: FanduelRacingPastRaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingPastRaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-past-races'],
        params: FanduelRacingPastRacesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingPastRacesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-past-tracks'],
        params: FanduelRacingPastTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingPastTracksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-race'],
        params: FanduelRacingRaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingRaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-races'],
        params: FanduelRacingRacesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingRacesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-results'],
        params: FanduelRacingResultsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-search'],
        params: FanduelRacingSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-track'],
        params: FanduelRacingTrackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingTrackResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-tracks'],
        params: FanduelRacingTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingTracksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-racing-wager-types'],
        params: FanduelRacingWagerTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelRacingWagerTypesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research'],
        params: FanduelResearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-article'],
        params: FanduelResearchArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-articles'],
        params: FanduelResearchArticlesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchArticlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-author'],
        params: FanduelResearchAuthorParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchAuthorResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-authors'],
        params: FanduelResearchAuthorsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchAuthorsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-featured-articles'],
        params: FanduelResearchFeaturedArticlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchFeaturedArticlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-fixtures'],
        params: FanduelResearchFixturesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchFixturesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-nfl-schedule'],
        params: FanduelResearchNflScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchNflScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-player-news'],
        params: FanduelResearchPlayerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchPlayerNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-quick-picks-daily'],
        params: FanduelResearchQuickPicksDailyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchQuickPicksDailyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-projection-slates'],
        params: FanduelResearchProjectionSlatesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchProjectionSlatesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-projection-tables'],
        params: FanduelResearchProjectionTablesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchProjectionTablesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-projections'],
        params: FanduelResearchProjectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchProjectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-sports'],
        params: FanduelResearchSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchSportsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-research-sub-categories'],
        params: FanduelResearchSubCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelResearchSubCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-autocomplete'],
        params: FanduelSportsbookAutocompleteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookAutocompleteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-builder'],
        params: FanduelSportsbookBuilderParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookBuilderResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-builder-events'],
        params: FanduelSportsbookBuilderEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookBuilderEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-builder-quotes'],
        params: FanduelSportsbookBuilderQuotesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookBuilderQuotesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-competition'],
        params: FanduelSportsbookCompetitionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookCompetitionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-event'],
        params: FanduelSportsbookEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-event-box-score'],
        params: FanduelSportsbookEventBoxScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventBoxScoreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-event-play-by-play'],
        params: FanduelSportsbookEventPlayByPlayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventPlayByPlayResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-event-players'],
        params: FanduelSportsbookEventPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-event-score'],
        params: FanduelSportsbookEventScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventScoreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-event-stats'],
        params: FanduelSportsbookEventStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-events-status'],
        params: FanduelSportsbookEventsStatusParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookEventsStatusResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-home'],
        params: FanduelSportsbookHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-league'],
        params: FanduelSportsbookLeagueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLeagueResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-live'],
        params: FanduelSportsbookLiveParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-live-count'],
        params: FanduelSportsbookLiveCountParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveCountResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-live-data'],
        params: FanduelSportsbookLiveDataParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveDataResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-live-scores'],
        params: FanduelSportsbookLiveScoresParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookLiveScoresResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-market-prices'],
        params: FanduelSportsbookMarketPricesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookMarketPricesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-parlays'],
        params: FanduelSportsbookParlaysParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookParlaysResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-player'],
        params: FanduelSportsbookPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-player-news'],
        params: FanduelSportsbookPlayerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-player-props'],
        params: FanduelSportsbookPlayerPropsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerPropsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-player-stats'],
        params: FanduelSportsbookPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-players'],
        params: FanduelSportsbookPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-promotions'],
        params: FanduelSportsbookPromotionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookPromotionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-schedule'],
        params: FanduelSportsbookScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-search'],
        params: FanduelSportsbookSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-search-tabs'],
        params: FanduelSportsbookSearchTabsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSearchTabsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-sport'],
        params: FanduelSportsbookSportParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSportResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-sports'],
        params: FanduelSportsbookSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookSportsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-standings'],
        params: FanduelSportsbookStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-stats'],
        params: FanduelSportsbookStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-team-depth-chart'],
        params: FanduelSportsbookTeamDepthChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamDepthChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-team-news'],
        params: FanduelSportsbookTeamNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-team-odds'],
        params: FanduelSportsbookTeamOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamOddsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-team-roster'],
        params: FanduelSportsbookTeamRosterParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamRosterResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-team-schedule'],
        params: FanduelSportsbookTeamScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-team-stats'],
        params: FanduelSportsbookTeamStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-teams'],
        params: FanduelSportsbookTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTeamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fanduel-sportsbook-trending'],
        params: FanduelSportsbookTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FanduelSportsbookTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class FanDuelClient(CrawloraClient):
    def __enter__(self) -> FanDuelClient: ...
    @overload
    def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesTextResponseParams]) -> str: ...
    @overload
    def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesDefaultParams]) -> FanduelCasinoCategoriesResponse: ...
    @overload
    def casino_category(self, **params: Unpack[FanduelCasinoCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def casino_category(self, **params: Unpack[FanduelCasinoCategoryTextResponseParams]) -> str: ...
    @overload
    def casino_category(self, **params: Unpack[FanduelCasinoCategoryDefaultParams]) -> FanduelCasinoCategoryResponse: ...
    @overload
    def casino_game(self, **params: Unpack[FanduelCasinoGameStreamParams]) -> BinaryIO: ...
    @overload
    def casino_game(self, **params: Unpack[FanduelCasinoGameTextResponseParams]) -> str: ...
    @overload
    def casino_game(self, **params: Unpack[FanduelCasinoGameDefaultParams]) -> FanduelCasinoGameResponse: ...
    @overload
    def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsStreamParams]) -> BinaryIO: ...
    @overload
    def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsTextResponseParams]) -> str: ...
    @overload
    def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsDefaultParams]) -> FanduelRacingCarryoverPoolsResponse: ...
    @overload
    def racing_filters(self, **params: Unpack[FanduelRacingFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def racing_filters(self, **params: Unpack[FanduelRacingFiltersTextResponseParams]) -> str: ...
    @overload
    def racing_filters(self, **params: Unpack[FanduelRacingFiltersDefaultParams]) -> FanduelRacingFiltersResponse: ...
    @overload
    def racing_horse(self, **params: Unpack[FanduelRacingHorseStreamParams]) -> BinaryIO: ...
    @overload
    def racing_horse(self, **params: Unpack[FanduelRacingHorseTextResponseParams]) -> str: ...
    @overload
    def racing_horse(self, **params: Unpack[FanduelRacingHorseDefaultParams]) -> FanduelRacingHorseResponse: ...
    @overload
    def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceStreamParams]) -> BinaryIO: ...
    @overload
    def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceTextResponseParams]) -> str: ...
    @overload
    def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceDefaultParams]) -> FanduelRacingPastRaceResponse: ...
    @overload
    def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesStreamParams]) -> BinaryIO: ...
    @overload
    def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesTextResponseParams]) -> str: ...
    @overload
    def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesDefaultParams]) -> FanduelRacingPastRacesResponse: ...
    @overload
    def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksStreamParams]) -> BinaryIO: ...
    @overload
    def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksTextResponseParams]) -> str: ...
    @overload
    def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksDefaultParams]) -> FanduelRacingPastTracksResponse: ...
    @overload
    def racing_race(self, **params: Unpack[FanduelRacingRaceStreamParams]) -> BinaryIO: ...
    @overload
    def racing_race(self, **params: Unpack[FanduelRacingRaceTextResponseParams]) -> str: ...
    @overload
    def racing_race(self, **params: Unpack[FanduelRacingRaceDefaultParams]) -> FanduelRacingRaceResponse: ...
    @overload
    def racing_races(self, **params: Unpack[FanduelRacingRacesStreamParams]) -> BinaryIO: ...
    @overload
    def racing_races(self, **params: Unpack[FanduelRacingRacesTextResponseParams]) -> str: ...
    @overload
    def racing_races(self, **params: Unpack[FanduelRacingRacesDefaultParams]) -> FanduelRacingRacesResponse: ...
    @overload
    def racing_results(self, **params: Unpack[FanduelRacingResultsStreamParams]) -> BinaryIO: ...
    @overload
    def racing_results(self, **params: Unpack[FanduelRacingResultsTextResponseParams]) -> str: ...
    @overload
    def racing_results(self, **params: Unpack[FanduelRacingResultsDefaultParams]) -> FanduelRacingResultsResponse: ...
    @overload
    def racing_search(self, **params: Unpack[FanduelRacingSearchStreamParams]) -> BinaryIO: ...
    @overload
    def racing_search(self, **params: Unpack[FanduelRacingSearchTextResponseParams]) -> str: ...
    @overload
    def racing_search(self, **params: Unpack[FanduelRacingSearchDefaultParams]) -> FanduelRacingSearchResponse: ...
    @overload
    def racing_track(self, **params: Unpack[FanduelRacingTrackStreamParams]) -> BinaryIO: ...
    @overload
    def racing_track(self, **params: Unpack[FanduelRacingTrackTextResponseParams]) -> str: ...
    @overload
    def racing_track(self, **params: Unpack[FanduelRacingTrackDefaultParams]) -> FanduelRacingTrackResponse: ...
    @overload
    def racing_tracks(self, **params: Unpack[FanduelRacingTracksStreamParams]) -> BinaryIO: ...
    @overload
    def racing_tracks(self, **params: Unpack[FanduelRacingTracksTextResponseParams]) -> str: ...
    @overload
    def racing_tracks(self, **params: Unpack[FanduelRacingTracksDefaultParams]) -> FanduelRacingTracksResponse: ...
    @overload
    def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesStreamParams]) -> BinaryIO: ...
    @overload
    def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesTextResponseParams]) -> str: ...
    @overload
    def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesDefaultParams]) -> FanduelRacingWagerTypesResponse: ...
    @overload
    def research(self, **params: Unpack[FanduelResearchStreamParams]) -> BinaryIO: ...
    @overload
    def research(self, **params: Unpack[FanduelResearchTextResponseParams]) -> str: ...
    @overload
    def research(self, **params: Unpack[FanduelResearchDefaultParams]) -> FanduelResearchResponse: ...
    @overload
    def research_article(self, **params: Unpack[FanduelResearchArticleStreamParams]) -> BinaryIO: ...
    @overload
    def research_article(self, **params: Unpack[FanduelResearchArticleTextResponseParams]) -> str: ...
    @overload
    def research_article(self, **params: Unpack[FanduelResearchArticleDefaultParams]) -> FanduelResearchArticleResponse: ...
    @overload
    def research_articles(self, **params: Unpack[FanduelResearchArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def research_articles(self, **params: Unpack[FanduelResearchArticlesTextResponseParams]) -> str: ...
    @overload
    def research_articles(self, **params: Unpack[FanduelResearchArticlesDefaultParams]) -> FanduelResearchArticlesResponse: ...
    @overload
    def research_author(self, **params: Unpack[FanduelResearchAuthorStreamParams]) -> BinaryIO: ...
    @overload
    def research_author(self, **params: Unpack[FanduelResearchAuthorTextResponseParams]) -> str: ...
    @overload
    def research_author(self, **params: Unpack[FanduelResearchAuthorDefaultParams]) -> FanduelResearchAuthorResponse: ...
    @overload
    def research_authors(self, **params: Unpack[FanduelResearchAuthorsStreamParams]) -> BinaryIO: ...
    @overload
    def research_authors(self, **params: Unpack[FanduelResearchAuthorsTextResponseParams]) -> str: ...
    @overload
    def research_authors(self, **params: Unpack[FanduelResearchAuthorsDefaultParams]) -> FanduelResearchAuthorsResponse: ...
    @overload
    def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesTextResponseParams]) -> str: ...
    @overload
    def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesDefaultParams]) -> FanduelResearchFeaturedArticlesResponse: ...
    @overload
    def research_fixtures(self, **params: Unpack[FanduelResearchFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def research_fixtures(self, **params: Unpack[FanduelResearchFixturesTextResponseParams]) -> str: ...
    @overload
    def research_fixtures(self, **params: Unpack[FanduelResearchFixturesDefaultParams]) -> FanduelResearchFixturesResponse: ...
    @overload
    def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleTextResponseParams]) -> str: ...
    @overload
    def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleDefaultParams]) -> FanduelResearchNflScheduleResponse: ...
    @overload
    def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsTextResponseParams]) -> str: ...
    @overload
    def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsDefaultParams]) -> FanduelResearchPlayerNewsResponse: ...
    @overload
    def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyStreamParams]) -> BinaryIO: ...
    @overload
    def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyTextResponseParams]) -> str: ...
    @overload
    def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyDefaultParams]) -> FanduelResearchQuickPicksDailyResponse: ...
    @overload
    def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesStreamParams]) -> BinaryIO: ...
    @overload
    def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesTextResponseParams]) -> str: ...
    @overload
    def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesDefaultParams]) -> FanduelResearchProjectionSlatesResponse: ...
    @overload
    def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesStreamParams]) -> BinaryIO: ...
    @overload
    def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesTextResponseParams]) -> str: ...
    @overload
    def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesDefaultParams]) -> FanduelResearchProjectionTablesResponse: ...
    @overload
    def research_projections(self, **params: Unpack[FanduelResearchProjectionsStreamParams]) -> BinaryIO: ...
    @overload
    def research_projections(self, **params: Unpack[FanduelResearchProjectionsTextResponseParams]) -> str: ...
    @overload
    def research_projections(self, **params: Unpack[FanduelResearchProjectionsDefaultParams]) -> FanduelResearchProjectionsResponse: ...
    @overload
    def research_sports(self, **params: Unpack[FanduelResearchSportsStreamParams]) -> BinaryIO: ...
    @overload
    def research_sports(self, **params: Unpack[FanduelResearchSportsTextResponseParams]) -> str: ...
    @overload
    def research_sports(self, **params: Unpack[FanduelResearchSportsDefaultParams]) -> FanduelResearchSportsResponse: ...
    @overload
    def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesTextResponseParams]) -> str: ...
    @overload
    def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesDefaultParams]) -> FanduelResearchSubCategoriesResponse: ...
    @overload
    def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteTextResponseParams]) -> str: ...
    @overload
    def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteDefaultParams]) -> FanduelSportsbookAutocompleteResponse: ...
    @overload
    def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderTextResponseParams]) -> str: ...
    @overload
    def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderDefaultParams]) -> FanduelSportsbookBuilderResponse: ...
    @overload
    def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsDefaultParams]) -> FanduelSportsbookBuilderEventsResponse: ...
    @overload
    def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesTextResponseParams]) -> str: ...
    @overload
    def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesDefaultParams]) -> FanduelSportsbookBuilderQuotesResponse: ...
    @overload
    def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionTextResponseParams]) -> str: ...
    @overload
    def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionDefaultParams]) -> FanduelSportsbookCompetitionResponse: ...
    @overload
    def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventDefaultParams]) -> FanduelSportsbookEventResponse: ...
    @overload
    def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreDefaultParams]) -> FanduelSportsbookEventBoxScoreResponse: ...
    @overload
    def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayDefaultParams]) -> FanduelSportsbookEventPlayByPlayResponse: ...
    @overload
    def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersDefaultParams]) -> FanduelSportsbookEventPlayersResponse: ...
    @overload
    def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreDefaultParams]) -> FanduelSportsbookEventScoreResponse: ...
    @overload
    def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsDefaultParams]) -> FanduelSportsbookEventStatsResponse: ...
    @overload
    def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusTextResponseParams]) -> str: ...
    @overload
    def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusDefaultParams]) -> FanduelSportsbookEventsStatusResponse: ...
    @overload
    def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeTextResponseParams]) -> str: ...
    @overload
    def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeDefaultParams]) -> FanduelSportsbookHomeResponse: ...
    @overload
    def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueTextResponseParams]) -> str: ...
    @overload
    def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueDefaultParams]) -> FanduelSportsbookLeagueResponse: ...
    @overload
    def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveDefaultParams]) -> FanduelSportsbookLiveResponse: ...
    @overload
    def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountDefaultParams]) -> FanduelSportsbookLiveCountResponse: ...
    @overload
    def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataDefaultParams]) -> FanduelSportsbookLiveDataResponse: ...
    @overload
    def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresTextResponseParams]) -> str: ...
    @overload
    def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresDefaultParams]) -> FanduelSportsbookLiveScoresResponse: ...
    @overload
    def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesTextResponseParams]) -> str: ...
    @overload
    def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesDefaultParams]) -> FanduelSportsbookMarketPricesResponse: ...
    @overload
    def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysTextResponseParams]) -> str: ...
    @overload
    def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysDefaultParams]) -> FanduelSportsbookParlaysResponse: ...
    @overload
    def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerDefaultParams]) -> FanduelSportsbookPlayerResponse: ...
    @overload
    def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsDefaultParams]) -> FanduelSportsbookPlayerNewsResponse: ...
    @overload
    def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsDefaultParams]) -> FanduelSportsbookPlayerPropsResponse: ...
    @overload
    def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsDefaultParams]) -> FanduelSportsbookPlayerStatsResponse: ...
    @overload
    def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersTextResponseParams]) -> str: ...
    @overload
    def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersDefaultParams]) -> FanduelSportsbookPlayersResponse: ...
    @overload
    def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsDefaultParams]) -> FanduelSportsbookPromotionsResponse: ...
    @overload
    def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleTextResponseParams]) -> str: ...
    @overload
    def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleDefaultParams]) -> FanduelSportsbookScheduleResponse: ...
    @overload
    def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchTextResponseParams]) -> str: ...
    @overload
    def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchDefaultParams]) -> FanduelSportsbookSearchResponse: ...
    @overload
    def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsDefaultParams]) -> FanduelSportsbookSearchTabsResponse: ...
    @overload
    def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportTextResponseParams]) -> str: ...
    @overload
    def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportDefaultParams]) -> FanduelSportsbookSportResponse: ...
    @overload
    def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsDefaultParams]) -> FanduelSportsbookSportsResponse: ...
    @overload
    def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsDefaultParams]) -> FanduelSportsbookStandingsResponse: ...
    @overload
    def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsDefaultParams]) -> FanduelSportsbookStatsResponse: ...
    @overload
    def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartDefaultParams]) -> FanduelSportsbookTeamDepthChartResponse: ...
    @overload
    def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsDefaultParams]) -> FanduelSportsbookTeamNewsResponse: ...
    @overload
    def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsDefaultParams]) -> FanduelSportsbookTeamOddsResponse: ...
    @overload
    def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterDefaultParams]) -> FanduelSportsbookTeamRosterResponse: ...
    @overload
    def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleDefaultParams]) -> FanduelSportsbookTeamScheduleResponse: ...
    @overload
    def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsDefaultParams]) -> FanduelSportsbookTeamStatsResponse: ...
    @overload
    def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsTextResponseParams]) -> str: ...
    @overload
    def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsDefaultParams]) -> FanduelSportsbookTeamsResponse: ...
    @overload
    def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingTextResponseParams]) -> str: ...
    @overload
    def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingDefaultParams]) -> FanduelSportsbookTrendingResponse: ...

class AsyncFanDuelClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFanDuelClient: ...
    fanduel: _AsyncFanduelGroup
    @overload
    async def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesTextResponseParams]) -> str: ...
    @overload
    async def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesDefaultParams]) -> FanduelCasinoCategoriesResponse: ...
    @overload
    async def casino_category(self, **params: Unpack[FanduelCasinoCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def casino_category(self, **params: Unpack[FanduelCasinoCategoryTextResponseParams]) -> str: ...
    @overload
    async def casino_category(self, **params: Unpack[FanduelCasinoCategoryDefaultParams]) -> FanduelCasinoCategoryResponse: ...
    @overload
    async def casino_game(self, **params: Unpack[FanduelCasinoGameStreamParams]) -> BinaryIO: ...
    @overload
    async def casino_game(self, **params: Unpack[FanduelCasinoGameTextResponseParams]) -> str: ...
    @overload
    async def casino_game(self, **params: Unpack[FanduelCasinoGameDefaultParams]) -> FanduelCasinoGameResponse: ...
    @overload
    async def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsTextResponseParams]) -> str: ...
    @overload
    async def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsDefaultParams]) -> FanduelRacingCarryoverPoolsResponse: ...
    @overload
    async def racing_filters(self, **params: Unpack[FanduelRacingFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_filters(self, **params: Unpack[FanduelRacingFiltersTextResponseParams]) -> str: ...
    @overload
    async def racing_filters(self, **params: Unpack[FanduelRacingFiltersDefaultParams]) -> FanduelRacingFiltersResponse: ...
    @overload
    async def racing_horse(self, **params: Unpack[FanduelRacingHorseStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_horse(self, **params: Unpack[FanduelRacingHorseTextResponseParams]) -> str: ...
    @overload
    async def racing_horse(self, **params: Unpack[FanduelRacingHorseDefaultParams]) -> FanduelRacingHorseResponse: ...
    @overload
    async def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceTextResponseParams]) -> str: ...
    @overload
    async def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceDefaultParams]) -> FanduelRacingPastRaceResponse: ...
    @overload
    async def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesTextResponseParams]) -> str: ...
    @overload
    async def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesDefaultParams]) -> FanduelRacingPastRacesResponse: ...
    @overload
    async def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksTextResponseParams]) -> str: ...
    @overload
    async def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksDefaultParams]) -> FanduelRacingPastTracksResponse: ...
    @overload
    async def racing_race(self, **params: Unpack[FanduelRacingRaceStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_race(self, **params: Unpack[FanduelRacingRaceTextResponseParams]) -> str: ...
    @overload
    async def racing_race(self, **params: Unpack[FanduelRacingRaceDefaultParams]) -> FanduelRacingRaceResponse: ...
    @overload
    async def racing_races(self, **params: Unpack[FanduelRacingRacesStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_races(self, **params: Unpack[FanduelRacingRacesTextResponseParams]) -> str: ...
    @overload
    async def racing_races(self, **params: Unpack[FanduelRacingRacesDefaultParams]) -> FanduelRacingRacesResponse: ...
    @overload
    async def racing_results(self, **params: Unpack[FanduelRacingResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_results(self, **params: Unpack[FanduelRacingResultsTextResponseParams]) -> str: ...
    @overload
    async def racing_results(self, **params: Unpack[FanduelRacingResultsDefaultParams]) -> FanduelRacingResultsResponse: ...
    @overload
    async def racing_search(self, **params: Unpack[FanduelRacingSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_search(self, **params: Unpack[FanduelRacingSearchTextResponseParams]) -> str: ...
    @overload
    async def racing_search(self, **params: Unpack[FanduelRacingSearchDefaultParams]) -> FanduelRacingSearchResponse: ...
    @overload
    async def racing_track(self, **params: Unpack[FanduelRacingTrackStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_track(self, **params: Unpack[FanduelRacingTrackTextResponseParams]) -> str: ...
    @overload
    async def racing_track(self, **params: Unpack[FanduelRacingTrackDefaultParams]) -> FanduelRacingTrackResponse: ...
    @overload
    async def racing_tracks(self, **params: Unpack[FanduelRacingTracksStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_tracks(self, **params: Unpack[FanduelRacingTracksTextResponseParams]) -> str: ...
    @overload
    async def racing_tracks(self, **params: Unpack[FanduelRacingTracksDefaultParams]) -> FanduelRacingTracksResponse: ...
    @overload
    async def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesTextResponseParams]) -> str: ...
    @overload
    async def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesDefaultParams]) -> FanduelRacingWagerTypesResponse: ...
    @overload
    async def research(self, **params: Unpack[FanduelResearchStreamParams]) -> BinaryIO: ...
    @overload
    async def research(self, **params: Unpack[FanduelResearchTextResponseParams]) -> str: ...
    @overload
    async def research(self, **params: Unpack[FanduelResearchDefaultParams]) -> FanduelResearchResponse: ...
    @overload
    async def research_article(self, **params: Unpack[FanduelResearchArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def research_article(self, **params: Unpack[FanduelResearchArticleTextResponseParams]) -> str: ...
    @overload
    async def research_article(self, **params: Unpack[FanduelResearchArticleDefaultParams]) -> FanduelResearchArticleResponse: ...
    @overload
    async def research_articles(self, **params: Unpack[FanduelResearchArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_articles(self, **params: Unpack[FanduelResearchArticlesTextResponseParams]) -> str: ...
    @overload
    async def research_articles(self, **params: Unpack[FanduelResearchArticlesDefaultParams]) -> FanduelResearchArticlesResponse: ...
    @overload
    async def research_author(self, **params: Unpack[FanduelResearchAuthorStreamParams]) -> BinaryIO: ...
    @overload
    async def research_author(self, **params: Unpack[FanduelResearchAuthorTextResponseParams]) -> str: ...
    @overload
    async def research_author(self, **params: Unpack[FanduelResearchAuthorDefaultParams]) -> FanduelResearchAuthorResponse: ...
    @overload
    async def research_authors(self, **params: Unpack[FanduelResearchAuthorsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_authors(self, **params: Unpack[FanduelResearchAuthorsTextResponseParams]) -> str: ...
    @overload
    async def research_authors(self, **params: Unpack[FanduelResearchAuthorsDefaultParams]) -> FanduelResearchAuthorsResponse: ...
    @overload
    async def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesTextResponseParams]) -> str: ...
    @overload
    async def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesDefaultParams]) -> FanduelResearchFeaturedArticlesResponse: ...
    @overload
    async def research_fixtures(self, **params: Unpack[FanduelResearchFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_fixtures(self, **params: Unpack[FanduelResearchFixturesTextResponseParams]) -> str: ...
    @overload
    async def research_fixtures(self, **params: Unpack[FanduelResearchFixturesDefaultParams]) -> FanduelResearchFixturesResponse: ...
    @overload
    async def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleTextResponseParams]) -> str: ...
    @overload
    async def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleDefaultParams]) -> FanduelResearchNflScheduleResponse: ...
    @overload
    async def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsTextResponseParams]) -> str: ...
    @overload
    async def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsDefaultParams]) -> FanduelResearchPlayerNewsResponse: ...
    @overload
    async def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyStreamParams]) -> BinaryIO: ...
    @overload
    async def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyTextResponseParams]) -> str: ...
    @overload
    async def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyDefaultParams]) -> FanduelResearchQuickPicksDailyResponse: ...
    @overload
    async def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesTextResponseParams]) -> str: ...
    @overload
    async def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesDefaultParams]) -> FanduelResearchProjectionSlatesResponse: ...
    @overload
    async def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesTextResponseParams]) -> str: ...
    @overload
    async def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesDefaultParams]) -> FanduelResearchProjectionTablesResponse: ...
    @overload
    async def research_projections(self, **params: Unpack[FanduelResearchProjectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_projections(self, **params: Unpack[FanduelResearchProjectionsTextResponseParams]) -> str: ...
    @overload
    async def research_projections(self, **params: Unpack[FanduelResearchProjectionsDefaultParams]) -> FanduelResearchProjectionsResponse: ...
    @overload
    async def research_sports(self, **params: Unpack[FanduelResearchSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_sports(self, **params: Unpack[FanduelResearchSportsTextResponseParams]) -> str: ...
    @overload
    async def research_sports(self, **params: Unpack[FanduelResearchSportsDefaultParams]) -> FanduelResearchSportsResponse: ...
    @overload
    async def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesTextResponseParams]) -> str: ...
    @overload
    async def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesDefaultParams]) -> FanduelResearchSubCategoriesResponse: ...
    @overload
    async def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteDefaultParams]) -> FanduelSportsbookAutocompleteResponse: ...
    @overload
    async def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderDefaultParams]) -> FanduelSportsbookBuilderResponse: ...
    @overload
    async def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsDefaultParams]) -> FanduelSportsbookBuilderEventsResponse: ...
    @overload
    async def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesDefaultParams]) -> FanduelSportsbookBuilderQuotesResponse: ...
    @overload
    async def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionDefaultParams]) -> FanduelSportsbookCompetitionResponse: ...
    @overload
    async def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventDefaultParams]) -> FanduelSportsbookEventResponse: ...
    @overload
    async def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreDefaultParams]) -> FanduelSportsbookEventBoxScoreResponse: ...
    @overload
    async def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayDefaultParams]) -> FanduelSportsbookEventPlayByPlayResponse: ...
    @overload
    async def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersDefaultParams]) -> FanduelSportsbookEventPlayersResponse: ...
    @overload
    async def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreDefaultParams]) -> FanduelSportsbookEventScoreResponse: ...
    @overload
    async def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsDefaultParams]) -> FanduelSportsbookEventStatsResponse: ...
    @overload
    async def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusDefaultParams]) -> FanduelSportsbookEventsStatusResponse: ...
    @overload
    async def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeDefaultParams]) -> FanduelSportsbookHomeResponse: ...
    @overload
    async def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueDefaultParams]) -> FanduelSportsbookLeagueResponse: ...
    @overload
    async def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveDefaultParams]) -> FanduelSportsbookLiveResponse: ...
    @overload
    async def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountDefaultParams]) -> FanduelSportsbookLiveCountResponse: ...
    @overload
    async def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataDefaultParams]) -> FanduelSportsbookLiveDataResponse: ...
    @overload
    async def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresDefaultParams]) -> FanduelSportsbookLiveScoresResponse: ...
    @overload
    async def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesDefaultParams]) -> FanduelSportsbookMarketPricesResponse: ...
    @overload
    async def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysDefaultParams]) -> FanduelSportsbookParlaysResponse: ...
    @overload
    async def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerDefaultParams]) -> FanduelSportsbookPlayerResponse: ...
    @overload
    async def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsDefaultParams]) -> FanduelSportsbookPlayerNewsResponse: ...
    @overload
    async def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsDefaultParams]) -> FanduelSportsbookPlayerPropsResponse: ...
    @overload
    async def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsDefaultParams]) -> FanduelSportsbookPlayerStatsResponse: ...
    @overload
    async def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersDefaultParams]) -> FanduelSportsbookPlayersResponse: ...
    @overload
    async def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsDefaultParams]) -> FanduelSportsbookPromotionsResponse: ...
    @overload
    async def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleDefaultParams]) -> FanduelSportsbookScheduleResponse: ...
    @overload
    async def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchDefaultParams]) -> FanduelSportsbookSearchResponse: ...
    @overload
    async def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsDefaultParams]) -> FanduelSportsbookSearchTabsResponse: ...
    @overload
    async def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportDefaultParams]) -> FanduelSportsbookSportResponse: ...
    @overload
    async def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsDefaultParams]) -> FanduelSportsbookSportsResponse: ...
    @overload
    async def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsDefaultParams]) -> FanduelSportsbookStandingsResponse: ...
    @overload
    async def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsDefaultParams]) -> FanduelSportsbookStatsResponse: ...
    @overload
    async def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartDefaultParams]) -> FanduelSportsbookTeamDepthChartResponse: ...
    @overload
    async def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsDefaultParams]) -> FanduelSportsbookTeamNewsResponse: ...
    @overload
    async def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsDefaultParams]) -> FanduelSportsbookTeamOddsResponse: ...
    @overload
    async def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterDefaultParams]) -> FanduelSportsbookTeamRosterResponse: ...
    @overload
    async def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleDefaultParams]) -> FanduelSportsbookTeamScheduleResponse: ...
    @overload
    async def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsDefaultParams]) -> FanduelSportsbookTeamStatsResponse: ...
    @overload
    async def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsDefaultParams]) -> FanduelSportsbookTeamsResponse: ...
    @overload
    async def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingDefaultParams]) -> FanduelSportsbookTrendingResponse: ...

class _AsyncFanduelGroup:
    @overload
    async def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesTextResponseParams]) -> str: ...
    @overload
    async def casino_categories(self, **params: Unpack[FanduelCasinoCategoriesDefaultParams]) -> FanduelCasinoCategoriesResponse: ...
    @overload
    async def casino_category(self, **params: Unpack[FanduelCasinoCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def casino_category(self, **params: Unpack[FanduelCasinoCategoryTextResponseParams]) -> str: ...
    @overload
    async def casino_category(self, **params: Unpack[FanduelCasinoCategoryDefaultParams]) -> FanduelCasinoCategoryResponse: ...
    @overload
    async def casino_game(self, **params: Unpack[FanduelCasinoGameStreamParams]) -> BinaryIO: ...
    @overload
    async def casino_game(self, **params: Unpack[FanduelCasinoGameTextResponseParams]) -> str: ...
    @overload
    async def casino_game(self, **params: Unpack[FanduelCasinoGameDefaultParams]) -> FanduelCasinoGameResponse: ...
    @overload
    async def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsTextResponseParams]) -> str: ...
    @overload
    async def racing_carryover_pools(self, **params: Unpack[FanduelRacingCarryoverPoolsDefaultParams]) -> FanduelRacingCarryoverPoolsResponse: ...
    @overload
    async def racing_filters(self, **params: Unpack[FanduelRacingFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_filters(self, **params: Unpack[FanduelRacingFiltersTextResponseParams]) -> str: ...
    @overload
    async def racing_filters(self, **params: Unpack[FanduelRacingFiltersDefaultParams]) -> FanduelRacingFiltersResponse: ...
    @overload
    async def racing_horse(self, **params: Unpack[FanduelRacingHorseStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_horse(self, **params: Unpack[FanduelRacingHorseTextResponseParams]) -> str: ...
    @overload
    async def racing_horse(self, **params: Unpack[FanduelRacingHorseDefaultParams]) -> FanduelRacingHorseResponse: ...
    @overload
    async def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceTextResponseParams]) -> str: ...
    @overload
    async def racing_past_race(self, **params: Unpack[FanduelRacingPastRaceDefaultParams]) -> FanduelRacingPastRaceResponse: ...
    @overload
    async def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesTextResponseParams]) -> str: ...
    @overload
    async def racing_past_races(self, **params: Unpack[FanduelRacingPastRacesDefaultParams]) -> FanduelRacingPastRacesResponse: ...
    @overload
    async def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksTextResponseParams]) -> str: ...
    @overload
    async def racing_past_tracks(self, **params: Unpack[FanduelRacingPastTracksDefaultParams]) -> FanduelRacingPastTracksResponse: ...
    @overload
    async def racing_race(self, **params: Unpack[FanduelRacingRaceStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_race(self, **params: Unpack[FanduelRacingRaceTextResponseParams]) -> str: ...
    @overload
    async def racing_race(self, **params: Unpack[FanduelRacingRaceDefaultParams]) -> FanduelRacingRaceResponse: ...
    @overload
    async def racing_races(self, **params: Unpack[FanduelRacingRacesStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_races(self, **params: Unpack[FanduelRacingRacesTextResponseParams]) -> str: ...
    @overload
    async def racing_races(self, **params: Unpack[FanduelRacingRacesDefaultParams]) -> FanduelRacingRacesResponse: ...
    @overload
    async def racing_results(self, **params: Unpack[FanduelRacingResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_results(self, **params: Unpack[FanduelRacingResultsTextResponseParams]) -> str: ...
    @overload
    async def racing_results(self, **params: Unpack[FanduelRacingResultsDefaultParams]) -> FanduelRacingResultsResponse: ...
    @overload
    async def racing_search(self, **params: Unpack[FanduelRacingSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_search(self, **params: Unpack[FanduelRacingSearchTextResponseParams]) -> str: ...
    @overload
    async def racing_search(self, **params: Unpack[FanduelRacingSearchDefaultParams]) -> FanduelRacingSearchResponse: ...
    @overload
    async def racing_track(self, **params: Unpack[FanduelRacingTrackStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_track(self, **params: Unpack[FanduelRacingTrackTextResponseParams]) -> str: ...
    @overload
    async def racing_track(self, **params: Unpack[FanduelRacingTrackDefaultParams]) -> FanduelRacingTrackResponse: ...
    @overload
    async def racing_tracks(self, **params: Unpack[FanduelRacingTracksStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_tracks(self, **params: Unpack[FanduelRacingTracksTextResponseParams]) -> str: ...
    @overload
    async def racing_tracks(self, **params: Unpack[FanduelRacingTracksDefaultParams]) -> FanduelRacingTracksResponse: ...
    @overload
    async def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesTextResponseParams]) -> str: ...
    @overload
    async def racing_wager_types(self, **params: Unpack[FanduelRacingWagerTypesDefaultParams]) -> FanduelRacingWagerTypesResponse: ...
    @overload
    async def research(self, **params: Unpack[FanduelResearchStreamParams]) -> BinaryIO: ...
    @overload
    async def research(self, **params: Unpack[FanduelResearchTextResponseParams]) -> str: ...
    @overload
    async def research(self, **params: Unpack[FanduelResearchDefaultParams]) -> FanduelResearchResponse: ...
    @overload
    async def research_article(self, **params: Unpack[FanduelResearchArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def research_article(self, **params: Unpack[FanduelResearchArticleTextResponseParams]) -> str: ...
    @overload
    async def research_article(self, **params: Unpack[FanduelResearchArticleDefaultParams]) -> FanduelResearchArticleResponse: ...
    @overload
    async def research_articles(self, **params: Unpack[FanduelResearchArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_articles(self, **params: Unpack[FanduelResearchArticlesTextResponseParams]) -> str: ...
    @overload
    async def research_articles(self, **params: Unpack[FanduelResearchArticlesDefaultParams]) -> FanduelResearchArticlesResponse: ...
    @overload
    async def research_author(self, **params: Unpack[FanduelResearchAuthorStreamParams]) -> BinaryIO: ...
    @overload
    async def research_author(self, **params: Unpack[FanduelResearchAuthorTextResponseParams]) -> str: ...
    @overload
    async def research_author(self, **params: Unpack[FanduelResearchAuthorDefaultParams]) -> FanduelResearchAuthorResponse: ...
    @overload
    async def research_authors(self, **params: Unpack[FanduelResearchAuthorsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_authors(self, **params: Unpack[FanduelResearchAuthorsTextResponseParams]) -> str: ...
    @overload
    async def research_authors(self, **params: Unpack[FanduelResearchAuthorsDefaultParams]) -> FanduelResearchAuthorsResponse: ...
    @overload
    async def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesTextResponseParams]) -> str: ...
    @overload
    async def research_featured_articles(self, **params: Unpack[FanduelResearchFeaturedArticlesDefaultParams]) -> FanduelResearchFeaturedArticlesResponse: ...
    @overload
    async def research_fixtures(self, **params: Unpack[FanduelResearchFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_fixtures(self, **params: Unpack[FanduelResearchFixturesTextResponseParams]) -> str: ...
    @overload
    async def research_fixtures(self, **params: Unpack[FanduelResearchFixturesDefaultParams]) -> FanduelResearchFixturesResponse: ...
    @overload
    async def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleTextResponseParams]) -> str: ...
    @overload
    async def research_nfl_schedule(self, **params: Unpack[FanduelResearchNflScheduleDefaultParams]) -> FanduelResearchNflScheduleResponse: ...
    @overload
    async def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsTextResponseParams]) -> str: ...
    @overload
    async def research_player_news(self, **params: Unpack[FanduelResearchPlayerNewsDefaultParams]) -> FanduelResearchPlayerNewsResponse: ...
    @overload
    async def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyStreamParams]) -> BinaryIO: ...
    @overload
    async def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyTextResponseParams]) -> str: ...
    @overload
    async def research_quick_picks_daily(self, **params: Unpack[FanduelResearchQuickPicksDailyDefaultParams]) -> FanduelResearchQuickPicksDailyResponse: ...
    @overload
    async def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesTextResponseParams]) -> str: ...
    @overload
    async def research_projection_slates(self, **params: Unpack[FanduelResearchProjectionSlatesDefaultParams]) -> FanduelResearchProjectionSlatesResponse: ...
    @overload
    async def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesTextResponseParams]) -> str: ...
    @overload
    async def research_projection_tables(self, **params: Unpack[FanduelResearchProjectionTablesDefaultParams]) -> FanduelResearchProjectionTablesResponse: ...
    @overload
    async def research_projections(self, **params: Unpack[FanduelResearchProjectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_projections(self, **params: Unpack[FanduelResearchProjectionsTextResponseParams]) -> str: ...
    @overload
    async def research_projections(self, **params: Unpack[FanduelResearchProjectionsDefaultParams]) -> FanduelResearchProjectionsResponse: ...
    @overload
    async def research_sports(self, **params: Unpack[FanduelResearchSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def research_sports(self, **params: Unpack[FanduelResearchSportsTextResponseParams]) -> str: ...
    @overload
    async def research_sports(self, **params: Unpack[FanduelResearchSportsDefaultParams]) -> FanduelResearchSportsResponse: ...
    @overload
    async def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesTextResponseParams]) -> str: ...
    @overload
    async def research_sub_categories(self, **params: Unpack[FanduelResearchSubCategoriesDefaultParams]) -> FanduelResearchSubCategoriesResponse: ...
    @overload
    async def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_autocomplete(self, **params: Unpack[FanduelSportsbookAutocompleteDefaultParams]) -> FanduelSportsbookAutocompleteResponse: ...
    @overload
    async def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_builder(self, **params: Unpack[FanduelSportsbookBuilderDefaultParams]) -> FanduelSportsbookBuilderResponse: ...
    @overload
    async def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_builder_events(self, **params: Unpack[FanduelSportsbookBuilderEventsDefaultParams]) -> FanduelSportsbookBuilderEventsResponse: ...
    @overload
    async def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_builder_quotes(self, **params: Unpack[FanduelSportsbookBuilderQuotesDefaultParams]) -> FanduelSportsbookBuilderQuotesResponse: ...
    @overload
    async def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_competition(self, **params: Unpack[FanduelSportsbookCompetitionDefaultParams]) -> FanduelSportsbookCompetitionResponse: ...
    @overload
    async def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event(self, **params: Unpack[FanduelSportsbookEventDefaultParams]) -> FanduelSportsbookEventResponse: ...
    @overload
    async def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_box_score(self, **params: Unpack[FanduelSportsbookEventBoxScoreDefaultParams]) -> FanduelSportsbookEventBoxScoreResponse: ...
    @overload
    async def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_play_by_play(self, **params: Unpack[FanduelSportsbookEventPlayByPlayDefaultParams]) -> FanduelSportsbookEventPlayByPlayResponse: ...
    @overload
    async def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_players(self, **params: Unpack[FanduelSportsbookEventPlayersDefaultParams]) -> FanduelSportsbookEventPlayersResponse: ...
    @overload
    async def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_score(self, **params: Unpack[FanduelSportsbookEventScoreDefaultParams]) -> FanduelSportsbookEventScoreResponse: ...
    @overload
    async def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_event_stats(self, **params: Unpack[FanduelSportsbookEventStatsDefaultParams]) -> FanduelSportsbookEventStatsResponse: ...
    @overload
    async def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_events_status(self, **params: Unpack[FanduelSportsbookEventsStatusDefaultParams]) -> FanduelSportsbookEventsStatusResponse: ...
    @overload
    async def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_home(self, **params: Unpack[FanduelSportsbookHomeDefaultParams]) -> FanduelSportsbookHomeResponse: ...
    @overload
    async def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_league(self, **params: Unpack[FanduelSportsbookLeagueDefaultParams]) -> FanduelSportsbookLeagueResponse: ...
    @overload
    async def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live(self, **params: Unpack[FanduelSportsbookLiveDefaultParams]) -> FanduelSportsbookLiveResponse: ...
    @overload
    async def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live_count(self, **params: Unpack[FanduelSportsbookLiveCountDefaultParams]) -> FanduelSportsbookLiveCountResponse: ...
    @overload
    async def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live_data(self, **params: Unpack[FanduelSportsbookLiveDataDefaultParams]) -> FanduelSportsbookLiveDataResponse: ...
    @overload
    async def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_live_scores(self, **params: Unpack[FanduelSportsbookLiveScoresDefaultParams]) -> FanduelSportsbookLiveScoresResponse: ...
    @overload
    async def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_market_prices(self, **params: Unpack[FanduelSportsbookMarketPricesDefaultParams]) -> FanduelSportsbookMarketPricesResponse: ...
    @overload
    async def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_parlays(self, **params: Unpack[FanduelSportsbookParlaysDefaultParams]) -> FanduelSportsbookParlaysResponse: ...
    @overload
    async def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player(self, **params: Unpack[FanduelSportsbookPlayerDefaultParams]) -> FanduelSportsbookPlayerResponse: ...
    @overload
    async def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player_news(self, **params: Unpack[FanduelSportsbookPlayerNewsDefaultParams]) -> FanduelSportsbookPlayerNewsResponse: ...
    @overload
    async def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player_props(self, **params: Unpack[FanduelSportsbookPlayerPropsDefaultParams]) -> FanduelSportsbookPlayerPropsResponse: ...
    @overload
    async def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_player_stats(self, **params: Unpack[FanduelSportsbookPlayerStatsDefaultParams]) -> FanduelSportsbookPlayerStatsResponse: ...
    @overload
    async def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_players(self, **params: Unpack[FanduelSportsbookPlayersDefaultParams]) -> FanduelSportsbookPlayersResponse: ...
    @overload
    async def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_promotions(self, **params: Unpack[FanduelSportsbookPromotionsDefaultParams]) -> FanduelSportsbookPromotionsResponse: ...
    @overload
    async def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_schedule(self, **params: Unpack[FanduelSportsbookScheduleDefaultParams]) -> FanduelSportsbookScheduleResponse: ...
    @overload
    async def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_search(self, **params: Unpack[FanduelSportsbookSearchDefaultParams]) -> FanduelSportsbookSearchResponse: ...
    @overload
    async def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_search_tabs(self, **params: Unpack[FanduelSportsbookSearchTabsDefaultParams]) -> FanduelSportsbookSearchTabsResponse: ...
    @overload
    async def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_sport(self, **params: Unpack[FanduelSportsbookSportDefaultParams]) -> FanduelSportsbookSportResponse: ...
    @overload
    async def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_sports(self, **params: Unpack[FanduelSportsbookSportsDefaultParams]) -> FanduelSportsbookSportsResponse: ...
    @overload
    async def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_standings(self, **params: Unpack[FanduelSportsbookStandingsDefaultParams]) -> FanduelSportsbookStandingsResponse: ...
    @overload
    async def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_stats(self, **params: Unpack[FanduelSportsbookStatsDefaultParams]) -> FanduelSportsbookStatsResponse: ...
    @overload
    async def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_depth_chart(self, **params: Unpack[FanduelSportsbookTeamDepthChartDefaultParams]) -> FanduelSportsbookTeamDepthChartResponse: ...
    @overload
    async def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_news(self, **params: Unpack[FanduelSportsbookTeamNewsDefaultParams]) -> FanduelSportsbookTeamNewsResponse: ...
    @overload
    async def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_odds(self, **params: Unpack[FanduelSportsbookTeamOddsDefaultParams]) -> FanduelSportsbookTeamOddsResponse: ...
    @overload
    async def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_roster(self, **params: Unpack[FanduelSportsbookTeamRosterDefaultParams]) -> FanduelSportsbookTeamRosterResponse: ...
    @overload
    async def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_schedule(self, **params: Unpack[FanduelSportsbookTeamScheduleDefaultParams]) -> FanduelSportsbookTeamScheduleResponse: ...
    @overload
    async def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_team_stats(self, **params: Unpack[FanduelSportsbookTeamStatsDefaultParams]) -> FanduelSportsbookTeamStatsResponse: ...
    @overload
    async def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_teams(self, **params: Unpack[FanduelSportsbookTeamsDefaultParams]) -> FanduelSportsbookTeamsResponse: ...
    @overload
    async def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingTextResponseParams]) -> str: ...
    @overload
    async def sportsbook_trending(self, **params: Unpack[FanduelSportsbookTrendingDefaultParams]) -> FanduelSportsbookTrendingResponse: ...

FanduelCasinoCategoriesDefaultParams = TypedDict('FanduelCasinoCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'region': NotRequired[Literal['mi', 'on']],
}, total=False)

FanduelCasinoCategoriesTextResponseParams = TypedDict('FanduelCasinoCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'region': NotRequired[Literal['mi', 'on']],
}, total=False)

FanduelCasinoCategoriesStreamParams = TypedDict('FanduelCasinoCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'region': NotRequired[Literal['mi', 'on']],
}, total=False)

FanduelCasinoCategoryDefaultParams = TypedDict('FanduelCasinoCategoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'region': NotRequired[Literal['mi', 'on']],
    'category': Required[Literal['all-games', 'new', 'slots', 'double-your-bet-category', 'jackpots', 'daily-jackpots', 'hot-slots', 'classic-reels-category', 'bonus-buy-category', 'high-limit-category', 'spooky-slots-category', 'exclusives', 'pick-play', 'arcade', 'blackjack', 'baccarat', 'roulette', 'table', 'livecasino', 'online-casino-favorites', 'explore-videos', 'motorcity-favorites', 'fallsview-favourites-category', 'the-wolf-den-category', 'sports-central']],
    'q': NotRequired[str],
    'provider': NotRequired[str],
    'badge': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelCasinoCategoryTextResponseParams = TypedDict('FanduelCasinoCategoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'region': NotRequired[Literal['mi', 'on']],
    'category': Required[Literal['all-games', 'new', 'slots', 'double-your-bet-category', 'jackpots', 'daily-jackpots', 'hot-slots', 'classic-reels-category', 'bonus-buy-category', 'high-limit-category', 'spooky-slots-category', 'exclusives', 'pick-play', 'arcade', 'blackjack', 'baccarat', 'roulette', 'table', 'livecasino', 'online-casino-favorites', 'explore-videos', 'motorcity-favorites', 'fallsview-favourites-category', 'the-wolf-den-category', 'sports-central']],
    'q': NotRequired[str],
    'provider': NotRequired[str],
    'badge': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelCasinoCategoryStreamParams = TypedDict('FanduelCasinoCategoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'region': NotRequired[Literal['mi', 'on']],
    'category': Required[Literal['all-games', 'new', 'slots', 'double-your-bet-category', 'jackpots', 'daily-jackpots', 'hot-slots', 'classic-reels-category', 'bonus-buy-category', 'high-limit-category', 'spooky-slots-category', 'exclusives', 'pick-play', 'arcade', 'blackjack', 'baccarat', 'roulette', 'table', 'livecasino', 'online-casino-favorites', 'explore-videos', 'motorcity-favorites', 'fallsview-favourites-category', 'the-wolf-den-category', 'sports-central']],
    'q': NotRequired[str],
    'provider': NotRequired[str],
    'badge': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelCasinoGameDefaultParams = TypedDict('FanduelCasinoGameDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'region': NotRequired[Literal['mi', 'on']],
    'game': Required[str],
}, total=False)

FanduelCasinoGameTextResponseParams = TypedDict('FanduelCasinoGameTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'region': NotRequired[Literal['mi', 'on']],
    'game': Required[str],
}, total=False)

FanduelCasinoGameStreamParams = TypedDict('FanduelCasinoGameStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'region': NotRequired[Literal['mi', 'on']],
    'game': Required[str],
}, total=False)

FanduelRacingCarryoverPoolsDefaultParams = TypedDict('FanduelRacingCarryoverPoolsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingCarryoverPoolsTextResponseParams = TypedDict('FanduelRacingCarryoverPoolsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingCarryoverPoolsStreamParams = TypedDict('FanduelRacingCarryoverPoolsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingFiltersDefaultParams = TypedDict('FanduelRacingFiltersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FanduelRacingFiltersTextResponseParams = TypedDict('FanduelRacingFiltersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FanduelRacingFiltersStreamParams = TypedDict('FanduelRacingFiltersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FanduelRacingHorseDefaultParams = TypedDict('FanduelRacingHorseDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingHorseTextResponseParams = TypedDict('FanduelRacingHorseTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingHorseStreamParams = TypedDict('FanduelRacingHorseStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastRaceDefaultParams = TypedDict('FanduelRacingPastRaceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'date': Required[str],
    'track': Required[str],
    'number': Required[str],
}, total=False)

FanduelRacingPastRaceTextResponseParams = TypedDict('FanduelRacingPastRaceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'date': Required[str],
    'track': Required[str],
    'number': Required[str],
}, total=False)

FanduelRacingPastRaceStreamParams = TypedDict('FanduelRacingPastRaceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'date': Required[str],
    'track': Required[str],
    'number': Required[str],
}, total=False)

FanduelRacingPastRacesDefaultParams = TypedDict('FanduelRacingPastRacesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'date': Required[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastRacesTextResponseParams = TypedDict('FanduelRacingPastRacesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'date': Required[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastRacesStreamParams = TypedDict('FanduelRacingPastRacesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'date': Required[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastTracksDefaultParams = TypedDict('FanduelRacingPastTracksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'date': NotRequired[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastTracksTextResponseParams = TypedDict('FanduelRacingPastTracksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'date': NotRequired[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingPastTracksStreamParams = TypedDict('FanduelRacingPastTracksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'date': NotRequired[str],
    'track': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingRaceDefaultParams = TypedDict('FanduelRacingRaceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'track': Required[str],
    'number': Required[str],
    'include': NotRequired[Literal['handicapping', 'timeform', 'pool_grids']],
}, total=False)

FanduelRacingRaceTextResponseParams = TypedDict('FanduelRacingRaceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'track': Required[str],
    'number': Required[str],
    'include': NotRequired[Literal['handicapping', 'timeform', 'pool_grids']],
}, total=False)

FanduelRacingRaceStreamParams = TypedDict('FanduelRacingRaceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'track': Required[str],
    'number': Required[str],
    'include': NotRequired[Literal['handicapping', 'timeform', 'pool_grids']],
}, total=False)

FanduelRacingRacesDefaultParams = TypedDict('FanduelRacingRacesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'open': NotRequired[bool],
    'within_minutes': NotRequired[int],
    'sort': NotRequired[Literal['mtp', 'post_time', 'race_number']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingRacesTextResponseParams = TypedDict('FanduelRacingRacesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'open': NotRequired[bool],
    'within_minutes': NotRequired[int],
    'sort': NotRequired[Literal['mtp', 'post_time', 'race_number']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingRacesStreamParams = TypedDict('FanduelRacingRacesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'status': NotRequired[Literal['O', 'IC', 'SK', 'RO']],
    'open': NotRequired[bool],
    'within_minutes': NotRequired[int],
    'sort': NotRequired[Literal['mtp', 'post_time', 'race_number']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingResultsDefaultParams = TypedDict('FanduelRacingResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingResultsTextResponseParams = TypedDict('FanduelRacingResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingResultsStreamParams = TypedDict('FanduelRacingResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'track': NotRequired[str],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingSearchDefaultParams = TypedDict('FanduelRacingSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'type': NotRequired[Literal['runner', 'jockey', 'trainer', 'owner']],
    'sort': NotRequired[Literal['name', 'last_event']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingSearchTextResponseParams = TypedDict('FanduelRacingSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'type': NotRequired[Literal['runner', 'jockey', 'trainer', 'owner']],
    'sort': NotRequired[Literal['name', 'last_event']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingSearchStreamParams = TypedDict('FanduelRacingSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'type': NotRequired[Literal['runner', 'jockey', 'trainer', 'owner']],
    'sort': NotRequired[Literal['name', 'last_event']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingTrackDefaultParams = TypedDict('FanduelRacingTrackDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'code': Required[str],
}, total=False)

FanduelRacingTrackTextResponseParams = TypedDict('FanduelRacingTrackTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'code': Required[str],
}, total=False)

FanduelRacingTrackStreamParams = TypedDict('FanduelRacingTrackStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'code': Required[str],
}, total=False)

FanduelRacingTracksDefaultParams = TypedDict('FanduelRacingTracksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'code': NotRequired[str],
    'finished': NotRequired[bool],
    'featured': NotRequired[bool],
    'sort': NotRequired[Literal['name', 'mtp', 'wagerable_mtp', 'ivr']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingTracksTextResponseParams = TypedDict('FanduelRacingTracksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'code': NotRequired[str],
    'finished': NotRequired[bool],
    'featured': NotRequired[bool],
    'sort': NotRequired[Literal['name', 'mtp', 'wagerable_mtp', 'ivr']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingTracksStreamParams = TypedDict('FanduelRacingTracksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': NotRequired[str],
    'exclude_country': NotRequired[str],
    'race_type': NotRequired[Literal['T', 'H', 'Q', 'L']],
    'code': NotRequired[str],
    'finished': NotRequired[bool],
    'featured': NotRequired[bool],
    'sort': NotRequired[Literal['name', 'mtp', 'wagerable_mtp', 'ivr']],
    'order': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelRacingWagerTypesDefaultParams = TypedDict('FanduelRacingWagerTypesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FanduelRacingWagerTypesTextResponseParams = TypedDict('FanduelRacingWagerTypesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FanduelRacingWagerTypesStreamParams = TypedDict('FanduelRacingWagerTypesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FanduelResearchDefaultParams = TypedDict('FanduelResearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FanduelResearchTextResponseParams = TypedDict('FanduelResearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FanduelResearchStreamParams = TypedDict('FanduelResearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FanduelResearchArticleDefaultParams = TypedDict('FanduelResearchArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'article': Required[str],
}, total=False)

FanduelResearchArticleTextResponseParams = TypedDict('FanduelResearchArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'article': Required[str],
}, total=False)

FanduelResearchArticleStreamParams = TypedDict('FanduelResearchArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'article': Required[str],
}, total=False)

FanduelResearchArticlesDefaultParams = TypedDict('FanduelResearchArticlesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'exclude_sport': NotRequired[str],
    'sub_category': NotRequired[str],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'author': NotRequired[str],
    'hero_type': NotRequired[Literal['IMAGE', 'JWPLAYER']],
    'published_after': NotRequired[str],
    'published_before': NotRequired[str],
    'hide_deprioritized': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchArticlesTextResponseParams = TypedDict('FanduelResearchArticlesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'exclude_sport': NotRequired[str],
    'sub_category': NotRequired[str],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'author': NotRequired[str],
    'hero_type': NotRequired[Literal['IMAGE', 'JWPLAYER']],
    'published_after': NotRequired[str],
    'published_before': NotRequired[str],
    'hide_deprioritized': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchArticlesStreamParams = TypedDict('FanduelResearchArticlesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'exclude_sport': NotRequired[str],
    'sub_category': NotRequired[str],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'author': NotRequired[str],
    'hero_type': NotRequired[Literal['IMAGE', 'JWPLAYER']],
    'published_after': NotRequired[str],
    'published_before': NotRequired[str],
    'hide_deprioritized': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchAuthorDefaultParams = TypedDict('FanduelResearchAuthorDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'author': Required[str],
}, total=False)

FanduelResearchAuthorTextResponseParams = TypedDict('FanduelResearchAuthorTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'author': Required[str],
}, total=False)

FanduelResearchAuthorStreamParams = TypedDict('FanduelResearchAuthorStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'author': Required[str],
}, total=False)

FanduelResearchAuthorsDefaultParams = TypedDict('FanduelResearchAuthorsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchAuthorsTextResponseParams = TypedDict('FanduelResearchAuthorsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchAuthorsStreamParams = TypedDict('FanduelResearchAuthorsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchFeaturedArticlesDefaultParams = TypedDict('FanduelResearchFeaturedArticlesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchFeaturedArticlesTextResponseParams = TypedDict('FanduelResearchFeaturedArticlesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchFeaturedArticlesStreamParams = TypedDict('FanduelResearchFeaturedArticlesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchFixturesDefaultParams = TypedDict('FanduelResearchFixturesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['nba', 'nfl', 'nhl', 'mlb']],
}, total=False)

FanduelResearchFixturesTextResponseParams = TypedDict('FanduelResearchFixturesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['nba', 'nfl', 'nhl', 'mlb']],
}, total=False)

FanduelResearchFixturesStreamParams = TypedDict('FanduelResearchFixturesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['nba', 'nfl', 'nhl', 'mlb']],
}, total=False)

FanduelResearchNflScheduleDefaultParams = TypedDict('FanduelResearchNflScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'week': Required[int],
    'season_type': NotRequired[Literal['PRE', 'REGULAR', 'POST']],
}, total=False)

FanduelResearchNflScheduleTextResponseParams = TypedDict('FanduelResearchNflScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'week': Required[int],
    'season_type': NotRequired[Literal['PRE', 'REGULAR', 'POST']],
}, total=False)

FanduelResearchNflScheduleStreamParams = TypedDict('FanduelResearchNflScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'week': Required[int],
    'season_type': NotRequired[Literal['PRE', 'REGULAR', 'POST']],
}, total=False)

FanduelResearchPlayerNewsDefaultParams = TypedDict('FanduelResearchPlayerNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['nfl', 'nba', 'mlb', 'nhl']],
    'news_type': NotRequired[Literal['INJURY', 'RECAP', 'TRANSACTION', 'LINEUP', 'GAME_UPDATE', 'OUTLOOK']],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'position': NotRequired[Literal['G', 'F', 'C', 'W', 'D', 'QB', 'DB', 'DL', 'K', 'LB', 'OL', 'P', 'RB', 'TE', 'WR', 'IF', 'OF', 'DH']],
    'include_non_primary': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchPlayerNewsTextResponseParams = TypedDict('FanduelResearchPlayerNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['nfl', 'nba', 'mlb', 'nhl']],
    'news_type': NotRequired[Literal['INJURY', 'RECAP', 'TRANSACTION', 'LINEUP', 'GAME_UPDATE', 'OUTLOOK']],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'position': NotRequired[Literal['G', 'F', 'C', 'W', 'D', 'QB', 'DB', 'DL', 'K', 'LB', 'OL', 'P', 'RB', 'TE', 'WR', 'IF', 'OF', 'DH']],
    'include_non_primary': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchPlayerNewsStreamParams = TypedDict('FanduelResearchPlayerNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['nfl', 'nba', 'mlb', 'nhl']],
    'news_type': NotRequired[Literal['INJURY', 'RECAP', 'TRANSACTION', 'LINEUP', 'GAME_UPDATE', 'OUTLOOK']],
    'team': NotRequired[int],
    'player': NotRequired[int],
    'position': NotRequired[Literal['G', 'F', 'C', 'W', 'D', 'QB', 'DB', 'DL', 'K', 'LB', 'OL', 'P', 'RB', 'TE', 'WR', 'IF', 'OF', 'DH']],
    'include_non_primary': NotRequired[bool],
    'limit': NotRequired[int],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchQuickPicksDailyDefaultParams = TypedDict('FanduelResearchQuickPicksDailyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchQuickPicksDailyTextResponseParams = TypedDict('FanduelResearchQuickPicksDailyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchQuickPicksDailyStreamParams = TypedDict('FanduelResearchQuickPicksDailyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'cursor': NotRequired[str],
}, total=False)

FanduelResearchProjectionSlatesDefaultParams = TypedDict('FanduelResearchProjectionSlatesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
}, total=False)

FanduelResearchProjectionSlatesTextResponseParams = TypedDict('FanduelResearchProjectionSlatesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
}, total=False)

FanduelResearchProjectionSlatesStreamParams = TypedDict('FanduelResearchProjectionSlatesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
}, total=False)

FanduelResearchProjectionTablesDefaultParams = TypedDict('FanduelResearchProjectionTablesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
}, total=False)

FanduelResearchProjectionTablesTextResponseParams = TypedDict('FanduelResearchProjectionTablesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
}, total=False)

FanduelResearchProjectionTablesStreamParams = TypedDict('FanduelResearchProjectionTablesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
}, total=False)

FanduelResearchProjectionsDefaultParams = TypedDict('FanduelResearchProjectionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'type': Required[Literal['DAILY', 'WEEKLY', 'YEARLY', 'REMAINING', 'PPR', 'SEASON_STATS']],
    'position': NotRequired[Literal['batters', 'pitchers', 'c', '1b', '2b', '3b', 'ss', 'of', 'sp', 'rp', 'qb', 'rb', 'wr', 'te', 'flex', 'k', 'defense', 'all', 'pg', 'sg', 'guards', 'sf', 'pf', 'forwards', 'centers', 'skaters', 'goalies', 'wingers', 'd', 'idp']],
    'scope': NotRequired[Literal['TOTAL', 'PER_GAME']],
    'slate_id': NotRequired[str],
    'event_id': NotRequired[str],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelResearchProjectionsTextResponseParams = TypedDict('FanduelResearchProjectionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'type': Required[Literal['DAILY', 'WEEKLY', 'YEARLY', 'REMAINING', 'PPR', 'SEASON_STATS']],
    'position': NotRequired[Literal['batters', 'pitchers', 'c', '1b', '2b', '3b', 'ss', 'of', 'sp', 'rp', 'qb', 'rb', 'wr', 'te', 'flex', 'k', 'defense', 'all', 'pg', 'sg', 'guards', 'sf', 'pf', 'forwards', 'centers', 'skaters', 'goalies', 'wingers', 'd', 'idp']],
    'scope': NotRequired[Literal['TOTAL', 'PER_GAME']],
    'slate_id': NotRequired[str],
    'event_id': NotRequired[str],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelResearchProjectionsStreamParams = TypedDict('FanduelResearchProjectionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['mlb', 'nba', 'nfl', 'nhl', 'golf']],
    'type': Required[Literal['DAILY', 'WEEKLY', 'YEARLY', 'REMAINING', 'PPR', 'SEASON_STATS']],
    'position': NotRequired[Literal['batters', 'pitchers', 'c', '1b', '2b', '3b', 'ss', 'of', 'sp', 'rp', 'qb', 'rb', 'wr', 'te', 'flex', 'k', 'defense', 'all', 'pg', 'sg', 'guards', 'sf', 'pf', 'forwards', 'centers', 'skaters', 'goalies', 'wingers', 'd', 'idp']],
    'scope': NotRequired[Literal['TOTAL', 'PER_GAME']],
    'slate_id': NotRequired[str],
    'event_id': NotRequired[str],
    'date': NotRequired[str],
    'week': NotRequired[int],
    'season': NotRequired[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

FanduelResearchSportsDefaultParams = TypedDict('FanduelResearchSportsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchSportsTextResponseParams = TypedDict('FanduelResearchSportsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchSportsStreamParams = TypedDict('FanduelResearchSportsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['casino', 'nascar', 'ncaab', 'f1', 'ufc', 'boxing', 'ncaaf', 'womenssoccer', 'tv-and-podcast', 'nba', 'pga', 'tennis', 'nhl', 'mma', 'soccer', 'fanduel-sportsbook-promo-codes', 'sports-betting-101', 'horse-racing', 'wnba', 'predicts', 'mlb', 'canada', 'nfl']],
}, total=False)

FanduelResearchSubCategoriesDefaultParams = TypedDict('FanduelResearchSubCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FanduelResearchSubCategoriesTextResponseParams = TypedDict('FanduelResearchSubCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FanduelResearchSubCategoriesStreamParams = TypedDict('FanduelResearchSubCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FanduelSportsbookAutocompleteDefaultParams = TypedDict('FanduelSportsbookAutocompleteDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookAutocompleteTextResponseParams = TypedDict('FanduelSportsbookAutocompleteTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookAutocompleteStreamParams = TypedDict('FanduelSportsbookAutocompleteStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookBuilderDefaultParams = TypedDict('FanduelSportsbookBuilderDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderTextResponseParams = TypedDict('FanduelSportsbookBuilderTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderStreamParams = TypedDict('FanduelSportsbookBuilderStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderEventsDefaultParams = TypedDict('FanduelSportsbookBuilderEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderEventsTextResponseParams = TypedDict('FanduelSportsbookBuilderEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderEventsStreamParams = TypedDict('FanduelSportsbookBuilderEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'experience': NotRequired[Literal['yourway', 'head-to-head', 'player-combos', 'bullseye', 'player-podium', 'or-bets']],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderQuotesDefaultParams = TypedDict('FanduelSportsbookBuilderQuotesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ramp_event_id': Required[int],
    'choice_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderQuotesTextResponseParams = TypedDict('FanduelSportsbookBuilderQuotesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ramp_event_id': Required[int],
    'choice_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookBuilderQuotesStreamParams = TypedDict('FanduelSportsbookBuilderQuotesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ramp_event_id': Required[int],
    'choice_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookCompetitionDefaultParams = TypedDict('FanduelSportsbookCompetitionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookCompetitionTextResponseParams = TypedDict('FanduelSportsbookCompetitionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookCompetitionStreamParams = TypedDict('FanduelSportsbookCompetitionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookEventDefaultParams = TypedDict('FanduelSportsbookEventDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
}, total=False)

FanduelSportsbookEventTextResponseParams = TypedDict('FanduelSportsbookEventTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
}, total=False)

FanduelSportsbookEventStreamParams = TypedDict('FanduelSportsbookEventStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'market_type': NotRequired[str],
}, total=False)

FanduelSportsbookEventBoxScoreDefaultParams = TypedDict('FanduelSportsbookEventBoxScoreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventBoxScoreTextResponseParams = TypedDict('FanduelSportsbookEventBoxScoreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventBoxScoreStreamParams = TypedDict('FanduelSportsbookEventBoxScoreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventPlayByPlayDefaultParams = TypedDict('FanduelSportsbookEventPlayByPlayDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
    'current': NotRequired[bool],
}, total=False)

FanduelSportsbookEventPlayByPlayTextResponseParams = TypedDict('FanduelSportsbookEventPlayByPlayTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
    'current': NotRequired[bool],
}, total=False)

FanduelSportsbookEventPlayByPlayStreamParams = TypedDict('FanduelSportsbookEventPlayByPlayStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
    'current': NotRequired[bool],
}, total=False)

FanduelSportsbookEventPlayersDefaultParams = TypedDict('FanduelSportsbookEventPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventPlayersTextResponseParams = TypedDict('FanduelSportsbookEventPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventPlayersStreamParams = TypedDict('FanduelSportsbookEventPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventScoreDefaultParams = TypedDict('FanduelSportsbookEventScoreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventScoreTextResponseParams = TypedDict('FanduelSportsbookEventScoreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventScoreStreamParams = TypedDict('FanduelSportsbookEventScoreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventStatsDefaultParams = TypedDict('FanduelSportsbookEventStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventStatsTextResponseParams = TypedDict('FanduelSportsbookEventStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventStatsStreamParams = TypedDict('FanduelSportsbookEventStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[int],
}, total=False)

FanduelSportsbookEventsStatusDefaultParams = TypedDict('FanduelSportsbookEventsStatusDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookEventsStatusTextResponseParams = TypedDict('FanduelSportsbookEventsStatusTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookEventsStatusStreamParams = TypedDict('FanduelSportsbookEventsStatusStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookHomeDefaultParams = TypedDict('FanduelSportsbookHomeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookHomeTextResponseParams = TypedDict('FanduelSportsbookHomeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookHomeStreamParams = TypedDict('FanduelSportsbookHomeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLeagueDefaultParams = TypedDict('FanduelSportsbookLeagueDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'custom_page_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLeagueTextResponseParams = TypedDict('FanduelSportsbookLeagueTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'custom_page_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLeagueStreamParams = TypedDict('FanduelSportsbookLeagueStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'custom_page_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLiveDefaultParams = TypedDict('FanduelSportsbookLiveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLiveTextResponseParams = TypedDict('FanduelSportsbookLiveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLiveStreamParams = TypedDict('FanduelSportsbookLiveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookLiveCountDefaultParams = TypedDict('FanduelSportsbookLiveCountDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookLiveCountTextResponseParams = TypedDict('FanduelSportsbookLiveCountTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookLiveCountStreamParams = TypedDict('FanduelSportsbookLiveCountStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookLiveDataDefaultParams = TypedDict('FanduelSportsbookLiveDataDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[str],
}, total=False)

FanduelSportsbookLiveDataTextResponseParams = TypedDict('FanduelSportsbookLiveDataTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[str],
}, total=False)

FanduelSportsbookLiveDataStreamParams = TypedDict('FanduelSportsbookLiveDataStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[str],
}, total=False)

FanduelSportsbookLiveScoresDefaultParams = TypedDict('FanduelSportsbookLiveScoresDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookLiveScoresTextResponseParams = TypedDict('FanduelSportsbookLiveScoresTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookLiveScoresStreamParams = TypedDict('FanduelSportsbookLiveScoresStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_id': Required[list[str]],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookMarketPricesDefaultParams = TypedDict('FanduelSportsbookMarketPricesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'market_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookMarketPricesTextResponseParams = TypedDict('FanduelSportsbookMarketPricesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'market_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookMarketPricesStreamParams = TypedDict('FanduelSportsbookMarketPricesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'market_id': Required[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookParlaysDefaultParams = TypedDict('FanduelSportsbookParlaysDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'view': NotRequired[Literal['popular', 'all', 'next-to-start', 'event']],
    'event_id': NotRequired[int],
    'type': NotRequired[Literal['PARLAY', 'SGP', 'SGP_PLUS']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': NotRequired[str],
    'min_odds': NotRequired[float],
    'max_odds': NotRequired[float],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookParlaysTextResponseParams = TypedDict('FanduelSportsbookParlaysTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'view': NotRequired[Literal['popular', 'all', 'next-to-start', 'event']],
    'event_id': NotRequired[int],
    'type': NotRequired[Literal['PARLAY', 'SGP', 'SGP_PLUS']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': NotRequired[str],
    'min_odds': NotRequired[float],
    'max_odds': NotRequired[float],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookParlaysStreamParams = TypedDict('FanduelSportsbookParlaysStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'view': NotRequired[Literal['popular', 'all', 'next-to-start', 'event']],
    'event_id': NotRequired[int],
    'type': NotRequired[Literal['PARLAY', 'SGP', 'SGP_PLUS']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'competition_id': NotRequired[str],
    'min_odds': NotRequired[float],
    'max_odds': NotRequired[float],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookPlayerDefaultParams = TypedDict('FanduelSportsbookPlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerTextResponseParams = TypedDict('FanduelSportsbookPlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerStreamParams = TypedDict('FanduelSportsbookPlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerNewsDefaultParams = TypedDict('FanduelSportsbookPlayerNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookPlayerNewsTextResponseParams = TypedDict('FanduelSportsbookPlayerNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookPlayerNewsStreamParams = TypedDict('FanduelSportsbookPlayerNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookPlayerPropsDefaultParams = TypedDict('FanduelSportsbookPlayerPropsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerPropsTextResponseParams = TypedDict('FanduelSportsbookPlayerPropsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerPropsStreamParams = TypedDict('FanduelSportsbookPlayerPropsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerStatsDefaultParams = TypedDict('FanduelSportsbookPlayerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerStatsTextResponseParams = TypedDict('FanduelSportsbookPlayerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayerStatsStreamParams = TypedDict('FanduelSportsbookPlayerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba']],
    'player': Required[str],
}, total=False)

FanduelSportsbookPlayersDefaultParams = TypedDict('FanduelSportsbookPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba']],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelSportsbookPlayersTextResponseParams = TypedDict('FanduelSportsbookPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba']],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelSportsbookPlayersStreamParams = TypedDict('FanduelSportsbookPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba']],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FanduelSportsbookPromotionsDefaultParams = TypedDict('FanduelSportsbookPromotionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'context': NotRequired[Literal['home', 'league', 'sport']],
    'custom_page_id': NotRequired[str],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'tag': NotRequired[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookPromotionsTextResponseParams = TypedDict('FanduelSportsbookPromotionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'context': NotRequired[Literal['home', 'league', 'sport']],
    'custom_page_id': NotRequired[str],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'tag': NotRequired[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookPromotionsStreamParams = TypedDict('FanduelSportsbookPromotionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'context': NotRequired[Literal['home', 'league', 'sport']],
    'custom_page_id': NotRequired[str],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'tag': NotRequired[str],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookScheduleDefaultParams = TypedDict('FanduelSportsbookScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
    'week': NotRequired[str],
    'date': NotRequired[str],
    'end_date': NotRequired[str],
}, total=False)

FanduelSportsbookScheduleTextResponseParams = TypedDict('FanduelSportsbookScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
    'week': NotRequired[str],
    'date': NotRequired[str],
    'end_date': NotRequired[str],
}, total=False)

FanduelSportsbookScheduleStreamParams = TypedDict('FanduelSportsbookScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
    'week': NotRequired[str],
    'date': NotRequired[str],
    'end_date': NotRequired[str],
}, total=False)

FanduelSportsbookSearchDefaultParams = TypedDict('FanduelSportsbookSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'event', 'competition']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'limit': NotRequired[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookSearchTextResponseParams = TypedDict('FanduelSportsbookSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'event', 'competition']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'limit': NotRequired[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookSearchStreamParams = TypedDict('FanduelSportsbookSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'event', 'competition']],
    'event_type_id': NotRequired[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'limit': NotRequired[int],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookSearchTabsDefaultParams = TypedDict('FanduelSportsbookSearchTabsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'tab': NotRequired[str],
    'pill': NotRequired[str],
    'start_index': NotRequired[int],
    'timezone': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookSearchTabsTextResponseParams = TypedDict('FanduelSportsbookSearchTabsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'tab': NotRequired[str],
    'pill': NotRequired[str],
    'start_index': NotRequired[int],
    'timezone': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookSearchTabsStreamParams = TypedDict('FanduelSportsbookSearchTabsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'tab': NotRequired[str],
    'pill': NotRequired[str],
    'start_index': NotRequired[int],
    'timezone': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

FanduelSportsbookSportDefaultParams = TypedDict('FanduelSportsbookSportDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookSportTextResponseParams = TypedDict('FanduelSportsbookSportTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookSportStreamParams = TypedDict('FanduelSportsbookSportStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'event_type_id': Required[Literal['6423', '1', '7522', '3', '7511', '7524', '2', '26420387', '2593174', '3503', '6', '5', '4', '8', '1477', '6422', '468328', '28608997', '998917', '4726642', '10', '2378961']],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
    'tab': NotRequired[str],
    'competition_id': NotRequired[int],
    'market_type': NotRequired[str],
    'exclude_markets': NotRequired[bool],
}, total=False)

FanduelSportsbookSportsDefaultParams = TypedDict('FanduelSportsbookSportsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookSportsTextResponseParams = TypedDict('FanduelSportsbookSportsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookSportsStreamParams = TypedDict('FanduelSportsbookSportsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'state': NotRequired[Literal['ar', 'az', 'co', 'ct', 'dc', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'mr', 'nc', 'nj', 'ny', 'oh', 'on', 'pa', 'pr', 'tn', 'va', 'vt', 'wv', 'wy']],
}, total=False)

FanduelSportsbookStandingsDefaultParams = TypedDict('FanduelSportsbookStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
}, total=False)

FanduelSportsbookStandingsTextResponseParams = TypedDict('FanduelSportsbookStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
}, total=False)

FanduelSportsbookStandingsStreamParams = TypedDict('FanduelSportsbookStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football']],
}, total=False)

FanduelSportsbookStatsDefaultParams = TypedDict('FanduelSportsbookStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'competition_id': NotRequired[int],
}, total=False)

FanduelSportsbookStatsTextResponseParams = TypedDict('FanduelSportsbookStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'competition_id': NotRequired[int],
}, total=False)

FanduelSportsbookStatsStreamParams = TypedDict('FanduelSportsbookStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'competition_id': NotRequired[int],
}, total=False)

FanduelSportsbookTeamDepthChartDefaultParams = TypedDict('FanduelSportsbookTeamDepthChartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamDepthChartTextResponseParams = TypedDict('FanduelSportsbookTeamDepthChartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamDepthChartStreamParams = TypedDict('FanduelSportsbookTeamDepthChartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamNewsDefaultParams = TypedDict('FanduelSportsbookTeamNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookTeamNewsTextResponseParams = TypedDict('FanduelSportsbookTeamNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookTeamNewsStreamParams = TypedDict('FanduelSportsbookTeamNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'cursor': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

FanduelSportsbookTeamOddsDefaultParams = TypedDict('FanduelSportsbookTeamOddsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamOddsTextResponseParams = TypedDict('FanduelSportsbookTeamOddsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamOddsStreamParams = TypedDict('FanduelSportsbookTeamOddsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamRosterDefaultParams = TypedDict('FanduelSportsbookTeamRosterDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'injured_only': NotRequired[bool],
    'status': NotRequired[str],
    'position': NotRequired[str],
}, total=False)

FanduelSportsbookTeamRosterTextResponseParams = TypedDict('FanduelSportsbookTeamRosterTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'injured_only': NotRequired[bool],
    'status': NotRequired[str],
    'position': NotRequired[str],
}, total=False)

FanduelSportsbookTeamRosterStreamParams = TypedDict('FanduelSportsbookTeamRosterStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
    'injured_only': NotRequired[bool],
    'status': NotRequired[str],
    'position': NotRequired[str],
}, total=False)

FanduelSportsbookTeamScheduleDefaultParams = TypedDict('FanduelSportsbookTeamScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamScheduleTextResponseParams = TypedDict('FanduelSportsbookTeamScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamScheduleStreamParams = TypedDict('FanduelSportsbookTeamScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamStatsDefaultParams = TypedDict('FanduelSportsbookTeamStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamStatsTextResponseParams = TypedDict('FanduelSportsbookTeamStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamStatsStreamParams = TypedDict('FanduelSportsbookTeamStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
    'team': Required[str],
}, total=False)

FanduelSportsbookTeamsDefaultParams = TypedDict('FanduelSportsbookTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': NotRequired[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
}, total=False)

FanduelSportsbookTeamsTextResponseParams = TypedDict('FanduelSportsbookTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': NotRequired[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
}, total=False)

FanduelSportsbookTeamsStreamParams = TypedDict('FanduelSportsbookTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': NotRequired[Literal['nfl', 'nba', 'mlb', 'college-football', 'college-basketball']],
}, total=False)

FanduelSportsbookTrendingDefaultParams = TypedDict('FanduelSportsbookTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'enriched': NotRequired[bool],
}, total=False)

FanduelSportsbookTrendingTextResponseParams = TypedDict('FanduelSportsbookTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'enriched': NotRequired[bool],
}, total=False)

FanduelSportsbookTrendingStreamParams = TypedDict('FanduelSportsbookTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'enriched': NotRequired[bool],
}, total=False)
