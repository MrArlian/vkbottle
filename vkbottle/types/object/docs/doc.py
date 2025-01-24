from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .doc_preview import DocPreview


class Doc(VkObject):
    """VK Object DocsDoc

    access_key - Access key for the document
    date - Date when file has been uploaded in Unixtime
    ext - File extension
    id - Document ID
    is_licensed -
    owner_id - Document owner ID
    preview -
    size - File size in bites
    tags - Document tags
    title - Document title
    type - Document type
    url - File URL
    """

    access_key: Optional[str] = None
    date: int
    ext: str
    id: int
    is_licensed: Optional[bool] = None
    owner_id: int
    preview: Optional[DocPreview] = None
    size: int
    tags: Optional[List[str]] = None
    title: str
    type: int
    url: Optional[str] = None
