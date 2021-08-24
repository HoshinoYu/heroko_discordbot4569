import discord
import time

client = discord.Client()

async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('少女前線')
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_message(message):
    if message.content.startswith('*T-Doll'):
        channel = message.channel
        await channel.send('https://space.bilibili.com/3349725/article')
            
async def on_message(message):
    if message.content == '*group':
        guilds = await client.fetch_guilds(limit=150).flatten()
        for i in guilds:
            await message.channel.send(i.name)
        
client.run(ODc5NTUzNDExODcwMjQ0OTY1.YSRZ8g.GePSRv8YVtJD1BAAic4uMWSkQHg)
