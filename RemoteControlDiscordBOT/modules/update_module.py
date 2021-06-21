import os
from discord import Embed, Colour


async def update(ctx, channel):
    cwd = os.getcwd()
    if "Updater.py" in cwd:
        os.chdir(f"{cwd[:-7]}")
    try:
        _file = ctx.message.attachments[0]
        await _file.save(fr"{cwd}\updates\new\{_file.filename}")
        if _file.filename != "Discord.py":
            os.chdir(f"{cwd}/updates")
            os.system(f"python Updater.py module")
        else:
            os.chdir(f"{cwd}/updates")
            os.system(f"python Updater.py main")
    except IndexError:
        embed = Embed(
            title="Attachment error",
            description="/update attachment is missing",
            colour=Colour.red()
        )
        await channel.send(embed=embed)
