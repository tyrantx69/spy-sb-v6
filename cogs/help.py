from discord.ext import commands, tasks
import discord
import main

class HelpCog(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.Cog.listener('on_message')	
	async def helpcommands(self, message):
		if message.author.id in main.SpyEncrypt2:
			async for messages in message.channel.history(limit=3):				
				if messages.id == message.id:
					try:
						arg = messages.content.lower().split()[1]
					except:
						arg = False
					if messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and not arg:
						await message.reply(f"""**Spy Self Bot V6 | Total Commands: 52**
						
> ・`{main.SpyEncrypt1}help` - Shows this page
> ・`{main.SpyEncrypt1}help nuke` - Shows nuking commands.
> ・`{main.SpyEncrypt1}help text` - Shows text commands.
> ・`{main.SpyEncrypt1}help utility` - Shows utility commands.
> ・`{main.SpyEncrypt1}help fun` - Shows fun commands.
> ・`{main.SpyEncrypt1}help status` - Shows status commands.
> ・`{main.SpyEncrypt1}help hack` - Shows hack commands.
> ・`{main.SpyEncrypt1}help nsfw` - Shows nsfw commands.
""")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == (f"hack"):
							await message.reply(f"""**Spy Self Bot V6 | Hack Commands (3)**
						
・`{main.SpyEncrypt1}tokendox <token>` - Get info on a token.
・`{main.SpyEncrypt1}delhook <url>` - Deletes a webhook.
・`{main.SpyEncrypt1}doxip <ip>` - Get info on an ip.""")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == (f"fun"):
							await message.reply(f"""**Spy Self Bot V6 | Fun Commands (4)**
						
・`{main.SpyEncrypt1}dickometer <@user>` - returns dick size
・`{main.SpyEncrypt1}avsteal <@user>` - Steals avatar of the user. 
・`{main.SpyEncrypt1}joke` - Shows A Random Joke.
・`{main.SpyEncrypt1}reddit` - Random Reddit Meme.
""")
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == (f"utility"):
						await message.reply(f"""**Spy Self Bot V6 | Utility Commands (9)**
						
> ・`{main.SpyEncrypt1}avatar <@user>` - Get avatar of any user. 
> ・`{main.SpyEncrypt1}banner <@user>` - Get banner of any user.
> ・`{main.SpyEncrypt1}serverinfo <server id>` - Get info about any server.
> ・`{main.SpyEncrypt1}userinfo <@user>` - Get info about any user.
> ・`{main.SpyEncrypt1}pingweb <url>` - Pings a website and returns it's status code.'
> ・`{main.SpyEncrypt1}idtoname <id>` - Get username of any user by their id.
> ・`{main.SpyEncrypt1}screenshot <website>` - Sends screenshot of the website.
> ・`{main.SpyEncrypt1}join <vc id>` - Joins the vc.
> ・`{main.SpyEncrypt1}leave` - Leaves the vc.
""")	

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == "text":
						await message.reply(f"""**Spy Self Bot V6 | Text Commands(8)**
						
>・`{main.SpyEncrypt1}spam <amount> <message>` - Haha spam go brrrr.
>・`{main.SpyEncrypt1}spamping` - Spam pings random users in the server.
>・`{main.SpyEncrypt1}spamthread <amount>` - Spam creates threads.
>・`{main.SpyEncrypt1}spampin <amount>` - Spam pins messages.
>・`{main.SpyEncrypt1}sendhook <url> <message>` - ok 
>・`{main.SpyEncrypt1}embedhook <url> <title> <image> <description>` - ok 
>・`{main.SpyEncrypt1}ghostmsg <message>` - Deletes the command immediatly, useful for ghost pings.
>・`{main.SpyEncrypt1}snipe` - ok 
""")			

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == "nuke":
						await message.reply(f"""**Spy Self Bot V6 | Nuke Commands(13)**
				
> ・`{main.SpyEncrypt1}channelfuckery` - You know it.
> ・`{main.SpyEncrypt1}botmassban <prefix> <cooldown>` - Initiates Massban In A Server using a bot.
> ・`{main.SpyEncrypt1}massban` - Initiates Massban In A Server.
> ・`{main.SpyEncrypt1}masskick` - Initiates Masskick In A Server.
> ・`{main.SpyEncrypt1}rolespam` - Spams Roles In A Server.
> ・`{main.SpyEncrypt1}channelspam` - Spams Channels In A Server.
> ・`{main.SpyEncrypt1}delroles` - Deletes roles.
> ・`{main.SpyEncrypt1}delchannels` - Deletes channels.
> ・`{main.SpyEncrypt1}renamechannels` - Renames channels.
> ・`{main.SpyEncrypt1}renameroles` - Renames roles.
> ・`{main.SpyEncrypt1}prune <rm> <days>` - Prunes the server. RM stands for role members i.e. if rm is 20 it will ignore those roles who have less than or equal to 20 members.
> ・`{main.SpyEncrypt1}checkprune <days>` - Returns the estimated amount of members pruned .
""")			
					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == (f"status"):
						await message.reply(f"""**Spy Self Bot V6 | Status Commands (5)**

> ・`{main.SpyEncrypt1}play <name>` - Playing Status.
> ・`{main.SpyEncrypt1}stream <name>` - Streaming Status.
> ・`{main.SpyEncrypt1}watching <name>` - Watching Status.
> ・`{main.SpyEncrypt1}listening <name>` - Listenting Status.
> ・`{main.SpyEncrypt1}stopactivity <name>` - Stops Activity.
""")			

					elif messages.content.lower().split()[0] == (f"{main.SpyEncrypt1}help") and messages.content.lower().split()[1] == (f"nsfw"):
						await message.reply(f"""**Spy Self Bot V6 | Nsfw Commands(10)**
						
> ・`{main.SpyEncrypt1}nsfw 4k` - 4k Porn.
> ・`{main.SpyEncrypt1}nsfw ass` - Real Ass.
> ・`{main.SpyEncrypt1}nsfw boobs` - Real Boobs.
> ・`{main.SpyEncrypt1}nsfw cum` - Cum Porn.
> ・`{main.SpyEncrypt1}nsfw feet` - Feet Pics.
> ・`{main.SpyEncrypt1}nsfw hentai` - Random Hentai.
> ・`{main.SpyEncrypt1}nsfw spank` - Spank!.
> ・`{main.SpyEncrypt1}nsfw pussy` - Pussy Porn.
> ・`{main.SpyEncrypt1}nsfw lesbian` - Lesban Porn.
> ・`{main.SpyEncrypt1}nsfw lewd` - Random Porn.
""")	
						
def setup(client):
	client.add_cog(HelpCog(client))
