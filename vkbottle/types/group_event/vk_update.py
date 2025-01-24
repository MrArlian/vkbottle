from __future__ import annotations

from typing import Optional, Dict, Any, cast

from pydantic import Field

from vkbottle.enum.group_event_types import GroupEventTypes

from .message_new import MessageNew
from .message_reply import MessageReply
from .message_edit import MessageEdit
from .message_allow import MessageAllow
from .message_deny import MessageDeny
from .message_typing_state import MessageTypingState
from .message_event import MessageEvent
from .photo_new import PhotoNew
from .photo_comment_new import PhotoCommentNew
from .photo_comment_edit import PhotoCommentEdit
from .photo_comment_restore import PhotoCommentRestore
from .photo_comment_delete import PhotoCommentDelete
from .audio_new import AudioNew
from .video_new import VideoNew
from .video_comment_new import VideoCommentNew
from .video_comment_edit import VideoCommentEdit
from .video_comment_restore import VideoCommentRestore
from .video_comment_delete import VideoCommentDelete
from .wall_post_new import WallPostNew
from .wall_repost import WallRepost
from .wall_reply_new import WallReplyNew
from .wall_reply_edit import WallReplyEdit
from .wall_reply_restore import WallReplyRestore
from .wall_reply_delete import WallReplyDelete
from .like_add import LikeAdd
from .like_remove import LikeRemove
from .board_post_new import BoardPostNew
from .board_post_edit import BoardPostEdit
from .board_post_restore import BoardPostRestore
from .board_post_delete import BoardPostDelete
from .market_comment_new import MarketCommentNew
from .market_comment_edit import MarketCommentEdit
from .market_comment_restore import MarketCommentRestore
from .market_comment_delete import MarketCommentDelete
from .market_order_new import MarketOrderNew
from .market_order_edit import MarketOrderEdit
from .group_leave import GroupLeave
from .group_join import GroupJoin
from .user_block import UserBlock
from .user_unblock import UserUnblock
from .poll_vote_new import PollVoteNew
from .group_officers_edit import GroupOfficersEdit
from .group_change_settings import GroupChangeSettings
from .group_change_photo import GroupChangePhoto
from .vkpay_transaction import VkpayTransaction
from .app_payload import AppPayload
from .donut_subscription_create import DonutSubscriptionCreate
from .donut_subscription_prolonged import DonutSubscriptionProlonged
from .donut_subscription_expired import DonutSubscriptionExpired
from .donut_subscription_cancelled import DonutSubscriptionCancelled
from .donut_subscription_price_changed import DonutSubscriptionPriceChanged
from .donut_money_withdraw import DonutMoneyWithdraw
from .donut_money_withdraw_error import DonutMoneyWithdrawError

from ..base import VkObject


