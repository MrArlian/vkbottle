from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_object_count import BaseObjectCount


class WidgetPage(VkObject):
    """VK Object WidgetsWidgetPage

    comments -
    date - Date when widgets on the page has been initialized firstly in Unixtime
    description - Page description
    id - Page ID
    likes -
    page_id - page_id parameter value
    photo - URL of the preview image
    title - Page title
    url - Page absolute URL
    """

    comments: Optional[BaseObjectCount] = None
    date: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    likes: Optional[BaseObjectCount] = None
    page_id: Optional[str] = None
    photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
