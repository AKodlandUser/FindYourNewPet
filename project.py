# Refer to https://gist.github.com/matthewzring/9f7bbfd102003963f9be7dbcf7d40e51 for Markdown syntax.
import asyncio
import discord
from discord.ext import commands

description = '''A bot that can help you which pet is better depending on the size of your house.
Depending on the size of your house, the bot will recommend a pet that is suitable for you.

The bot will ask you a few questions and then give you a recommendation.
The bot will also give you some information about the pet you chose.

The bot will also use Markdown syntax to format the text, making it look a lot better than unformatted text.
This will catch the user's attention and make the bot look more professional.'''

# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Command: Recommend a pet
@bot.command()
async def recommend(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Hi! Let's find the best pet for you. How big is your house?" + "\n" + "(small (<60m²)/medium (60m²-100m²)/large (>100m²))")
    try:
        house_size = await bot.wait_for("message", check=check, timeout=30.0)
        size = house_size.content.lower()

        if size == "small":
            await ctx.send("**Recommendation**: A cat or a small dog would be perfect for a small house!")
        elif size == "medium":
            await ctx.send("**Recommendation**: A medium-sized dog or a rabbit would suit your house! Exotic pets like spiders or snakes also could suit your house.")
        elif size == "large":
            await ctx.send("**Recommendation**: A large dog or even multiple pets would be great!")
        else:
            await ctx.send("I didn't understand that. Please respond with **small**, **medium**, or **large**.")
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! Please try again.")

@bot.command()
async def info(ctx, pet):
    if pet == "dog":
        await ctx.send("Dogs are loyal and friendly companions. They require regular exercise and grooming. Depending on the breed, they can be **medium-maintenance** to **high-maintenance**.")
        await play_sound(r"C:\path\to\dog.mp3")
    elif pet == "cat":
        await ctx.send("Cats are independent and **low-maintenance** pets. They enjoy playtime and cuddles.")
        await play_sound(r"C:\path\to\cat.mp3")
    elif pet == "rabbit":
        await ctx.send("Rabbits are social and playful pets. They need a safe space to hop around and play.")
        await play_sound(r"C:\path\to\rabbit.mp3")
    elif pet == "fish":
        await ctx.send("Fish are **low-maintenance** pets that require a clean tank and proper food.")
        await play_sound(r"C:\path\to\fish.mp3")
    elif pet == "snake":
        await ctx.send("Snakes are **low-maintenance** pets. They require a secure enclosure and proper heating, along with adequate food.")
        await play_sound(r"C:\path\to\snake.mp3")
    elif pet == "spider":
        await ctx.send("Spiders are **low-maintenance** pets. They require a secure enclosure and proper humidity, with a diet of insects.")
        await play_sound(r"C:\path\to\spider.mp3")
    elif pet == "lizard":
        await ctx.send("Lizards are **low-maintenance** pets. They require a secure enclosure and proper heating, along with a diet of insects or vegetables.")
        await play_sound(r"C:\path\to\lizard.mp3")
    elif pet == "hamster":
        await ctx.send("Hamsters are small, **low-maintenance** pets. They require a secure cage and a diet of pellets and fresh vegetables.")
        await play_sound(r"C:\path\to\hamster.mp3")
    else:
        await ctx.send("I don't have information about that pet. Please choose from *dog*, *cat*, *rabbit*, *hamster*, *fish*, *snake*, *spider*, or *lizard*.")

# Run the bot
bot.run("secrettoken")
