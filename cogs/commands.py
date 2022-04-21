from discord.ext import commands, tasks
import discord, httpx,aiohttp
import main
import os
import sys 
import requests
from io import BytesIO
from urllib.parse import urlencode
from urllib.request import urlretrieve 

def tdoxfunc(token):
		userreq = httpx.get("https://discord.com/api/v10/users/@me",headers={"Authorization":token})
		botreq = httpx.get("https://discord.com/api/v10/users/@me",headers={"Authorization":f"Bot {token}"})
		for req in [userreq, botreq]:
			if req.status_code == 200:
				json = req.json()
				try:
					if json["premium_type"] == 2:
						nitro_type = "Nitro Boost"
					elif json["premium_type"] == 1:
						nitro_type = "Nitro Classic"
				except:
					nitro_type = None
				try:
					bot = json["bot"]
				except:
					bot = False
				try:
					phone = json["phone"]
				except:
					phone = None
				if len(json["bio"]) == 0:
					bio = None
				else:
					bio = json["bio"]
				avatar = f"https://cdn.discordapp.com/avatars/{json['id']}/{json['avatar']}"
				banner = f"https://cdn.discordapp.com/banners/{json['id']}/{json['banner']}"
				return f"""**SPY SELFBOT V6 | Token Dox**
		
**Name:** `{json['username']}#{json['discriminator']}`
**ID:** `{json['id']}`
**Bot?:** `{bot}`
**Email:** `{json['email']}`
**Phone:** `{phone}`
**Bio:** `{bio}`
**MFA Enabled?:** `{json['mfa_enabled']}`
**Nitro Type:** `{nitro_type}`
**Avatar:** {avatar}
**Banner:** {banner}
"""
		if userreq.status_code == 401 and botreq.status_code == 401:
			return "Invalid Token Specified."

