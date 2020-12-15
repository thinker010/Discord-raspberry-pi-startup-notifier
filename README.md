# Discord-raspberry-pi-startup-notifier
This project is about how to send any kind of notification(here, raspberry pi start up notification) in discord channel through discord webhooks when raspberry pi boots up(after entering desktop).


# Requirements
1. Raspberry Pi with an Internet connection.
2. python3: `sudo apt install python3`
3. pip3: `sudo apt-get install python3-pip`
4. discord.py: `sudo pip3 install discord`
5. discord_webhooks.py: `sudo pip3 install discord-webhooks`
6. requests: `sudo pip3 install requests`

**HOW TO GET YOUR DISCORD WEBHOOK URL(NEEDED):**

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks


# Procedure

For Pi's with monitor:-

  1. First download the repo using the command `git clone https://github.com/thinker010/Discord-raspberry-pi-startup-notifier.git` in terminal.
  2. Then copy the `main.desktop` file and paste it in here `/etc/xdg/autostart`.
  3. Then paste the `main.py` to the pi folder at `/home/pi`.
  4. Now in `main.py`, Replace ['`YOUR DISCORD WEBHOOK URL`'](https://github.com/thinker010/Discord-raspberry-pi-startup-               notifier/blob/a6c1aa99d43b6c33258f546bdc98eb42bb3f1119/main.py#L3)(keeping the single quotes) with [your Discord channel webhook URL](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). 
  5. You can set a custom message in the [content variable](https://github.com/thinker010/Discord-raspberry-pi-startup- notifier/blob/a6c1aa99d43b6c33258f546bdc98eb42bb3f1119/main.py#L3)(keeping the single quotes).
  6. Now go to the terminal and make the python file executable by typing `sudo chmod +x main.py` in `/home/pi`.
  
  For pi's without monitor:
  
  Use [cp command](https://www.raspberrypi.org/documentation/linux/usage/commands.md) and, copy and paste the files in places mentioned above


# Procedure All in CLI(Use this to copy and paste the commands directly while watching)
<a href="https://asciinema.org/a/GE5SdBMJIRsjL4dGEH23v6Vb8" target="_blank"><img src="https://asciinema.org/a/GE5SdBMJIRsjL4dGEH23v6Vb8.svg" /></a>

# Troubleshooting
1. If its not working try updating python3 `sudo apt install python3` again.
2. Dont try executing the `main.py` file on terminal before making it an executable file, do it by doing the 6th line of procedure or you can try it on thonny editor to check if it sends the message on Discord.


Hoping this was helpful.:)


# Source

https://pypi.org/project/discord-webhook/

https://www.hackster.io/kamal-khan/desktop-shortcut-for-python-script-on-raspberry-pi-fd1c63
