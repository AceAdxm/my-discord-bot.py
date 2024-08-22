import discord
from discord.ext import commands
from PIL import Image, ImageOps
import io
import random

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Respond to a simple command
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}! How can I assist you today?")

# Mini-game: Rock Paper Scissors
@bot.command(name="rps")
async def rock_paper_scissors(ctx, choice: str):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)
    
    if choice not in choices:
        await ctx.send("Invalid choice! Choose rock, paper, or scissors.")
        return
    
    if choice == bot_choice:
        result = "It's a tie!"
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "paper" and bot_choice == "rock") or \
         (choice == "scissors" and bot_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    await ctx.send(f"You chose {choice}, I chose {bot_choice}. {result}")

# Image processing: Identify a user's profile picture
@bot.command(name="avatar")
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    avatar = member.avatar.url

    await ctx.send(f"[{member.name}'{'' if member.name.endswith('s') else 's'} Avatar]({avatar})")

# Respond to messages containing specific words
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "help" in message.content.lower():
        await message.channel.send("How can I assist you? Type `!help` for commands.")
    
    await bot.process_commands(message)

# Start the bot
bot.run('#your token here')
