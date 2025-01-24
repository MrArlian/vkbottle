from __future__ import annotations

from ...base import VkObject


class WikipageHistory(VkObject):
    """VK Object PagesWikipageHistory

    date - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    editor_name - Last editor name
    id - Version ID
    length - Page size in bytes
    """

    date: int
    editor_id: int
    editor_name: str
    id: int
    length: int
