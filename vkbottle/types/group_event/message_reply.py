import json

from typing import Callable, Optional, Union, Dict, Any

from ..object.messages import Message


class MessageReply(Message):

    def get_payload_json(
        self,
        throw_error: bool = False,
        unpack_failure: Callable[..., Any] = lambda payload: payload,
    ) -> Optional[Union[Dict[str, Any], Any]]:
        """
            ...
        """
        if self.payload is None:
            return
        try:
            return json.loads(self.payload)
        except (ValueError, TypeError) as e:
            if throw_error:
                raise e from e
        return unpack_failure(self.payload)
