import time
import asyncio
import async_timeout
import os, time, platform, re
import subprocess
import psutil, datetime
import cpuinfo
import traceback

from random import *
from uptime import *
from pyrogram import Client, filters

api_id = ""
api_hash = ""

app = Client("account", api_id, api_hash)

@app.on_message(filters.regex("инфа о системе"))
async def info(client, message):
    await asyncio.sleep(1)
    await message.edit_text("Начинается магия 😁")
    try:
        osname = os.uname().sysname 
    except:
        pass
    try:
        osarch = os.uname().machine
    except:
        pass
    try:
        osrelease = os.uname().release
    except:
        pass
    try:
        ospython = platform.python_version()
    except:
        pass
    try:
        diskused = psutil.disk_usage("/.").used / (1024 ** 3)
        disku = round(diskused, 1)
    except:
        pass
    try:
        disktotal = psutil.disk_usage("/.").total / (1024 ** 3)
        diskb = round(disktotal, 1)
    except:
        pass
    try:
        diskper = psutil.disk_usage("/.").percent
    except:
        pass
    try:
        time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d.%m.%Y %H:%M:%S")
    except:
        pass
    try:
        cpu = psutil.cpu_count(logical=True)
        loadcpu = psutil.cpu_percent(interval=1, percpu=True)
    except:
        pass
    try:
        useed_m = round(psutil.virtual_memory().used / 1024 ** 2)
        tot_m = round(psutil.virtual_memory().total / 1024 ** 2)
        used_m = round(useed_m, 2)
    except:
        pass
    try:
        now = datetime.datetime.now()
        timeserv = now.strftime("%d.%m.%Y %H:%M:%S")
    except:
        pass
    try:
        upt = uptime() / 60 ** 2
        up = round(upt, 1)
    except:
        pass
    try:
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ\n• Время последнего рестарта:""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ\n• Время последнего рестарта:\n> {time}""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ\n• Время последнего рестарта:\n> {time}\n• Время работы сервера:""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ\n• Время последнего рестарта:\n> {time}\n• Время работы сервера:\n> {up} ч.""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ\n• Время последнего рестарта:\n> {time}\n• Время работы сервера:\n> {up} ч.\n• Время на сервере:""")
        await asyncio.sleep(0.05)
        await message.edit_text(f"""🖥Информация о системе:\n• OC: {osname}\n• Arch: {osarch}\n• Release: {osrelease}\n• Python: {ospython}\n___________________________\n⚙Информация о железе:\n• Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}\n• Загрузка CPU: {loadcpu}% [{cpu}]\n• Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]\n• RAM: {useed_m}МБ / {tot_m}МБ\n• Время последнего рестарта:\n> {time}\n• Время работы сервера:\n> {up} ч.\n• Время на сервере:\n> {timeserv}""")
    except:
        pass


@app.on_message(filters.regex("пинг"))
async def ping(client, message):
    start = time.time()
    await message.edit_text("...")
    delta_ping = time.time() - start
    await message.edit_text(f"**Pong!** `{delta_ping * 1000:.3f} ms`")


app.run()