# -*- coding: utf-8 -*-
"""
Notifications
-------------
Example showing how to add notifications to a characteristic and handle the responses.
Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>
"""

import logging
import asyncio
import platform
import color_test

from bleak import BleakClient
from bleak import _logger as logger

# set your uuid and address
MODEL_NBR_UUID = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
address = 'xx:xx:xx:xx:xx:xx'

CHARACTERISTIC_UUID = "AADC"  # <--- Change to the characteristic you want to enable notifications from.


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    value_hex = bytes(data).hex()
    print("{0}: {1}".format(sender, value_hex))
    color_test.set_data(value_hex)


async def run(address, loop, debug=False):
    if debug:
        import sys

        # loop.set_debug(True)
        l = logging.getLogger("asyncio")
        l.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        l.addHandler(h)
        logger.addHandler(h)

    async with BleakClient(address, loop=loop, timeout=10) as client:
        x = await client.is_connected()
        logger.info("Connected: {0}".format(x))

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        while True:
            await asyncio.sleep(3000, loop=loop)

        # await client.stop_notify(CHARACTERISTIC_UUID)


if __name__ == "__main__":
    import os

    os.environ["PYTHONASYNCIODEBUG"] = str(1)
    address = (
        address
        if platform.system() != "Darwin"
        else MODEL_NBR_UUID
    )
    loop = asyncio.get_event_loop()

    loop.run_until_complete(run(address, loop, True))
    loop.run_forever()
