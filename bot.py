import discord
import time

client = discord.Client()
bad = ['고도리']
helpEmbed = discord.Embed(title ='Welcome', color =0xFFBBC6)
helpEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/542369581143162892/774919210307551242/ScreenShot_20-11-08_00-02-13-000.jpg')
helpEmbed.add_field(name='$help,$도움말',value='도움이 필요하면 불러봐요',inline=True)
helpEmbed.add_field(name='다른 기능들',value='추후 업데이트 예정입니다',inline=True)


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("배고파")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    message_content=message.content
    for i in bad:
        if i in message_content:
            await message.channel.send('안녕!')





client.run("OTAxMzUzNzgyMjEyOTUyMTM0.YXOpIA.edOZzaO31GB7LY-H8tgdHv-bSQU")
