import asyncio
import platform

from bleak import BleakClient

MODEL_NBR_UUID = '50430B3B-0437-485E-8D91-3862CE188C31'
address = 'db:d4:9e:88:24:c2'

import platform
import asyncio
import logging

from bleak import BleakClient


async def run(address, loop, debug=False):
    log = logging.getLogger(__name__)
    if debug:
        import sys

        loop.set_debug(True)
        log.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        log.addHandler(h)

    async with BleakClient(address, loop=loop, timeout=10) as client:
        x = await client.is_connected()
        log.info("Connected: {0}".format(x))

        for service in client.services:
            log.info("[Service] {0}: {1}".format(service.uuid, service.description))
            for char in service.characteristics:
                if "read" in char.properties:
                    try:
                        value = bytes(await client.read_gatt_char(char.uuid))
                    except Exception as e:
                        value = str(e).encode()
                else:
                    value = None

                value_hex = ''
                if value is not None:
                    value_hex = value.hex()

                log.info(
                    "\t[Characteristic] {0}: ({1}) | Name: {2}, Value: {3} {4}".format(
                        char.uuid, ",".join(char.properties), char.description, value, value_hex
                    )
                )
                for descriptor in char.descriptors:
                    value = await client.read_gatt_descriptor(descriptor.handle)
                    value_hex = ''
                    if value is not None:
                        value_hex = value.hex()

                    log.info(
                        "\t\t[Descriptor] {0}: (Handle: {1}) | Value: {2} {3}".format(
                            descriptor.uuid, descriptor.handle, bytes(value), value_hex
                        )
                    )
        print('----')
        for service in client.services:
            log.info("[Service] {0}: {1}".format(service.uuid, service.description))
            for char in service.characteristics:
                if "read" in char.properties:
                    try:
                        value = bytes(await client.read_gatt_char(char.uuid))
                    except Exception as e:
                        value = str(e).encode()
                else:
                    value = None

                value_hex = ''
                if value is not None:
                    value_hex = value.hex()

                log.info(
                    "\t[Characteristic] {0}: ({1}) | Name: {2}, Value: {3} {4}".format(
                        char.uuid, ",".join(char.properties), char.description, value, value_hex
                    )
                )
                for descriptor in char.descriptors:
                    value = await client.read_gatt_descriptor(descriptor.handle)
                    value_hex = ''
                    if value is not None:
                        value_hex = value.hex()

                    log.info(
                        "\t\t[Descriptor] {0}: (Handle: {1}) | Value: {2} {3}".format(
                            descriptor.uuid, descriptor.handle, bytes(value), value_hex
                        )
                    )



if __name__ == "__main__":
    address = (
        address
        if platform.system() != "Darwin"
        else MODEL_NBR_UUID
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop, True))

