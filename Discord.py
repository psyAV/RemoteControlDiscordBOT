import sys
import traceback
import discord
from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import Bot
import platform
from modules import camera_module, \
    information_module, \
    restart_module, \
    kill_process_module, \
    screenshot_module, \
    shutdown_module, \
    cmd_module, \
    update_module,\
    file_module


class BotConfig:
    help_list = ""

    def __init__(self, token, prefix, version, python_version, admin):
        self.token = token
        self.prefix = prefix
        self.version = version
        self.python_version = python_version
        self.admin_id = admin


# Set up configuration file
try:
    with open("config") as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            elif "token" in line:
                _token = str(line.replace(" ", ""))[6:]
            elif "prefix" in line:
                _prefix = str(line.replace(" ", ""))[7:]
            elif "version" in line:
                _version = str(line.replace(" ", ""))[8:]
            elif "admin_id" in line:
                _admin = str(line.replace(" ", ""))[9:]
    config = BotConfig(_token, _prefix, _version, platform.python_version(), _admin)
except FileNotFoundError:
    print("Configuration file not found...\nLeaving the program")
    sys.exit()

# Create bot client with description and command prefix
client = Bot(description="Amadus remote control", command_prefix="/")
client.remove_command("help")


async def checkAdmin(ctx):
    if str(ctx.author.id) == str(config.admin_id):
        return True
    else:
        await critical(ctx, "Permission Denied", f"{ctx.author} must have admin permission to perform this command")


async def embed(ctx, title, description, colour, fields: list, channel=None):
    """
    Description: creates and embed with title, description and fields (at least 2)
    """
    _embed = Embed(title=title, description=description, colour=colour)
    for count, field in enumerate(fields):
        _embed.add_field(name=field[count][0], value=field[count][1], inline=field[2])
    if not channel:
        await ctx.channel.send(embed=_embed)
    else:
        await channel.send(embed=_embed)


async def critical(ctx, title, description):
    """
    Description: send a message on warnig channel
    """
    channel = client.get_channel(833068265257304075)
    await embed(ctx, title, description, Colour.red(), [], channel)


@client.event
async def on_ready():
    print("\n--------------------------------------Discord Remote Control BOT console by AV--------------------------------------\n\n"
          f"Logged in as {client.user.name} (ID: {str(client.user.id)})\n\n | Connected to "
          f"{str(len(client.guilds))} servers\n | Connected to {str(len(set(client.get_all_members())))} users"
          f"\n | Current Discord.py Version: {config.version} | Current Python Version: {config.python_version}")
    return await client.change_presence(activity=discord.Game(name="remote control"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        pass
    else:
        print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        await critical(ctx, "Command Error", f"{error}")


@client.command()
@commands.check(checkAdmin)
async def update(ctx):
    """
    Module: update
    Description: Update Discord.py or a module in ./modules
    Usage: /update or /update moduleToUpdate
    """
    await critical(ctx, "Update", "Updating Discord.py")
    await update_module.update(ctx, client.get_channel(833068265257304075))


@client.command()
@commands.check(checkAdmin)
async def cmd(ctx, command):
    """
    Module: cmd
    Description: Use cmd commands
    Usage: /cmd command
    """
    await cmd_module.cmd(ctx, command)


@client.command()
@commands.check(checkAdmin)
async def shutdown(ctx, seconds=0):
    """
    Module: shutdown
    Description: Shuts system down
    Usage: /shutdown or /shutdown secondsToShutdown
    """
    await critical(ctx, "Critical command executed", "/shutdown")
    await shutdown_module.shutdown(ctx, seconds)


@client.command()
@commands.check(checkAdmin)
async def restart(ctx, seconds=0):
    """
    Module: restart
    Description: Restarts system
    Usage: /restart or /restart secondsToRestart
    """
    await critical(ctx, "Critical command executed", "/restart")
    await restart_module.restart(ctx, seconds)


@client.command()
@commands.check(checkAdmin)
async def clear(ctx, amount=1):
    """
    Module: clear
    Description: delete previous messages
    Usage: /clear or /clear amount to clear a specified amount of messages
    """
    channel = client.get_channel(832928115239288846)
    await channel.purge(limit=amount + 1)


@client.command()
@commands.check(checkAdmin)
async def kill(ctx, process, minutes=0):
    """
    Module: kill
    Description: kill a specified process
    Usage: /kill "Process Name" or /kill "Process Name" minutesToQuit
    """
    await critical(ctx, "Critical command executed", f"/kill {process} {minutes}")
    await kill_process_module.kill(ctx, process, minutes)


@client.command()
async def ping(ctx):
    """
    Module: ping
    Description: Give the latency in milliseconds
    Usage: /ping
    """
    await embed(ctx, "Ping", f"Pong! {round(client.latency * 1000)}ms", Colour.green(), [])


@client.command()
async def screenshot(ctx, seconds=0):
    """
    Module: screenshot
    Description: Takes a screenshot and sends it back
    Usage: /screenshot or /screenshot secondsToScreenshot
    """
    await screenshot_module.screenshot(ctx, seconds)


@client.command()
async def info(ctx):
    """
    Module: info
    Description: Gives system information, cpu, ram, disk
    Usage: /info
    """
    await information_module.system_information(ctx, round(client.latency * 1000))


@client.command()
async def media(ctx, command, times=1):
    """
    Module: media
    Description: Controls Media Features
    Usage: /media command or /media command times
    """
    await media_module.media(ctx, command, times)



@client.command()
async def camera(ctx, command, time=5):
    """
    Module: camera
    Description: Records a video or takes a photo (no audio)
    Usage: /camera command time
    """
    await camera_module.camera(ctx, command, time)


@client.command()
async def file(ctx, command, *args):
    """
    Module: file
    Description: Allows file download, upload and system navigation
    Usage: /file file_name [command] [[path]|[times]]
    """
    await file_module.file(ctx, command, *args)


@client.command()
async def help(ctx):
    """
    Module: help
    Description: Display a list with all the commands, warning commands are not included
    Usage: /help
    """
    for command in client.all_commands:
        BotConfig.help_list = f"{BotConfig.help_list}/{command}\n"
    await embed(ctx, "Help", f"Command list:\n{BotConfig.help_list}", Colour.blue(), [])


if __name__ == "__main__":
    client.run(config.token)
