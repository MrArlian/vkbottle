from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Topic(VkObject):
    """VK Object BoardTopic

    comments - Comments number
    created - Date when the topic has been created in Unixtime
    created_by - Creator ID
    first_comment - First comment text
    id - Topic ID
    is_closed - Information whether the topic is closed
    is_fixed - Information whether the topic is fixed
    last_comment - Last comment text
    title - Topic title
    updated - Date when the topic has been updated in Unixtime
    updated_by - ID of user who updated the topic
    """

    comments: Optional[int] = None
    created: Optional[int] = None
    created_by: Optional[int] = None
    first_comment: Optional[str] = None
    id: Optional[int] = None
    is_closed: Optional[bool] = None
    is_fixed: Optional[bool] = None
    last_comment: Optional[str] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    updated_by: Optional[int] = None
