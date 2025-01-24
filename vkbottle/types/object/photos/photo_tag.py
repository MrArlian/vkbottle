from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PhotoTag(VkObject):
    """VK Object PhotosPhotoTag

    date - Date when tag has been added in Unixtime
    description - Tagged description.
    id - Tag ID
    placer_id - ID of the tag creator
    tagged_name - Tag description
    user_id - Tagged user ID
    viewed - Information whether the tag is reviewed
    x - Coordinate X of the left upper corner
    x2 - Coordinate X of the right lower corner
    y - Coordinate Y of the left upper corner
    y2 - Coordinate Y of the right lower corner
    """

    date: int
    description: Optional[str] = None
    id: int
    placer_id: int
    tagged_name: str
    user_id: int
    viewed: bool
    x: float
    x2: float
    y: float
    y2: float
