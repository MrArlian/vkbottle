from enum import StrEnum


class OrderStatus(StrEnum):
    """ Order status """

    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"
