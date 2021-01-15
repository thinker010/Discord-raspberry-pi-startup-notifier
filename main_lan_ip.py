import datetime
import urllib.request
from threading import Thread
from discord_webhook import DiscordWebhook
import datetime
import subprocess
import re

net_status=False

def connect(host='https://google.com'):
    global net_status
    while net_status is False:
        try:
            urllib.request.urlopen(host)
        except:
            continue


def send_noti():
    global net_status
    now = datetime.datetime.now()
    wifi=lan_ip('wlan0')
    ethernet=lan_ip('eth0')
    while True:
        try:
            webhook = DiscordWebhook(url='YOUR DISCORD WEBHOOK URL',content='Online at '+now.strftime("%d-%m-%Y  %H:%M:%S")+' at local WLAN: '+str(wifi)+' or at local ELAN: '+ str(ethernet))
            response = webhook.execute()
            net_status=True
            break
        except:
            continue

def lan_ip(interface):
    ifconfig_result=subprocess.check_output(["ifconfig",interface])
    lan_ip_result=re.search(r"(192)\.(168)(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2}", str(ifconfig_result))
    if str(lan_ip_result) == 'None':
        return 'None'
    else:
        return lan_ip_result.group(0)

t1=Thread(target=connect)
t2=Thread(target=send_noti)

t1.start()
t2.start()

t1.join()
t2.join()
