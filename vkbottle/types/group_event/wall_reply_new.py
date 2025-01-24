from typing import Optional

from ..object.wall import WallComment


class WallReplyNew(WallComment):
    post_id: Optional[int] = None
    post_owner_id: Optional[int] = None
