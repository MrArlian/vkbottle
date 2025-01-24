from typing import Optional

from ..object.wall import WallpostFull


class WallPostNew(WallpostFull):
    postponed_id: Optional[int] = None
