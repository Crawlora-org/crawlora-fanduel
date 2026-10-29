"""Typed FanDuel client for the Crawlora hosted API."""

from .platform import FanDuelClient, AsyncFanDuelClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FanDuelClient
AsyncClient = AsyncFanDuelClient
__version__ = '0.1.0'
DISPLAY_NAME = 'FanDuel'
PLATFORM = 'fanduel'
CONTRACT_REVISION = 'sha256:cb36ab030bfb9495ece6981b47d17cda615ba7a9959a2aaaef5da0122ed79a54'

__all__ = [
    "FanDuelClient", "AsyncFanDuelClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
