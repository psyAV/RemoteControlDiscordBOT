import os
import discord


async def camera(ctx, command, time=5):
    """
    Module: camera
    Description: Records a video or takes a photo (no audio)
    Usage: /camera command time
    Dependencies: cv2, datetime, timedelta
    """
    cwd = os.getcwd()
    photo_count = len(os.listdir(fr"{cwd}\media\photo"))
    video_count = len(os.listdir(fr"{cwd}\media\video"))
    await ctx.send("Recording!")

    if command == "photo":
        os.system(f"python lib/camera_control.py photo")
        try:
            await ctx.send(file=discord.File(fr"{cwd}\media\photo{photo_count}.jpg"))
        except:
            await ctx.send(file=discord.File(fr"{cwd}\media\photo.jpg"))

    if command == "video":
        os.system(f"python3 lib/camera_control.py video {time}")
        try:
            await ctx.send(file=discord.File(fr"{cwd}\media\video\video{video_count}.mp4"))
        except:
            await ctx.send(file=discord.File(fr"{cwd}\media\video\video.mp4"))
