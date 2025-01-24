from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type, Self, Unpack
from types import TracebackType

from aiohttp import ClientSession, ClientResponse

from vkbottle.modules import JSONModule, json as json_module

from .abc import ABCHTTPClient

if TYPE_CHECKING:
    from .aiohttp_types import AiohttpRequestKwargs, AiohttpSessionKwargs


class AiohttpClient(ABCHTTPClient):
    def __init__(
        self,
        session: Optional[ClientSession] = None,
        json_processing_module: Optional[JSONModule] = None,
        optimize: bool = False,
        **session_params: Unpack[AiohttpSessionKwargs],
    ) -> None:
        json_serialize = session_params.pop("json_serialize", None)
        self.json_processing_module = json_processing_module or json_serialize or json_module

        if optimize:
            session_params["skip_auto_headers"] = {"User-Agent"}
            session_params["raise_for_status"] = True

        self.session = session

        self._session_params = session_params

    async def request_raw(
        self,
        url: str,
        method: str = "GET",
        data: Optional[dict] = None,
        **kwargs: Unpack[AiohttpRequestKwargs],
    ) -> ClientResponse:
        if not self.session:
            self.session = ClientSession(
                json_serialize=self.json_processing_module.dumps,
                **self._session_params,
            )
        async with self.session.request(url=url, method=method, data=data, **kwargs) as response:
            await response.read()
            return response

    async def request_json(
        self,
        url: str,
        method: str = "GET",
        data: Optional[dict] = None,
        **kwargs: Unpack[AiohttpRequestKwargs],
    ) -> dict:
        response = await self.request_raw(url, method, data, **kwargs)
        return await response.json(
            encoding="utf-8", loads=self.json_processing_module.loads, content_type=None
        )

    async def request_text(
        self,
        url: str,
        method: str = "GET",
        data: Optional[dict] = None,
        **kwargs: Unpack[AiohttpRequestKwargs],
    ) -> str:
        response = await self.request_raw(url, method, data, **kwargs)
        return await response.text(encoding="utf-8")

    async def request_content(
        self,
        url: str,
        method: str = "GET",
        data: Optional[dict] = None,
        **kwargs: Unpack[AiohttpRequestKwargs],
    ) -> bytes:
        response = await self.request_raw(url, method, data, **kwargs)
        return response._body

    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    def __del__(self) -> None:
        if self.session and not self.session.closed:
            if self.session._connector is not None and self.session._connector_owner:
                self.session._connector._close()
            self.session._connector = None


class SingleAiohttpClient(AiohttpClient):
    __instance__: Optional[Self] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:  # noqa: ARG003
        if cls.__instance__ is None:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        pass  # no need to close session in this case
