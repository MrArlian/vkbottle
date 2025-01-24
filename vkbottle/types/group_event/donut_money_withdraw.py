from ..base import VkObject


class DonutMoneyWithdraw(VkObject):
    amount: float
    amount_without_fee: float