class Cog(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.snipeauthor = {}
		self.snipecontent = {}
		self.snipetime = {}

	@commands.Cog.listener('on_message_delete')
	async def snipefunc(self, message):
		self.snipetime[message.channel.id] = datetime.datetime.now()
		self.snipeauthor[message.channel.id] = message.author
		self.snipecontent[message.channel.id] = message.content

	@commands.Cog.listener("on_message")
	async def commands(self, message):
		if message.author.id in main.SpyEncrypt2:
			async for messages in message.channel.history(limit=5):				
				if messages.id == message.id:
					if messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}av") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}avatar"):
						try:
							memb = messages.mentions[0]
						except:
							memb = messages.author
						try:
							av = memb.avatar_url
						except:
							av = memb.default_avatar_url
						await messages.reply(av)		
	
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}banner"):
						try:
							mem = messages.mentions[0]
						#	memb = httpx.get(f"https://discord.com/api/v10/guilds/{messages.guild.id}/members/{mem.id}",headers=main.headers)
						except:
							mem = messages.author
						memb = httpx.get(f"https://discord.com/api/v10/users/{mem.id}",headers=main.headers)
						print(memb.json())
						try:
							banner = memb.json()["banner"]
						except:
							banner = "None"
						await messages.reply(f"https://cdn.discordapp.com/banners/{mem.id}/{banner}?size=1024")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}userinfo") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}ui") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}doxuser"):
						try:
							user = messages.mentions[0]
							
						except:
							user = messages.author
						userobj = httpx.get(f"https://discord.com/api/v10/users/{user.id}",headers=main.headers)
						#print(userobj.json())
						try:
							av = userobj.json()["avatar"]
						except:
							av = "None"
						avatar = f"https://cdn.discordapp.com/avatars/{user.id}/{av}?size=1024"
						try:
							bannerig = userobj.json()["banner"]
						except:
							bannerig = "None"
						banner = f"https://cdn.discordapp.com/banners/{user.id}/{bannerig}?size=1024"
						await messages.reply(f"""**SPY SELFBOT V6 | Info on {user}**
						
**Name:** `{user.name}`						
**ID:** `{user.id}`
**Display Name:** `{user.display_name}`
**Created At:** `{user.created_at.strftime('%a, %d %B %Y, %I:%M %p UTC')}`						
**Avatar:** {avatar}
**Banner:** {banner}
								""")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}join") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}joinvc"):
						try:
							channel = messages.content.split()[1]
							channelobj = await main.client.fetch_channel(int(channel))
						except:
							channelobj = messages.guild.me.voice.channel
						await channelobj.connect()
						await messages.reply(f"SPY SB V6 | Joined VC.")
					   	

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}leave") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}leavevc"):
						
						for i in main.client.voice_clients:
							if i.guild == messages.guild:
								await i.disconnect()
								await messages.reply(f"k vai krliya leave")
						else:
							await messages.reply("Fail hogya vai cry krle")
					   	
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}idtoname"):
						id = int(messages.content.split()[1])
						try:
							obj = await self.client.fetch_user(id)
							await messages.reply(obj)
						except:
							await messages.reply("SPY SELFBOT V6 | Invalid ID.")

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}ping") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}pingweb"):
						url = messages.content.split()[1]
						await messages.reply(f"Pinging {url}....")
						req = httpx.get(url)
						if req.status_code in (200, 201, 204):
							await messages.reply(f"Site is working perfectly. Status Code - {req.status_code}")
						elif req.status_code in (400,403,404):
							await messages.reply(f"Site is fucked up. Status Code - {req.status_code}")

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}serverinfo") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}doxserver"):
						try:
							serverid = messages.content.split()[1]
						except:
							serverid = messages.guild.id
						server = await main.client.fetch_guild(int(serverid))
						try:
							serverowner = server.owner.mention
						except:
							serverowner = "None"
						await messages.channel.send(f"""**Name:** `{server.name}`
**ID:** `{server.id}`
**Owner:** `{serverowner}`
**Created At:** `{server.created_at.strftime("%d %b 20%y, %H:%M:%S")}`
**Boosts:** `{server.premium_subscription_count}`
**Avatar:** {server.icon_url}
**Banner:** {server.banner_url}

**__Members__**

**Total:** `{len(server.members)}`
**Humans:** `{sum(not member.bot for member in server.members)}`
**Bots:** `{sum(member.bot for member in server.members)}`

**__Channels__**

**Categories:** `{len(server.categories)}`
**Text Channels:** `{len(server.text_channels)}`
**Voice Channels:** `{len(server.voice_channels)}`

**__Roles__**

**Total:** `{len(server.roles)}`""")

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}pinspam"):
						amount = int(messages.content.split()[1])
						async with aiohttp.ClientSession(headers=main.headers) as session:
							for idk in range(amount):
								messageig = await messages.channel.send(f"SPY SELFBOT V6 | Mass Pin.")
								async with session.put(f"https://discord.com/api/v9/channels/{messages.channel.id}/pins/{messageig.id}",json={"reason":"SPY SELFBOT V6 | Mass Pin."}) as r:
					   	       	#if vgehra krdo koi bhay
									print("Pinned")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}restart"):
						os.execv(sys.executable, ['python'] + sys.argv)
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamthread") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}threadspam"):
						amount = int(messages.content.split()[1])
						async with aiohttp.ClientSession(headers=main.headers) as session:
							for idk in range(amount):
								messageig = await messages.channel.send("SPY SELFBOT V6 | Mass Thread.")
								async with session.post(f"https://discord.com/api/v9/channels/{messages.channel.id}/messages/{messageig.id}/threads",json={"name":"SPY SELFBOT V6 | Mass Thread.","auto_archive_duration":60}) as r:
									if r.status in (200, 201, 204):
										print("Threaded")
									else:
										print("Failed")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}avsteal") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}avatarsteal") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}stealavatar"):
						user = messages.mentions[0]
						apicall = httpx.get(f"https://discord.com/api/v10/guilds/{messages.guild.id}/members/{user.id}",headers=main.headers)
						avmaybe = apicall.json()["user"]["avatar"]
						av = f"https://cdn.discordapp.com/avatars/{user.id}/{avmaybe}"
						req = httpx.get(av)
						bytes = BytesIO(req.read())
						avatarig = bytes.getvalue()
						await main.client.user.edit(avatar=avatarig)
						await messages.reply(f"SPY SELFBOT V6 | Av stolen and applied.")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}dickometer"):
						a=random.randrange(1,10)
						b = "="
						m=b*a
						await messages.reply(f"8{m}D")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}joke"):
						r = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
						res = r.json()
						joke=res["joke"]
						await message.reply(joke)
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}meme"):
						r = httpx.get("https://memes.blademaker.tv/api")
						res = r.json()
						meme = res["image"]
						await messages.reply(meme)	
						
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}tdox") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}tokendox") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}doxtoken"):
						token = messages.content.split()[1]
						print(token)
						await messages.reply(tdoxfunc(token))
		
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}delhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}delwebhook"):
						webhook = messages.content.split()[1]
						req = httpx.delete(webhook)
						if req.status_code == 204:
							await messages.reply(f"SPY SELFBOT V6 | Webhook deleted.")
						else:
							await messages.reply(f"SPY SELFBOT V6 | Failed, request responded with {req.status_code}.")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}doxip") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}iplookup"):
						ip = messages.content.split()[1]
						doxreq = httpx.get(f"https://api.ipfind.com?ip={ip}")
						json = doxreq.json()
						await messages.reply(f"""SPY SELFBOT V6 | IP Lookup
						
IP: {json['ip_address']}
Country: {json['country']}
Country Code: {json['country_code']}
Continent: {json['continent']}		
Continent Code: {json['continent_code']}
City: {json['city']}
County: {json['county']}
Region: {json['region']}
Region Code: {json['region_code']}
Postal Code: {json['postal_code']}
Time Zone: {json['timezone']}
Owner: {json['owner']}
Longitude: {json['longitude']}
Latitsude: {json['latitude']}
Currency: {json['currency']}
Languages: {json['languages']}""")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}nsfw"):
						try:
							tag = messages.content.split()[1]
						except:
							tag = "hentai"
						req = httpx.get(f"http://api.nekos.fun:8080/api/{tag}")
						await messages.reply(req.json()["image"])
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}stream") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}streaming"):
						try:
							rawname = messages.content.split()[2:]
							name = ' '.join(rawname)
						except:
							name = "SPY SELFBOT V6"
						try:
							url = messages.content.split()[1]
						except:
							url = "https://twitch.tv/tyrantx1337"
						await messages.reply("SPY SELFBOT V6 | Changing Status...")
						stream = discord.Streaming(name=name,url=url)
						await self.client.change_presence(activity=stream)
						await messages.reply("SPY SELFBOT V6 | Streaming created!")

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}playing") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}play"):
						try:
							rawname = messages.content.split()[1:]
							name = ' '.join(rawname)
						except:
							name = "SPY SELFBOT V6"
						game = discord.Game(name=name) 
						await messages.reply("SPY SB V6 | Changing Status......")
						await self.client.change_presence(activity=game) 
						await messages.reply("SPY SELFBOT V6 | Playing Created!")
    
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}watch") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}watching"):
						try:
							rawname = messages.content.split()[1:]
							name = ' '.join(rawname)
						except:
							name = "SPY SELFBOT V6"
						await messages.reply("SPY SELFBOT V6 | Changing Status.....")
						await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
						await messages.reply("SPY SELFBOT V6 | Watching created!")

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}listen") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}listening"):
						try:
							rawname = messages.content.split()[1:]
							name = ' '.join(rawname)
						except:
							name = "SPY SELFBOT V6"
						await messages.reply("SPY SELFBOT V6 | Changing Status.....")
						await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=name))
						await messages.reply("SPY SELFBOT V6 | Listening created.")
   
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}stopstatus") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}killstatus"):
						await messages.reply("SPY SELFBOT V6 | Killing Status...")
						await self.client.change_presence(activity=None)
						await messages.reply("SPY SELFBOT V6 | Status Removed Successfully.")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}embedhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}embedwebhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}webhookembed"):
						webhook = messages.content.split()[1]
						title = messages.content.split()[2]
						split = messages.content.split()
						for element in messages.content.split():
							if element.startswith('https://'):
								img = element
								split.remove(element)
						rawdescription = split[2:]
						description = ' '.join(rawdescription)
						json = {"embeds":[{"title":title,"description":description,"image":{"url":img}}]}
						req = httpx.post(webhook,json=json)	
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}snipe"):
						try:
							author = self.snipeauthor[messages.channel.id]
							content = self.snipecontent[messages.channel.id]
							time = self.snipetime[messages.channel.id].strftime('%a, %d %B %Y, %I:%M %p UTC')
							await messages.reply(f"""Message sent by {author} deleted in {messages.channel}

Message Content - {content}
Deleted at - {time}""")
						except:
							await messages.reply(f"kuch vi del na hua bhaijaan")		
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}ghostmsg") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}ghostping") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}ghostmessage"):
						await messages.delete()
				

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spam"):
						amount = messages.content.split()[1]
						msg = messages.content.replace(f"{main.SpyEncrypt1}spam {amount}","")
						for idk in range(int(amount)):
							await messages.channel.send(msg)

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamping"):
						members = [member.mention for member in messages.guild.members]
						if len(members) >= 100:
							ping = random.sample(members, 100)
						else:
							ping = random.sample(members, 50)
						await messages.channel.send(ping)
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}sendhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}sendwebhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}webhooksend"):
						webhook = messages.content.split()[1]
						rawmessage = messages.content.split()[2:]					
						message = ' '.join(rawmessage)
						req = httpx.post(webhook,json={"content":message})		
					if messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}screenshot") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}ss"):
						params = urlencode(dict(access_key="a96159e0141a452882c3550c8989a820",url=messages.content.split()[1]))
						k = urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")			
						await messages.reply(file=discord.File("screenshot.jpeg"))	


def setup(client):
	client.add_cog(Cog(client))
