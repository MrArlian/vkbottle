from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .lead_forms_question_item import LeadFormsQuestionItem


class LeadFormsForm(VkObject):
    """VK Object LeadFormsForm"""

    active: Optional[bool] = None
    confirmation: Optional[str] = None
    description: Optional[str] = None
    form_id: int
    group_id: int
    leads_count: int
    name: Optional[str] = None
    notify_admins: Optional[str] = None
    notify_emails: Optional[str] = None
    once_per_user: Optional[int] = None
    photo: Optional[str] = None
    pixel_code: Optional[str] = None
    policy_link_url: Optional[str] = None
    questions: Optional[List[LeadFormsQuestionItem]] = None
    site_link_url: Optional[str] = None
    title: Optional[str] = None
    url: str
