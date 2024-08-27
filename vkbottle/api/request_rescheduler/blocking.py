from time import sleep as blocking_sleep
from typing import Any

from vkbottle.api.request_rescheduler.abc import ABCRequestRescheduler
from vkbottle.modules import logger
from vkbottle.api.abc import ABCAPI


DEFAULT_DELAY = 5


class BlockingRequestRescheduler(ABCRequestRescheduler):

    def __init__(self, delay: int = DEFAULT_DELAY):
        self.delay = delay

    async def reschedule(
        self,
        ctx_api: ABCAPI,
        method: str,
        data: dict,
        response: Any,
    ) -> dict:
        logger.debug(
            "Usage of blocking rescheduler is assumed when VK doesn't respond to "
            "all requests for an amount of time. Starting..."
        )

        attempt_number = 1
        while not isinstance(response, dict):
            logger.info("Attempt number {}. Making request...", attempt_number)
            blocking_sleep(self.delay * attempt_number)  # noqa: ASYNC101
            response = await ctx_api.request(method, data)
            attempt_number += 1
            logger.debug("Attempt succeed? - {}", isinstance(response, dict))

        logger.info("Finally succeed after {} seconds", self.delay * attempt_number)
        return response
