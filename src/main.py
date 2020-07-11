#!/usr/bin/python3


# import bluetooth
# from bluetooth.ble import DiscoveryService


# simple inquiry example
# import bluetooth


import asyncio
from bleak import discover
from bleak import BleakClient
from bleak.backends.service import BleakGATTServiceCollection

my_cube_name = 'GiS92866'

#
# data = b"\xdb\xd4\x9e\x88$\xc2\x0c'\x00\t"
#
# print(data.hex())
#
# exit()


MODEL_NBR_UUID = '50430B3B-0437-485E-8D91-3862CE188C31'
address = 'db:d4:9e:88:24:c2'

# async def run(address, loop):
#     async with BleakClient(address, loop=loop) as client:
#         model_number = await client.read_gatt_char(MODEL_NBR_UUID)
#         print("Model Number: {0}".format("".join(map(chr, model_number))))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run(address, loop))
#
# exit()


loop = asyncio.get_event_loop()


# def connect(uuid, mac_address):
#     async def run(mac_address, loop):
#         async with BleakClient(mac_address, loop=loop) as client:
#             model_number = await client.read_gatt_char(uuid)
#             print("Model Number: {0}".format("".join(map(chr, model_number))))
#
#
#     loop.run_until_complete(run(mac_address, loop))


async def run():
    devices = await discover()
    for d in devices:
        if my_cube_name == d.name:
            print(d)
            print('name is :', d.name)
            print(d.address, d.metadata)
            if 'manufacturer_data' in d.metadata:
                for key, value in d.metadata['manufacturer_data'].items():
                    print(key, value)
                    print(value.hex())
                    # just in mac os
                    uuid = d.address
                    mac_address_data = value.hex()[0:12]
                    mac_address = mac_address_data[0:2] \
                                  + ':' + mac_address_data[2:4] \
                                  + ':' + mac_address_data[4:6] \
                                  + ':' + mac_address_data[6:8] \
                                  + ':' + mac_address_data[8:10] \
                                  + ':' + mac_address_data[10:12]

                    print('uuid is: ', uuid)
                    print('mac address is: ', mac_address)
                    # connect(uuid, mac_address)
                    client = BleakClient(mac_address, loop=loop)

                    # model_number = await client.read_gatt_char(str(uuid))
                    #
                    # print(model_number)

                    # print(client.get_services())

                    bleakServices = await client.get_services()

                    print(bleakServices.services)

                    # print("Model Number: {0}".format("".join(map(chr, model_number))))


loop.run_until_complete(run())

# def scan():
#     nearby_devices = bluetooth.discover_devices(lookup_names=True)
#     print("Found {} devices.".format(len(nearby_devices)))
#
#     for addr, name in nearby_devices:
#         print("  {} - {}".format(addr, name))
#
# def main():
#     scan()
#
#
#
# if __name__ == '__main__':
#     main()