_map: Dict[GroupEventTypes, VkObject] = {
    GroupEventTypes.MESSAGE_NEW: MessageNew,
    GroupEventTypes.MESSAGE_REPLY: MessageReply,
    GroupEventTypes.MESSAGE_EDIT: MessageEdit,
    GroupEventTypes.MESSAGE_ALLOW: MessageAllow,
    GroupEventTypes.MESSAGE_DENY: MessageDeny,
    GroupEventTypes.MESSAGE_TYPING_STATE: MessageTypingState,
    GroupEventTypes.MESSAGE_EVENT: MessageEvent,
    GroupEventTypes.PHOTO_NEW: PhotoNew,
    GroupEventTypes.PHOTO_COMMENT_NEW: PhotoCommentNew,
    GroupEventTypes.PHOTO_COMMENT_EDIT: PhotoCommentEdit,
    GroupEventTypes.PHOTO_COMMENT_RESTORE: PhotoCommentRestore,
    GroupEventTypes.PHOTO_COMMENT_DELETE: PhotoCommentDelete,
    GroupEventTypes.AUDIO_NEW: AudioNew,
    GroupEventTypes.VIDEO_NEW: VideoNew,
    GroupEventTypes.VIDEO_COMMENT_NEW: VideoCommentNew,
    GroupEventTypes.VIDEO_COMMENT_EDIT: VideoCommentEdit,
    GroupEventTypes.VIDEO_COMMENT_RESTORE: VideoCommentRestore,
    GroupEventTypes.VIDEO_COMMENT_DELETE: VideoCommentDelete,
    GroupEventTypes.WALL_POST_NEW: WallPostNew,
    GroupEventTypes.WALL_REPOST: WallRepost,
    GroupEventTypes.WALL_REPLY_NEW: WallReplyNew,
    GroupEventTypes.WALL_REPLY_EDIT: WallReplyEdit,
    GroupEventTypes.WALL_REPLY_RESTORE: WallReplyRestore,
    GroupEventTypes.WALL_REPLY_DELETE: WallReplyDelete,
    GroupEventTypes.LIKE_ADD: LikeAdd,
    GroupEventTypes.LIKE_REMOVE: LikeRemove,
    GroupEventTypes.BOARD_POST_NEW: BoardPostNew,
    GroupEventTypes.BOARD_POST_EDIT: BoardPostEdit,
    GroupEventTypes.BOARD_POST_RESTORE: BoardPostRestore,
    GroupEventTypes.BOARD_POST_DELETE: BoardPostDelete,
    GroupEventTypes.MARKET_COMMENT_NEW: MarketCommentNew,
    GroupEventTypes.MARKET_COMMENT_EDIT: MarketCommentEdit,
    GroupEventTypes.MARKET_COMMENT_RESTORE: MarketCommentRestore,
    GroupEventTypes.MARKET_COMMENT_DELETE: MarketCommentDelete,
    GroupEventTypes.MARKET_ORDER_NEW: MarketOrderNew,
    GroupEventTypes.MARKET_ORDER_EDIT: MarketOrderEdit,
    GroupEventTypes.GROUP_LEAVE: GroupLeave,
    GroupEventTypes.GROUP_JOIN: GroupJoin,
    GroupEventTypes.USER_BLOCK: UserBlock,
    GroupEventTypes.USER_UNBLOCK: UserUnblock,
    GroupEventTypes.POLL_VOTE_NEW: PollVoteNew,
    GroupEventTypes.GROUP_OFFICERS_EDIT: GroupOfficersEdit,
    GroupEventTypes.GROUP_CHANGE_SETTINGS: GroupChangeSettings,
    GroupEventTypes.GROUP_CHANGE_PHOTO: GroupChangePhoto,
    GroupEventTypes.VKPAY_TRANSACTION: VkpayTransaction,
    GroupEventTypes.APP_PAYLOAD: AppPayload,
    GroupEventTypes.DONUT_SUBSCRIPTION_CREATE: DonutSubscriptionCreate,
    GroupEventTypes.DONUT_SUBSCRIPTION_PROLONGED: DonutSubscriptionProlonged,
    GroupEventTypes.DONUT_SUBSCRIPTION_EXPIRED: DonutSubscriptionExpired,
    GroupEventTypes.DONUT_SUBSCRIPTION_CANCELLED: DonutSubscriptionCancelled,
    GroupEventTypes.DONUT_SUBSCRIPTION_PRICE_CHANGED: DonutSubscriptionPriceChanged,
    GroupEventTypes.DONUT_MONEY_WITHDRAW: DonutMoneyWithdraw,
    GroupEventTypes.DONUT_MONEY_WITHDRAW_ERROR: DonutMoneyWithdrawError
}


class VkGroupUpdate(VkObject):
    type: GroupEventTypes
    event_id: str
    group_id: int
    object: Dict[str, Any]
    api_version: str = Field(alias='v')
    secret: Optional[str] = None

    @property
    def event_object(self) -> Optional[VkObject]:
        if object_type := _map.get(self.type):
            return cast(VkObject, object_type(ctx_api=self.api, **self.object))
