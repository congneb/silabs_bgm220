import asyncio
from bleak import BleakScanner
import re


from bleak import BleakClient

MODEL_NBR_UUID = "2A01"

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        mac_pattern = r'(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})'
        mac_addresses = re.findall(mac_pattern, str(d))
        # print(mac_addresses)
        try:
            async with BleakClient(str(mac_addresses)) as client:
                model_number = await client.read_gatt_char(MODEL_NBR_UUID)
                print("Model Number: {0}".format("".join(map(chr, model_number))))
        except:
            print("Error")

asyncio.run(main())
