from typing import Dict, Optional, AsyncGenerator, Any
from urllib.parse import urlencode

from vkbottle_types.responses.groups import GroupsLongPollServer
from vkbottle.types.group_event import VkGroupUpdate
from vkbottle.api import API

from .middlewares.context import EventContextMiddleware
from .middlewares.manager import MiddlewareManager
from .middlewares.fsm import FsmManagerMiddleware
from .router import BotRouter

from vkbottle.tools.storage import BaseFsmStorage


class Bot(BotRouter):

    def __init__(self, storage: BaseFsmStorage, name: Optional[str] = None) -> None:
        super().__init__(name=name)

        self.storage = storage

        self._base_middleware = MiddlewareManager()
        self._base_middleware.register(EventContextMiddleware())
        self._base_middleware.register(FsmManagerMiddleware(self.storage))

    async def _pre_processing_update(
        self,
        update: VkGroupUpdate,
        **context: Any
    ) -> Any:
        if not isinstance(update, VkGroupUpdate):
            raise RuntimeError(
                f"Expected VkGroupUpdate, got {type(update).__name__}"
            )

        context.update(update=update)
        return await self.process_event(
            update_type=update.type,
            update_object=update.event_object,
            **context
        )

    async def group_update(self, update: VkGroupUpdate, **kwargs: Any) -> Any:
        """
            ...
        """
        kwargs.update(group_id=update.group_id)
        return await self._base_middleware.apply_middlewares(
            callback=self._pre_processing_update,
            event=update,
            context=kwargs
        )

    async def raw_group_update(self, raw_update: Dict[str, Any], **kwargs: Any) -> Any:
        vk_update = VkGroupUpdate(**kwargs, **raw_update)
        return await self.group_update(vk_update, **kwargs)

    async def _listen_updates(
        self,
        *,
        api: API,
        server: GroupsLongPollServer,
        wait: int
    ) -> AsyncGenerator[Dict[str, Any], None]:
        request_data = {
            'act': 'a_chec',
            'key': server.key,
            'ts': server.ts,
            'wait': wait
        }

        while True:
            url = f"{server.server}?{urlencode(request_data)}"

            try:
                updates = await api.http_client.request_json(url, method="POST")
            except Exception as ex:
                raise Exception from ex

            if not updates:
                raise Exception

            request_data['ts'] = updates['ts']

            for update in updates['updates']:
                yield update

    async def run_polling(self, api: API, wait: int = 25) -> None:
        group_info = await api.groups.get_by_id()
        server = await api.groups.get_long_poll_server(group_info[0].id)

        async for update in self._listen_updates(
            api=api,
            server=server,
            wait=wait
        ):
            await self.raw_group_update(update, ctx_api=api)
