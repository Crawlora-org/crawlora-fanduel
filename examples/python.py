import os

from crawlora_fanduel import FanDuelClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FanDuelClient(api_key=api_key) as client:
    casino_categories = client.casino_categories()
    print('casino_categories', casino_categories)
    racing_tracks = client.racing_tracks()
    print('racing_tracks', racing_tracks)
