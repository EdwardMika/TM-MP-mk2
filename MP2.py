import discord
from discord.ext import commands

discord_bot_token = 'MTE0MDQ3MzAyMzc4NzQzODIyMQ.G5-4XR.u3-89_vfHgx-AqdLzV8MMKJrgBYXVhApMBxh44'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print('Bot: {}'.format(bot.user))
    await bot.change_presence(status=discord.Status.online, activity=game)

game = discord.Game("help: 도와줘정마피")

#test
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def 도와줘정마피(ctx):
    await ctx.send("TM가입: TM가입 폼 링크 제공")
    await ctx.send("TM공모전: 진행중인 공모전 정보")
    await ctx.send("TM부서: TM내 부서 정보")

#기본 담소
@bot.command()
async def 이름이뭐야(ctx):
    await ctx.send("니네 단장 정마피다")

@bot.command()
async def 야이(ctx):
    await ctx.send("뭐 ㅋㅋㅋ")

@bot.command()
async def 내가누구야(ctx):
    await ctx.send(f'TM의 노예 {ctx.author.name} 아니십니까~')

@bot.command()
async def TM이뭐야(ctx):
    await ctx.send(f'세계 최악 최흉의 독재자가 있는 집단')

@bot.command(aliases=['준서','wjdwnstj','wnstj','정마피'])
async def 정준서(ctx):
    if ctx.author.id == 366189735216939008 or ctx.author.id == 815277688653611070:
        await ctx.send("아 그 미공찐 말씀이신가요?")
    else:
        await ctx.send("걔는 뭐... 에휴...")

@bot.command()
async def 미공찐(ctx):
    await ctx.send("확실히 이름이 정... 뭐시기였던 것 같은데...")

@bot.command()
async def 죽어라정마피(ctx):
    await ctx.send("얘! 죽어버리렴~")

#TM 관련 정보
@bot.command()
async def TM가입(ctx):
    await ctx.send("https://docs.google.com/forms/d/e/1FAIpQLSe66h3rtRTlrbnk5f5eSLn5K4emX-YkqQ7fTrk3e7orA7A_qg/viewform?usp=send_form")

@bot.command()
async def TM공모전(ctx):
    await ctx.send("음악부: https://discord.com/channels/444712493080641536/641225896212299776/1139554471848980520")

@bot.command()
async def TM부서(ctx):
    await ctx.send("총무부, 영상부, 아틸리에, ETP, CRAFTING TABLE")


#이스터에그
@bot.command(aliases=['19221230','노동','단결'])
async def 소비에트(ctx):
    await ctx.send("Пpoлeтapии всех стран, соединяйтесь!")

bot.run(discord_bot_token)