import os
import asyncio


async def cmd(ctx, command):
    """
    Module: cmd
    Description: Executes cmd command
    Usage: !cmd "command"
    Dependencies: time, os
    """
    await ctx.send("Executing in command prompt: " + command)
    command_result = os.popen(command).read()
    await ctx.send(command_result)
    await asyncio.sleep(3)
