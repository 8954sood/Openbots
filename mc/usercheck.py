import discord
import asyncio
from mcstatus import MinecraftServer

app = discord.Client()
ip_domain = "localhost"
@app.event
async def on_ready():
    print("It's Bot ready!")
    
    while True:
        await asyncio.sleep(4)
        try:
            server = MinecraftServer.lookup(ip_domain)
            status = await server.async_status()
            players = status.players.online
            game = discord.Game("now playing user - {0}".format(players))
            await app.change_presence(status=discord.Status.online, activity=game)
        except:
            game = discord.Game("Server is Close")
            await app.change_presence(status=discord.Status.dnd, activity=game)



app.run("<token>")
