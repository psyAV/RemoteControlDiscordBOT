import time
import os
import discord
from mss import mss


async def screenshot(ctx, seconds=0):
    """
    Module: screenshot
    Description: Takes a screenshot and sends it back
    Usage: /screenshot or /screenshot secondsToScreenshot
    Dependencies: time, os, mss
    """
    cwd = os.getcwd()
    file_count = len(os.listdir(fr"{cwd}\media\screenshot")) + 1
    await ctx.send("Taking a screenshot.")
    if time != 0:
        time.sleep(seconds)
    with mss() as sct:
        filename = sct.shot(mon=-1, output=fr"{cwd}\media\screenshot\screenshot{file_count}.png")
    try:
        await ctx.send(file=discord.File(fr"{cwd}\media\screenshot\screenshot{file_count}.png"))
    except:
        await ctx.send(file=discord.File(fr"{cwd}\media\screenshot\screenshot.png"))
