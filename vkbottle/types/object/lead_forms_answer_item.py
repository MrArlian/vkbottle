from __future__ import annotations

from typing import Optional

from ..base import VkObject


class LeadFormsAnswerItem(VkObject):
    """VK Object LeadFormsAnswerItem"""

    key: Optional[str] = None
    value: str
