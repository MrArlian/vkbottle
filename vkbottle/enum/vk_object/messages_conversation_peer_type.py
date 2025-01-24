from enum import StrEnum


class MessagesConversationPeerType(StrEnum):
    """ Peer type """

    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"
