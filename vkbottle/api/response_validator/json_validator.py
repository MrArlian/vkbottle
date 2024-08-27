import contextlib

from typing import Any, Optional

from vkbottle.api.request_rescheduler.abc import ABCRequestRescheduler
from vkbottle.api.response_validator.abc import ABCResponseValidator
from vkbottle.modules import json, logger
from vkbottle.api import ABCAPI


class JSONResponseValidator(ABCResponseValidator):
    """Default response json-parse validator
    Documentation: https://vkbottle.rtfd.io/ru/latest/low-level/api/response-validator
    """

    def __init__(
        self,
        rescheduler: ABCRequestRescheduler,
        context: Optional[dict] = None
    ):
        self.rescheduler = rescheduler
        self.context = context or {}

    async def validate(
        self,
        ctx_api: ABCAPI,
        method: str,
        data: dict,
        response: Any,
    ) -> Any:
        if isinstance(response, dict):
            return response
        elif isinstance(response, str):
            with contextlib.suppress(ValueError):
                return json.loads(response)

        if self.context.get("reschedule"):
            return None

        logger.info(
            "VK returned object of invalid type ({}). Request will be rescheduled with {}",
            type(response).__name__,
            self.rescheduler.__class__.__name__,
        )
        self.context["reschedule"] = True
        response = await self.validate(
            method,
            data,
            await self.rescheduler.reschedule(ctx_api, method, data, response),
            ctx_api,
        )
        self.context.pop("reschedule")
        return response
