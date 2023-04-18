import discord
from discord.ext import commands
from datetime import datetime




# Указываем нужные нам интенты
intents = discord.Intents.default()
intents.members = True

# Создаем клиент
bot = commands.Bot(command_prefix='!', intents=intents)


now = datetime.now()
timestamp = now.strftime("%d.%m.%Y %H:%M:%S")
# ID сообщения, на которое хотим реагировать
MESSAGE_ID = 1091996411932979231

# ID реакции, на которую будем ждать нажатие
REACTION_ID = "🍞"

# ID канала, куда отправлять ембед
TARGET_CHANNEL_ID = 1018868019935592520

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


# Обработчик событий on_ready
@bot.event
async def on_ready():
    print(f"{bot.user} подключен к Discord!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Scarlett"))


# Обработчик событий on_ready
@bot.event
async def on_ready():
    print(f"{bot.user} подключен к Discord!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Scarlett server"))


# Обработчик события on_raw_reaction_add
@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    # Проверяем, что реакция находится в нужном сообщении и имеет нужный ID
    if payload.message_id == MESSAGE_ID and str(payload.emoji) == REACTION_ID:
        # Получаем канал, куда нужно отправить ембед
        target_channel = bot.get_channel(TARGET_CHANNEL_ID)
        user = await bot.fetch_user(payload.user_id)
        # Создаем ембед и отправляем его
        embed = discord.Embed(title="", description=(f"﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍\n\nПриветствуем нового участника на сервере!\n\n{user.mention}\n\nОзнакомься с [правилами](https://discord.gg/S4WtmXazZE)\n\n﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉"), color=0x836953)
        embed.set_thumbnail(url="https://www.pngjoy.com/pngl/414/25897875_paw-cat-neko-aesthetic-kawaii-anime-art-sticker.png")
        embed.set_footer(text=timestamp)
        sent_message = await target_channel.send(embed=embed)
        # Удаляем отправленное сообщение через 3 минуты
        await sent_message.delete(delay=180)

bot.run("TOKEN")