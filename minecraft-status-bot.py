# Minecraft Status bot for Discord
# By noseapus#9041

# discord stuff and python stuff
import discord, datetime, asyncio
# https://github.com/Dinnerbone/mcstatus python thing to check status of minecraft servers
from mcstatus import MinecraftServer

# Discord bot token. Shouldn't be shared.
token = open("token.txt",'r').read()
# Address of the minecraft server
mcAddress = ""
# How often to check the status of the server.
checkFrequency = 10

# Start bot
client = discord.Client()

# When bot starts, start checking status of the minecraft server
@client.event
async def on_ready():
    client.loop.create_task(refreshStatus())

async def refreshStatus():
    # loops
    while True:
        # Error handling for if server can't be reached.
        try:
            # Get info from server
            server = MinecraftServer.lookup(mcAddress).status()
            # Put in console if server was reached
            print(datetime.datetime.now().isoformat()+"The server has {0} players and replied in {1} ms".format(server.players.online, server.latency))
            # Update status to reflect player numbers
            await client.change_presence(activity=discord.Game(name="Minecraft (" + str(server.players.online) + " online)", status=discord.Status.online))
        except:
            # If it couldn't reach the server, put that in console, and update status
            print(datetime.datetime.now().isoformat()+"Error reaching server.")
            await client.change_presence(activity=discord.Game(name="Error reaching server", status=discord.Status.dnd))

        await asyncio.sleep(checkFrequency)

# Start the bot
client.run(token)
