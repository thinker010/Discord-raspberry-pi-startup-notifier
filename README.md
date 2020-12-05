# Discord-raspberry-pi-startup-notifier
This project is about how to send notification in discord through discord webhooks when raspberry pi boots up(after entering desktop).




First download the zip file through command `git clone https://github.com/thinker010/Discord-raspberry-pi-startup-notifier.git` in  and extract in your raspberry pi(.).
Then copy the `main.desktop` file and paste it in here `/etc/xdg/autostart`.
then paste the `main.py` to the pi folder at `/home/pi` (or where ever you want but you have to change the address of the `main.py` file in main.desktop )
now go to the terminal and make the python file executable by typing *sudo chmod +x main.py*.Now configure your code by typing ur desired message. 




# HOW TO GET YOUR WEBHOOK URL:

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks





# Source: 

https://pypi.org/project/discord-webhook/
        
   https://www.hackster.io/kamal-khan/desktop-shortcut-for-python-script-on-raspberry-pi-fd1c63
Hoping this was helpful.:)
