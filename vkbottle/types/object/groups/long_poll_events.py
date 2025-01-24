from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LongPollEvents(VkObject):
    """VK Object GroupsLongPollEvents"""

    audio_new: bool
    board_post_delete: bool
    board_post_edit: bool
    board_post_new: bool
    board_post_restore: bool
    donut_money_withdraw: bool
    donut_money_withdraw_error: bool
    donut_subscription_cancelled: bool
    donut_subscription_create: bool
    donut_subscription_expired: bool
    donut_subscription_price_changed: bool
    donut_subscription_prolonged: bool
    group_change_photo: bool
    group_change_settings: bool
    group_join: bool
    group_leave: bool
    group_officers_edit: bool
    lead_forms_new: Optional[bool] = None
    market_comment_delete: bool
    market_comment_edit: bool
    market_comment_new: bool
    market_comment_restore: bool
    market_order_edit: Optional[bool] = None
    market_order_new: Optional[bool] = None
    message_allow: bool
    message_deny: bool
    message_edit: bool
    message_new: bool
    message_read: bool
    message_reply: bool
    message_typing_state: bool
    photo_comment_delete: bool
    photo_comment_edit: bool
    photo_comment_new: bool
    photo_comment_restore: bool
    photo_new: bool
    poll_vote_new: bool
    user_block: bool
    user_unblock: bool
    video_comment_delete: bool
    video_comment_edit: bool
    video_comment_new: bool
    video_comment_restore: bool
    video_new: bool
    wall_post_new: bool
    wall_reply_delete: bool
    wall_reply_edit: bool
    wall_reply_new: bool
    wall_reply_restore: bool
    wall_repost: bool
