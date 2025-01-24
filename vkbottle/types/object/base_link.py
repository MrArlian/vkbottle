from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .base_link_product import BaseLinkProduct
    from .base_link_button import BaseLinkButton
    from .base_link_application import BaseLinkApplication
    from .link_target_object import LinkTargetObject
    from .photos.photo import Photo
    from .video.video import Video
    from .base_link_rating import BaseLinkRating


class BaseLink(VkObject):
    """VK Object BaseLink

    application -
    button -
    caption - Link caption
    description - Link description
    id - Link ID
    is_external - Information whether the current link is external
    is_favorite -
    photo -
    preview_page - String ID of the page with article preview
    preview_url - URL of the page with article preview
    product -
    rating -
    target_object -
    title - Link title
    url - Link URL
    video - Video from link
    """

    application: Optional[BaseLinkApplication] = None
    button: Optional[BaseLinkButton] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_external: Optional[bool] = None
    is_favorite: Optional[bool] = None
    photo: Optional[Photo] = None
    preview_page: Optional[str] = None
    preview_url: Optional[str] = None
    product: Optional[BaseLinkProduct] = None
    rating: Optional[BaseLinkRating] = None
    target_object: Optional[LinkTargetObject] = None
    title: Optional[str] = None
    url: str
    video: Optional[Video] = None
