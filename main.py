import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
    print("Bot ready.")

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id != YOUR DISCORD ID HERE:
        return
    if after.deaf == True:
        await member.edit(deafen=False, mute=False)
        print("undeafened")
    if after.mute == True:
        await member.edit(mute=False, deafen=False)       
        print("unmuted")

bot.run("TOKEN HERE")
