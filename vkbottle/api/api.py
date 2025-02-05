from collections.abc import Callable, Awaitable
from typing import (
    AsyncIterator,
    NamedTuple,
    Sequence,
    Optional,
    Union,
    Any
)

from vkbottle_types import API_URL, API_VERSION

from vkbottle.api.request_rescheduler.blocking import BlockingRequestRescheduler
from vkbottle.api.token_generator import Token, get_token_generator
from vkbottle.api.abc import ABCAPI

from vkbottle.api.response_validator import JSONResponseValidator, VKAPIErrorResponseValidator
from vkbottle.api.request_validator import TranslateFriendlyTypesRequestValidator
from vkbottle.api.response_validator.abc import ABCResponseValidator
from vkbottle.api.request_validator.abc import ABCRequestValidator

from vkbottle.api.http.aiohttp import SingleAiohttpClient
from vkbottle.api.http.abc import ABCHTTPClient

from vkbottle.exception_factory.base_exceptions import CaptchaError
from vkbottle.modules import logger


DEFAULT_REQUEST_VALIDATORS = (
    TranslateFriendlyTypesRequestValidator(),
)

DEFAULT_RESPONSE_VALIDATORS = (
    JSONResponseValidator(BlockingRequestRescheduler()),
    VKAPIErrorResponseValidator(),
)


CaptchaHandler = Callable[[CaptchaError], Awaitable]


class APIRequest(NamedTuple):
    method: str
    data: dict


class API(ABCAPI):
    """
    Default API instance
    Documentation: https://vkbottle.rtfd.io/ru/latest/low-level/api
    """
    __api_url__: str = API_URL
    __api_version__: str = API_VERSION

    def __init__(
        self,
        token: Token,
        ignore_errors: bool = False,
        http_client: Optional[ABCHTTPClient] = None,
        captcha_handler: Optional[CaptchaHandler] = None,
        response_validators: Sequence[ABCResponseValidator] = DEFAULT_RESPONSE_VALIDATORS,
        request_validators: Sequence[ABCRequestValidator] = DEFAULT_REQUEST_VALIDATORS
    ):
        self.token_generator = get_token_generator(token)
        self.ignore_errors = ignore_errors
        self.http_client = http_client or SingleAiohttpClient()
        self.response_validators = response_validators
        self.request_validators = request_validators
        self.captcha_handler = captcha_handler

    async def request(self, method: str, data: dict) -> dict:
        """Makes a single request opening a session"""
        data = await self.validate_request(data)

        async with self.token_generator as token:
            response = await self.http_client.request_text(
                self.__api_url__ + method,
                method="POST",
                data=data,
                params={"access_token": token, "v": self.__api_version__},
            )
        logger.debug("Request {} with {} data returned {}", method, data, response)
        return await self.validate_response(method, data, response)

    async def request_many(self, requests: Sequence[APIRequest]) -> AsyncIterator[dict]:
        """Makes many requests opening one session"""
        for request in requests:
            method, data = request.method, await self.validate_request(request.data)
            async with self.token_generator as token:
                response = await self.http_client.request_json(
                    self.__api_url__ + method,
                    method="POST",
                    data=data,
                    params={"access_token": token, "v": self.__api_version__},
                )
            logger.debug("Request {} with {} data returned {}", method, data, response)
            yield await self.validate_response(method, data, response)

    async def validate_response(
        self, method: str, data: dict, response: Union[dict, str]
    ) -> Any:
        """Validates response from VK,
        to change validations change API.response_validators (list of ResponseValidator's)"""
        for validator in self.response_validators:
            response = await validator.validate(
                ctx_api=self, method=method, data=data, response=response
            )
        logger.debug("API response was validated")
        return response

    async def validate_request(self, request: dict) -> dict:
        """Validates requests from VK,
        to change validations change API.request_validators (list of RequestValidator's)"""
        for validator in self.request_validators:
            request = await validator.validate(request=request)
        logger.debug("API request was validated")
        return request

    def __repr__(self) -> str:
        return f"<API token_generator={self.token_generator}...>"
