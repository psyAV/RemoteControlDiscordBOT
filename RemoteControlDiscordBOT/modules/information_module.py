import platform
import psutil
from time import time
from datetime import timedelta
from psutil import Process, virtual_memory
from discord import Embed, Colour


async def system_information(ctx, latency):
    """
    Module: info
    Description: Gives system information, cpu, ram, disk
    Usage: /info
    Dependencies: datetime, timedelta, psutil, platform
    """
    proc = Process()
    uptime = timedelta(seconds=time() - proc.create_time())
    mem_total = virtual_memory().total / (1024 ** 2)
    mem_of_total = proc.memory_percent()
    mem_usage = mem_total * (mem_of_total / 100)
    embed = Embed(title="SYSTEM INFORMATION",
                  description=f"Uptime: {uptime}",
                  colour=Colour.orange())
    fields = [
        ("Python version", platform.python_version(), False),
        ("Uptime", timedelta(seconds=time()-proc.create_time()), False),
        ("CPU:", f"{psutil.cpu_percent()}%", True),
        ("RAM:", f"{psutil.virtual_memory().percent}%", True),
        ("Memory usage", f"{mem_usage:,.3f} / {mem_total:,.0f} MiB ({mem_of_total:.0f}%)", False)]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    embed.set_footer(text=f"latency: {latency}ms")
    await ctx.send(embed=embed)
