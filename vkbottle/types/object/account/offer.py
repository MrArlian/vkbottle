from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import LinkType

from ...base import VkObject


class Offer(VkObject):
    """VK Object AccountOffer

    currency_amount - Currency amount
    description - Offer description
    id - Offer ID
    img - URL of the preview image
    instruction - Instruction how to process the offer
    instruction_html - Instruction how to process the offer (HTML format)
    link_id - Link id
    link_type - Link type
    price - Offer price
    short_description - Offer short description
    tag - Offer tag
    title - Offer title
    """

    currency_amount: Optional[float] = None
    description: Optional[str] = None
    id: Optional[int] = None
    img: Optional[str] = None
    instruction: Optional[str] = None
    instruction_html: Optional[str] = None
    link_id: Optional[int] = None
    link_type: Optional[LinkType] = None
    price: Optional[int] = None
    short_description: Optional[str] = None
    tag: Optional[str] = None
    title: Optional[str] = None
