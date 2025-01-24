from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_image import BaseImage
    from ..base_link_button_action import BaseLinkButtonAction


class ItemHolidayRecommendationsBlockHeader(VkObject):
    """VK Object NewsfeedItemHolidayRecommendationsBlockHeader

    action -
    image -
    subtitle - Subtitle of the header
    title - Title of the header
    """

    action: Optional[BaseLinkButtonAction] = None
    image: Optional[List[BaseImage]] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
