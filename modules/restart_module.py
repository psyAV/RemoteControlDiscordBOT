import time
import os
from sys import platform


async def restart(ctx, seconds=0):
    """
    Module: restart
    Description: Restarts system
    Usage: /restart or /restart secondsToRestart
    Dependencies: time, os, sys.platform
    """
    await ctx.send("Restarting system.")
    if platform == "win32":
        if time != 0:
            time.sleep(seconds)
        os.system("Shutdown.exe -r")
    elif platform == "linux" or platform == "linux2":
        if time != 0:
            time.sleep(seconds)
        os.system("sudo reboot")
    else:
        await ctx.send(ctx, "Can't restart system.")
