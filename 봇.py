import discord
import os

client = discord.Client()

건의사항 = 657221052174434307

@client.event
async def on_message(message):
    if message.content.startswith("!확성기"):
        msg = message.content[5:]
        await client .get_channel(int(690199478401237072)).send(msg)

        
        
client.run("NzI5NTUxOTMwMTM2ODU0NTU4.XwLHUQ.41GNyu2hAN159h5L_T9dW7rH1Mk")
