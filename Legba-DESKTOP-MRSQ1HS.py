import discord
from discord.ext import commands
import asyncio
import glob

# The token used to retrieve Legba from the internet.
TOKEN = "ODI2NjA5NzIzMzk0NDkwNDI5.YGO-Sw.9rEY1kkcOa_AdlX8dcsnf4nNyTs"

prefixMarker = ""
description = "I am the being through which language flows. Come to me if you need assistance delivering a message."

#Bot name
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefixMarker), description = description)

defaultChannel_ID = "532733219813195789" #public channel on my server.

#Load files in Source
source_directory = glob.glob('*.py')
for file in source_directory:
    print(file)

#Cog Loaders
cog_list = []

if __name__ == '__main__':
    for extension in cog_list:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    oauth_url()
    #await load_intro()

    print('>>')
    print(bot.user.name, ' is now loaded!')
    print(bot.user.id)
    print('Discord.py Version: {}'.format(discord.__version__))
    print('<<')

    
    for server in bot.guilds:
        defChannel = bot.get_channel(server.text_channels[0])
        await server.text_channels[0].send(description)

def oauth_url():
    perms = discord.Permissions()
    perms.all()
    perms.update(manage_roles=True,
                 manage_messages=True,
                 read_messages=True,
                 read_message_history=True,
                 send_messages=True,
                 embed_links=True,
                 change_nickname=True,
                 add_reactions=True,
                 administrator=True)
    print(perms.administrator)
    print(perms.manage_messages)
    print(perms.change_nickname)
    print("Perms have been set")

@bot.event
async def load_intro():
    print("active")
    for server in bot.guilds:
        await server.text_channels[0].send(description)

@bot.command()
async def erase(ctx, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.send(content="Your rights to exist have been confiscated.")
        await ctx.channel.send("*{0}*".format(user.name) + " *has been annihilated.*")
        await user.kick(reason="You have been banished to the other side.")

    else:
        await ctx.channel.send("*{0},*".format(ctx.author.name) + " you lack the credentials to deliver such a message...")

bot.run(TOKEN)
