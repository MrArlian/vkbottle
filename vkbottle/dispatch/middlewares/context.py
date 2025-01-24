from typing import Dict, Optional, Any

from pydantic.dataclasses import dataclass

from vkbottle.types import VkGroupUpdate
from vkbottle.types.group_event import (
    MessageNew,
    MessageReply,
    MessageEdit,
    MessageAllow,
    MessageDeny,
    MessageTypingState,
    MessageEvent,
    PhotoNew,
    PhotoCommentNew,
    PhotoCommentEdit,
    PhotoCommentRestore,
    PhotoCommentDelete,
    AudioNew,
    VideoNew,
    VideoCommentNew,
    VideoCommentEdit,
    VideoCommentRestore,
    VideoCommentDelete,
    WallPostNew,
    WallRepost,
    WallReplyNew,
    WallReplyEdit,
    WallReplyRestore,
    WallReplyDelete,
    LikeAdd,
    LikeRemove,
    BoardPostNew,
    BoardPostEdit,
    BoardPostRestore,
    BoardPostDelete,
    MarketCommentNew,
    MarketCommentEdit,
    MarketCommentRestore,
    MarketCommentDelete,
    MarketOrderNew,
    MarketOrderEdit,
    GroupLeave,
    GroupJoin,
    UserBlock,
    UserUnblock,
    PollVoteNew,
    GroupOfficersEdit,
    GroupChangeSettings,
    GroupChangePhoto,
    VkpayTransaction,
    AppPayload,
    DonutSubscriptionCreate,
    DonutSubscriptionProlonged,
    DonutSubscriptionExpired,
    DonutSubscriptionCancelled,
    DonutSubscriptionPriceChanged,
    DonutMoneyWithdraw,
    DonutMoneyWithdrawError
)

from .base import BaseMiddleware, MiddlewareHandlerType


@dataclass(frozen=True)
class EventContext:
    group_id: int
    peer_id: Optional[int] = None
    from_id: Optional[int] = None


class EventContextMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: MiddlewareHandlerType,
        event: VkGroupUpdate,
        context: Dict[str, Any]
    ) -> Any:

        if not isinstance(event, VkGroupUpdate):
            raise TypeError

        context['event_context'] = self._get_group_context(event)
        return await handler(event, context)

    def _get_group_context(self, update: VkGroupUpdate) -> EventContext:
        _object = update.event_object
        group_id = update.group_id

        if isinstance(_object, MessageNew):
            return EventContext(group_id, _object.full_message.peer_id, _object.full_message.from_id)
        if isinstance(_object, (MessageReply, MessageEdit)):
            return EventContext(group_id, _object.peer_id, _object.from_id)
        if isinstance(_object, (MessageAllow, MessageDeny)):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, MessageTypingState):
            return EventContext(group_id, _object.to_id, _object.from_id)
        if isinstance(_object, MessageEvent):
            return EventContext(group_id, _object.peer_id, _object.user_id)

        if isinstance(_object, PhotoNew):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(
            _object,
            (
                PhotoCommentNew,
                PhotoCommentEdit,
                PhotoCommentRestore,
                PhotoCommentDelete
            )
        ):
            return EventContext(group_id, from_id=_object.from_id)

        if isinstance(_object, AudioNew):
            return EventContext(group_id, from_id=_object.owner_id)

        if isinstance(_object, VideoNew):
            return EventContext(group_id, from_id=_object.owner_id)
        if isinstance(
            _object,
            (
                VideoCommentNew,
                VideoCommentEdit,
                VideoCommentRestore
            )
        ):
            return EventContext(group_id, from_id=_object.from_id)
        if isinstance(_object, VideoCommentDelete):
            return EventContext(group_id, from_id=_object.deleter_id)

        if isinstance(_object, (WallPostNew, WallRepost)):
            return EventContext(group_id, from_id=_object.from_id)
        if isinstance(_object, (WallReplyNew, WallReplyEdit, WallReplyRestore)):
            return EventContext(group_id, from_id=_object.from_id)
        if isinstance(_object, WallReplyDelete):
            return EventContext(group_id, from_id=_object.deleter_id)

        if isinstance(_object, (LikeAdd, LikeRemove)):
            return EventContext(group_id, from_id=_object.liker_id)

        if isinstance(_object, (BoardPostNew, BoardPostEdit, BoardPostRestore)):
            return EventContext(group_id, from_id=_object.from_id)
        if isinstance(_object, BoardPostDelete):
            return EventContext(group_id)

        if isinstance(
            _object,
            (
                MarketCommentNew,
                MarketCommentEdit,
                MarketCommentRestore
            )
        ):
            return EventContext(group_id, from_id=_object)
        if isinstance(_object, MarketCommentDelete):
            return EventContext(group_id, from_id=_object.deleter_id)
        if isinstance(_object, (MarketOrderNew, MarketOrderEdit)):
            return EventContext(group_id, from_id=_object.user_id)

        if isinstance(_object, (GroupJoin, GroupLeave)):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, (UserBlock, UserUnblock)):
            return EventContext(group_id, from_id=_object.admin_id)

        if isinstance(_object, PollVoteNew):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, GroupOfficersEdit):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, GroupChangeSettings):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, GroupChangePhoto):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, VkpayTransaction):
            return EventContext(group_id, from_id=_object.from_id)
        if isinstance(_object, AppPayload):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, DonutSubscriptionCreate):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, DonutSubscriptionProlonged):
            return EventContext(group_id)
        if isinstance(_object, DonutSubscriptionExpired):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, DonutSubscriptionCancelled):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, DonutSubscriptionPriceChanged):
            return EventContext(group_id, from_id=_object.user_id)
        if isinstance(_object, DonutMoneyWithdraw):
            return EventContext(group_id)
        if isinstance(_object, DonutMoneyWithdrawError):
            return EventContext(group_id)

        return EventContext(group_id)
