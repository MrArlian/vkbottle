from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .tags_suggestion_item_button import TagsSuggestionItemButton
    from .photo_tag import PhotoTag
    from .photo import Photo


class TagsSuggestionItem(VkObject):
    """VK Object PhotosTagsSuggestionItem"""

    buttons: Optional[List[TagsSuggestionItemButton]] = None
    caption: Optional[str] = None
    photo: Optional[Photo] = None
    tags: Optional[List[PhotoTag]] = None
    title: Optional[str] = None
    track_code: Optional[str] = None
    type: Optional[str] = None
