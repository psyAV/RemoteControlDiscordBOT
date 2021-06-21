import os
import asyncio
from sys import platform
from Discord import critical


async def kill(ctx, process, minutes=0):
    """
    Module: appQuitter
    Description: Quits the application
    Usage: /kill "Process Name" or /kill "Process Name" minutesToQuit
    Dependencies: time, os, sys.platform
    """
    await ctx.send("Terminating {0} process".format(process.upper()))
    minutes = minutes*60

    if minutes != 0:
        await asyncio.sleep(minutes)

    if platform == "win32":
        os.system("taskkill /F /IM {0}.exe".format(process))
    elif platform == "linux" or platform == "linux2":
        os.popen("pkill -f {0}".format(process))
    else:
        await critical(ctx, "Error", "Can't kill the process.")
        await asyncio.sleep(3)
