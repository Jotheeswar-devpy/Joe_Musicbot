#  Copyright (c) 2025 Jotheeswar-devpy.
#  Joe_Musicbot is an open-source Telegram music bot licensed under AGPL-3.0.
#  All rights reserved where applicable.
#
#

__all__ = ["JiosaavnData", "SpotifyData", "YouTubeData", "ApiData"]

from ._api import ApiData
from ._jiosaavn import JiosaavnData
from ._spotify import SpotifyData
from ._youtube import YouTubeData
