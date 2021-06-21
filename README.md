# RemoteControlDiscordBOT
A cross platform discord bot to control your pc remotely and an update tool to upload new modules and functionalities
## Requirements:
* Python 3
* discord.py
* requests
* psutil
* pynput
* opencv-python
* mss
## Feature list and usage:
* /help ==> "Display a list with all the commands"
* /file ==> "Allows file download, upload and system navigation"
* /media {command} {time} ==> "Controls Media Features"
* /restart {secondsToRestart} ==> "Restart the system"
* /shutdown {secondsToShutdown} ==> "Shuts system down"
* /kill {ProcessName} {minutesToQuit} ==> "kill a specified process"
* /camera {action} {time} ==> "Records a video or takes a photo (no audio)"
* /screenshot {secondsToScreenshot} ==> "Takes a screenshot and sends it back"
* /info ==> "Gives system information, cpu, ram..."
* /cmd {command} ==> Execute console commands
* /update {moduleToUpdate} ==> "Replace Discord.py or add modules in ./modules, old file are stored in ./update/old directory"
* /ping ==> "Return the bot latency in milliseconds"
* /clear {amount} ==> "delete previous messages"
## Installation:
1. Install Python 3.5 or higher
2. Create a bot and get its token and then get your channel ID and your user ID
3. Create a warning channel to print the logs
4. Download the resository and replace the config file with your personal data
5. Edit Discord.py and replace client.get_channel(your warning channel ID)
6. Launch Discord.py
