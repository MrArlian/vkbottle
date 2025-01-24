from __future__ import annotations

from typing import Any, Optional, List

from ...base import VkObject


class Info(VkObject):
    """VK Object AccountInfo

    _2fa_required - Two factor authentication is enabled
    country - Country code
    https_required - Information whether HTTPS-only is enabled
    intro - Information whether user has been processed intro
    lang - Language ID
    link_redirects -
    mini_apps_ads_slot_id - Ads slot id for MyTarget
    no_wall_replies - Information whether wall comments should be hidden
    own_posts_default - Information whether only owners posts should be shown
    qr_promotion -
    show_vk_apps_intro -
    subscriptions -
    wishlists_ae_promo_banner_show -
    """

    _2fa_required: Optional[bool] = None
    country: Optional[str] = None
    https_required: Optional[bool] = None
    intro: Optional[bool] = None
    lang: Optional[int] = None
    link_redirects: Optional[Any] = None
    mini_apps_ads_slot_id: Optional[int] = None
    no_wall_replies: Optional[bool] = None
    own_posts_default: Optional[bool] = None
    qr_promotion: Optional[int] = None
    show_vk_apps_intro: Optional[bool] = None
    subscriptions: Optional[List[int]] = None
    wishlists_ae_promo_banner_show: Optional[bool] = None
