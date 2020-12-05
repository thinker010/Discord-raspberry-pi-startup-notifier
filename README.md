# Discord-raspberry-pi-startup-notifier
This project is about how to send any kind of notification in discord channel through discord webhooks when raspberry pi boots up(after entering desktop).


# Requirements
1. python3: `sudo apt install python3`
2. pip3: `sudo apt-get install python3-pip`
3. discord.py: `sudo pip3 install discord`
4. discord_webhooks.py: `sudo pip3 install discord-webhooks`
5. requests: `sudo apt install requests`

**HOW TO GET YOUR DISCORD WEBHOOK URL(NEEDED):**

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks


# Preperation

1. First download the repo using the command `git clone https://github.com/thinker010/Discord-raspberry-pi-startup-notifier.git` in terminal.
2. Then copy the `main.desktop` file and paste it in here `/etc/xdg/autostart`.
3. Then paste the `main.py` to the pi folder at `/home/pi`.
4. Now in `main.py`, Replace '`YOUR DISCORD WEBHOOK URL`'(keeping the single quotes) with [your Discord channel webhook URL](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). 
5. You can set a custom message in the content variable(keeping the single quotes).
6. Now go to the terminal and make the python file executable by typing `sudo chmod +x main.py` in `/home/pi`.



# Troubleshooting:
1. If its not working try updating python3 `sudo apt install python3` again
2. Dont try it on terminal because it doesnt work on terminal but u can try it on thonny editor or complete the whole process and check if it sends the message


Hoping this was helpful.:)


# Source: 

https://pypi.org/project/discord-webhook/
        
   https://www.hackster.io/kamal-khan/desktop-shortcut-for-python-script-on-raspberry-pi-fd1c63
