import discord
import googletrans
import os
from pprint import pprint
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('少女前線')
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    #翻譯
    if client.user in message.mentions:
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
    if content == '':
        content = first
    if translator.detect(content).lang == DSTLanguage:
        return
    if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
        remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 
        
client.run(TOKEN)
