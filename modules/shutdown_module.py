import time
import os
import asyncio
from sys import platform


async def shutdown(ctx, seconds=0):
    """
    Module: shutdown
    Description: Shuts system down
    Usage: !shutdown or !shutdown secondsToShutdown
    Dependencies: time, os
    """
    await ctx.send("Shutting system down.")
    if platform == "win32":
        if seconds != 0:
            time.sleep(seconds)
        os.system("Shutdown.exe -s -t 0")
    elif platform == "linux" or platform == "linux2":
        if seconds != 0:
            time.sleep(seconds)
        os.system("sudo shutdown")
    else:
        await ctx.send(ctx, "Can't shutdown system.")
        await asyncio.sleep(3)
