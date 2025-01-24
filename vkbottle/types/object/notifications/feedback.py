from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..wall.wallpost_attachment import WallpostAttachment
    from ..base_geo import BaseGeo
    from ..base_likes_info import BaseLikesInfo


class Feedback(VkObject):
    """VK Object NotificationsFeedback

    attachments -
    from_id - Reply author's ID
    geo -
    id - Item ID
    likes -
    text - Reply text
    to_id - Wall owner's ID
    """

    attachments: Optional[List[WallpostAttachment]] = None
    from_id: Optional[int] = None
    geo: Optional[BaseGeo] = None
    id: Optional[int] = None
    likes: Optional[BaseLikesInfo] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
