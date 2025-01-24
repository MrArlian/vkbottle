from __future__ import annotations

from typing import TYPE_CHECKING, Union, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .base_link_button import BaseLinkButton
    from .base_image import BaseImage


class PrettyCardsPrettyCard(VkObject):
    """VK Object PrettyCardsPrettyCard

    button - Button key
    button_text - Button text in current language
    card_id - Card ID (long int returned as string)
    images -
    link_url - Link URL
    photo - Photo ID (format "<owner_id>_<media_id>")
    price - Price if set (decimal number returned as string)
    price_old - Old price if set (decimal number returned as string)
    title - Title
    """

    button: Optional[Union[BaseLinkButton, str]] = None
    button_text: Optional[str] = None
    card_id: str
    images: Optional[List[BaseImage]] = None
    link_url: str
    photo: str
    price: Optional[str] = None
    price_old: Optional[str] = None
    title: str
