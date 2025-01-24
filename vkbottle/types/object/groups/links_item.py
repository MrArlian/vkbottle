from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LinksItem(VkObject):
    """VK Object GroupsLinksItem

    desc - Link description
    edit_title - Information whether the link title can be edited
    id - Link ID
    image_processing - Information whether the image on processing
    name - Link title
    photo_100 - URL of square image of the link with 100 pixels in width
    photo_50 - URL of square image of the link with 50 pixels in width
    url - Link URL
    """

    desc: Optional[str] = None
    edit_title: Optional[bool] = None
    id: Optional[int] = None
    image_processing: Optional[bool] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_50: Optional[str] = None
    url: Optional[str] = None
