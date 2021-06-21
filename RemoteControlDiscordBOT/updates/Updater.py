import os
import shutil
import sys


def test():
    pass


def update(module_type):
    cwd = os.getcwd()
    updates = os.listdir(fr"{cwd}\new")
    old = os.listdir(fr"{cwd}\old")
    modules = os.listdir(f"{cwd[:-7]}/modules")
    if module_type == "main" and "Discord.py" in updates:
        os.rename(f"{cwd[:-7]}/Discord.py", f"{str(len(old))}.py")
        shutil.move(fr"{cwd}\{str(len(old))}.py", f"{cwd}/old")
        shutil.move(f"{cwd}/new/Discord.py", f"{cwd[:-7]}")
    elif module_type == "module":
        for file_py in updates:
            if file_py == "Discord.py":
                updates.remove("Discord.py")
        for module in updates:
            if module in modules:
                os.rename(f"{cwd[:-7]}/modules/{module}", f"{str(len(old))}m.py")
                shutil.move(fr"{cwd}\{str(len(old))}m.py", f"{cwd}/old")
                shutil.move(f"{cwd}/new/{module}", f"{cwd[:-7]}/modules")
            else:
                shutil.move(f"{cwd}/new/{module}", f"{cwd[:-7]}/modules")
    os.chdir(f"{cwd[:-7]}")
    os.system(fr"python Discord.py")


function = sys.argv[1]
if function == "main":
    update("main")
if function == "module":
    update("module")
if function == "test":
    test()
