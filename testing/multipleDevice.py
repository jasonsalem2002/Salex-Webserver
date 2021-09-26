from tabulate import tabulate
from random import choice
from operator import itemgetter
import string

devices = []

for i in range(10):
    device = dict()

    device["name"] = (
        choice(["r1", "r2", "r3", "r4"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    device["vendor"] = (choice(["Apple", "Samsung", "Google"]))

    if device["vendor"] == "Apple":
        device["os"] = choice(["IOS 14.0", "IOS 13.0", "IOS 15.0"])
    elif device["vendor"] == "Samsung":
        device["os"] = choice(["Home UI 1.0", "Home UI 2.0", "Home UI 3.0"])
    elif device["vendor"] == "Google":
        device["os"] = choice(["Pixel OS 17.0", "Pixel OS 18.0", "Pixel OS 19.0"])

    device["IP Address"] = "192.168.1." + str(i)

    devices.append(device)

print(tabulate(sorted(devices, key=itemgetter("vendor", "os")), headers="keys"))