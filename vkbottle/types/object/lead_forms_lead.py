from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .lead_forms_answer import LeadFormsAnswer


class LeadFormsLead(VkObject):
    """VK Object LeadFormsLead"""

    ad_id: Optional[int] = None
    answers: List[LeadFormsAnswer]
    date: int
    lead_id: int
    user_id: int
