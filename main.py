#sudo pip3 install discord-webhook
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='YOUR DISCORD WEBHOOK URL', content='YOUR MESSAGE')
response = webhook.execute()
