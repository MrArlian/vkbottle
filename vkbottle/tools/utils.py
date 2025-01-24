import asyncio
import importlib
import os
import re
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING, Any, Coroutine, Iterator, TypeVar

from vkbottle.modules import logger


T = TypeVar("T")


# This feature is not used in production
# but can be useful for customization
# purposes
def run_in_task(coroutine: Coroutine) -> asyncio.Task:
    """Gets loop and runs add makes task from the given coroutine"""
    loop = asyncio.get_running_loop()
    return loop.create_task(coroutine)


def run_sync(coroutine: Coroutine[Any, Any, T]) -> T:
    return ThreadPoolExecutor().submit(asyncio.run, coroutine).result()
