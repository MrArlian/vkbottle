from typing import Optional

from ..base import VkObject


class AppPayload(VkObject):
    user_id: Optional[int] = None
    app_id: Optional[int] = None
    payload: Optional[str] = None
    group_id: Optional[int] = None
