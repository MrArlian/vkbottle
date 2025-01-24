from __future__ import annotations

from typing import Optional, Dict, List, Any, Generator

from vkbottle.types.base import VkObject
from vkbottle.enum.group_event_types import GroupEventTypes

from .event.vk_event_manager import VkSingleEventManager, HandlerNotFound


class BotRouter:

    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name

        self._parent: Optional[BotRouter] = None
        self._children: List[BotRouter] = []

        self.message_new = VkSingleEventManager(router=self, event_name='message_new')
        self.message_reply = VkSingleEventManager(router=self, event_name='message_reply')
        self.message_edit = VkSingleEventManager(router=self, event_name='message_edit')
        self.message_allow = VkSingleEventManager(router=self, event_name='message_allow')
        self.message_deny = VkSingleEventManager(router=self, event_name='message_deny')
        self.message_typing_state = VkSingleEventManager(router=self, event_name='message_typing_state')
        self.message_event = VkSingleEventManager(router=self, event_name='message_event')

        self.photo_new = VkSingleEventManager(router=self, event_name='photo_new')
        self.photo_comment_new = VkSingleEventManager(router=self, event_name='photo_comment_new')
        self.photo_comment_edit = VkSingleEventManager(router=self, event_name='photo_comment_edit')
        self.photo_comment_restore = VkSingleEventManager(router=self, event_name='photo_comment_restore')
        self.photo_comment_delete = VkSingleEventManager(router=self, event_name='photo_comment_delete')

        self.audio_new = VkSingleEventManager(router=self, event_name='audio_new')

        self.video_new = VkSingleEventManager(router=self, event_name='video_new')
        self.video_comment_new = VkSingleEventManager(router=self, event_name='video_comment_new')
        self.video_comment_edit = VkSingleEventManager(router=self, event_name='video_comment_edit')
        self.video_comment_restore = VkSingleEventManager(router=self, event_name='video_comment_restore')
        self.video_comment_delete = VkSingleEventManager(router=self, event_name='video_comment_delete')

        self.wall_post_new = VkSingleEventManager(router=self, event_name='wall_post_new')
        self.wall_repost = VkSingleEventManager(router=self, event_name='wall_repost')
        self.wall_reply_new = VkSingleEventManager(router=self, event_name='wall_reply_new')
        self.wall_reply_edit = VkSingleEventManager(router=self, event_name='wall_reply_edit')
        self.wall_reply_restore = VkSingleEventManager(router=self, event_name='wall_reply_restore')
        self.wall_reply_delete = VkSingleEventManager(router=self, event_name='wall_reply_delete')

        self.like_add = VkSingleEventManager(router=self, event_name='like_add')
        self.like_remove = VkSingleEventManager(router=self, event_name='like_remove')

        self.board_post_new = VkSingleEventManager(router=self, event_name='board_post_new')
        self.board_post_edit = VkSingleEventManager(router=self, event_name='board_post_edit')
        self.board_post_restore = VkSingleEventManager(router=self, event_name='board_post_restore')
        self.board_post_delete = VkSingleEventManager(router=self, event_name='board_post_delete')

        self.market_comment_new = VkSingleEventManager(router=self, event_name='market_comment_new')
        self.market_comment_edit = VkSingleEventManager(router=self, event_name='market_comment_edit')
        self.market_comment_restore = VkSingleEventManager(router=self, event_name='market_comment_restore')
        self.market_comment_delete = VkSingleEventManager(router=self, event_name='market_comment_delete')
        self.market_order_new = VkSingleEventManager(router=self, event_name='market_order_new')
        self.market_order_edit = VkSingleEventManager(router=self, event_name='market_order_edit')

        self.group_leave = VkSingleEventManager(router=self, event_name='group_leave')
        self.group_join = VkSingleEventManager(router=self, event_name='group_join')
        self.user_block = VkSingleEventManager(router=self, event_name='user_block')
        self.user_unblock = VkSingleEventManager(router=self, event_name='user_unblock')

        self.poll_vote_new = VkSingleEventManager(router=self, event_name='poll_vote_new')
        self.group_officers_edit = VkSingleEventManager(router=self, event_name='group_officers_edit')
        self.group_change_settings = VkSingleEventManager(router=self, event_name='group_change_settings')
        self.group_change_photo = VkSingleEventManager(router=self, event_name='group_change_photo')
        self.vkpay_transaction = VkSingleEventManager(router=self, event_name='vkpay_transaction')
        self.app_payload = VkSingleEventManager(router=self, event_name='app_payload')

        self.donut_subscription_create = VkSingleEventManager(router=self, event_name='donut_subscription_create')
        self.donut_subscription_prolonged = VkSingleEventManager(router=self, event_name='donut_subscription_prolonged')
        self.donut_subscription_expired = VkSingleEventManager(router=self, event_name='donut_subscription_expired')
        self.donut_subscription_cancelled = VkSingleEventManager(router=self, event_name='donut_subscription_cancelled')
        self.donut_subscription_price_changed = VkSingleEventManager(router=self, event_name='donut_subscription_price_changed')
        self.donut_money_withdraw = VkSingleEventManager(router=self, event_name='donut_money_withdraw')
        self.donut_money_withdraw_error = VkSingleEventManager(router=self, event_name='donut_money_withdraw_error')

        self.event_manager_map: Dict[str, VkSingleEventManager] = {
            'message_new': self.message_new,
            'message_reply': self.message_reply,
            'message_edit': self.message_edit,
            'message_allow': self.message_allow,
            'message_deny': self.message_deny,
            'message_typing_state': self.message_typing_state,
            'message_event': self.message_event,
            'photo_new': self.photo_new,
            'photo_comment_new': self.photo_comment_new,
            'photo_comment_edit': self.photo_comment_edit,
            'photo_comment_restore': self.photo_comment_restore,
            'photo_comment_delete': self.photo_comment_delete,
            'audio_new': self.audio_new,
            'video_new': self.video_new,
            'video_comment_new': self.video_comment_new,
            'video_comment_edit': self.video_comment_edit,
            'video_comment_restore': self.video_comment_restore,
            'video_comment_delete': self.video_comment_delete,
            'wall_post_new': self.wall_post_new,
            'wall_repost': self.wall_repost,
            'wall_reply_new': self.wall_reply_new,
            'wall_reply_edit': self.wall_reply_edit,
            'wall_reply_restore': self.wall_reply_restore,
            'wall_reply_delete': self.wall_reply_delete,
            'like_add': self.like_add,
            'like_remove': self.like_remove,
            'board_post_new': self.board_post_new,
            'board_post_edit': self.board_post_edit,
            'board_post_restore': self.board_post_restore,
            'board_post_delete': self.board_post_delete,
            'market_comment_new': self.market_comment_new,
            'market_comment_edit': self.market_comment_edit,
            'market_comment_restore': self.market_comment_restore,
            'market_comment_delete': self.market_comment_delete,
            'market_order_new': self.market_order_new,
            'market_order_edit': self.market_order_edit,
            'group_leave': self.group_leave,
            'group_join': self.group_join,
            'user_block': self.user_block,
            'user_unblock': self.user_unblock,
            'poll_vote_new': self.poll_vote_new,
            'group_officers_edit': self.group_officers_edit,
            'group_change_settings': self.group_change_settings,
            'group_change_photo': self.group_change_photo,
            'vkpay_transaction': self.vkpay_transaction,
            'app_payload': self.app_payload,
            'donut_subscription_create': self.donut_subscription_create,
            'donut_subscription_prolonged': self.donut_subscription_prolonged,
            'donut_subscription_expired': self.donut_subscription_expired,
            'donut_subscription_cancelled': self.donut_subscription_cancelled,
            'donut_subscription_price_changed': self.donut_subscription_price_changed,
            'donut_money_withdraw': self.donut_money_withdraw,
            'donut_money_withdraw_error': self.donut_money_withdraw_error
        }

    @property
    def parent(self) -> Optional[BotRouter]:
        return self._parent

    @parent.setter
    def parent(self, parent_router: BotRouter) -> None:
        """
            ...
        """
        if not isinstance(parent_router, BotRouter):
            raise ValueError(
                f"Expected 'parent_router' to be of type BotRouter, got {type(parent_router).__name__}"
            )
        if self._parent:
            raise RuntimeError(
                "This router already has a parent. Reassignment of the parent is not allowed."
            )
        if parent_router == self:
            raise RuntimeError("A router cannot be set as its own parent.")

        _parent: Optional[BotRouter] = parent_router
        while _parent is not None:
            if _parent == self:
                raise RuntimeError(
                    "Circular referencing of Router is not allowed"
                )
            _parent = _parent.parent

        self._parent = parent_router

    @property
    def parent_chain(self) -> Generator[BotRouter, None, None]:
        """
            ...
        """
        router: Optional[BotRouter] = self
        while router:
            yield router
            router = router.parent

    @property
    def child_chain(self) -> Generator[BotRouter, None, None]:
        """
            ...
        """
        yield self
        for child in self._children:
            yield from child.child_chain

    def include_routers(self, *sub_routers: BotRouter) -> None:
        """
            ...
        """
        for sub_router in sub_routers:
           self.include_router(sub_router)

    def include_router(self, sub_router: BotRouter) -> None:
        """
            ...
        """
        if not isinstance(sub_router, BotRouter):
            raise TypeError(
                f"Expected 'sub_router' to be of type BotRouter, got {type(sub_router).__name__}"
            )
        if sub_router == self:
            raise ValueError("A router cannot include itself as a sub-router.")

        sub_router.parent = self
        self._children.append(sub_router)

    async def process_event(
        self,
        update_type: GroupEventTypes,
        update_object: VkObject,
        **context: Any
    ) -> Any:
        """
            ...
        """
        event_manager = self.event_manager_map.get(update_type)
        context.update(router=self)

        if event_manager is None:
            raise ValueError

        response = await event_manager.root_middleware.apply_middlewares(
            callback=event_manager.trigger,
            event=update_object,
            context=context
        )

        if response is not HandlerNotFound:
            return response

        for child in self._children:
            response = await child.process_event(
                update_type=update_type,
                update_object=update_object,
                **context
            )

            if response is not HandlerNotFound:
                break

        return response

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name!r}"

    def __repr__(self) -> str:
        return f"<{self}>"
