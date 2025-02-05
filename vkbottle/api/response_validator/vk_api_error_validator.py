from typing import Any

from vkbottle.exception_factory import CaptchaError, VKAPIError
from vkbottle.modules import logger

from vkbottle.api.response_validator.abc import ABCResponseValidator
from vkbottle.modules import logger
from vkbottle.api.abc import ABCAPI


class VKAPIErrorResponseValidator(ABCResponseValidator):
    """Default vk api error response validator
    Documentation: https://vkbottle.rtfd.io/ru/latest/low-level/api/response-validator
    """

    async def validate(
        self,
        ctx_api: ABCAPI,
        method: str,
        data: dict,
        response: Any
    ) -> Any:
        if "error" not in response:
            if "response" not in response:
                request_params = [{"key": key, "value": value} for key, value in data.items()]
                raise VKAPIError[1](
                    error_msg=f"Unknown response from {method}: {response}",
                    request_params=request_params,
                )
            if isinstance(response["response"], list) and any(
                "error" in item for item in response["response"]
            ):
                logger.info("API error(s) in response wasn't handled: {}", response["response"])
            return response

        if ctx_api.ignore_errors:
            return None
        error = response["error"]
        code = error.pop("error_code")

        if VKAPIError[code] is CaptchaError and ctx_api.captcha_handler:
            key = await ctx_api.captcha_handler(CaptchaError(**error))
            return await ctx_api.request(
                method, {**data, "captcha_sid": error["captcha_sid"], "captcha_key": key}
            )

        raise VKAPIError[code](**error)
