from enum import Enum


class DeliveryStatus(Enum):
    PREPARING = 0
    SHIPPED = 1
    DELIVERED = 2
    CONFIRMED = 3

    def getStringValue(x):
        value_to_string = {
            0: 'Preparing',
            1: 'Shipped',
            2: 'Delivered',
            3: 'Confirmed'
        }

        return value_to_string[x]
