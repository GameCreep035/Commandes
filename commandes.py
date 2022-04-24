import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
from pystyle import *
from random import randrange
import datetime
import asyncio
import random
import json

with open('config.json') as f:
    data = json.load(f)
    token = data["token"]

default_intents = discord.Intents.default()
default_intents.members = True

bot = commands.Bot(command_prefix="!")
client = discord.Client(intents=default_intents)
bot.remove_command("help")



@bot.event
async def on_ready():
    print("Bot prêt")
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("""
!help | Developped by GameCreep35#5395"""))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title = "Informations", description = "Voici les informations de ce serveur :", color=discord.Color.blue())
    embed.add_field(name="Serveur crée le :", value="2022-04-14 à 12:53:06")
    embed.add_field(name="Créateur du serveur :", value="GameCreep35#5395")
    embed.add_field(name="Region du serveur :", value="Europe")
    embed.add_field(name="Date et heure :", value=str(datetime.now()))
    embed.add_field(name = "Besoin d'aide ?", value =  "Fais !help")
    embed.set_thumbnail(url='')
    await ctx.send(embed=embed)

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Utilise la commande !help <commande> pour avoir plus d'informations sur la commande.", color = discord.Color.green())
    em.add_field(name="Moderation", value="`kick`, `ban`, `mute`")
    em.add_field(name="Utile", value="`info`, `delete`, `gstart`")
    em.add_field(name="Fun", value="`pfc`")
    await ctx.send(embed = em)

@help.command()
async def kick(ctx):
    em = discord.Embed(title = "Kick", description = "expulse un membre du serveur", color = discord.Color.red())
    em.add_field(name = "**Syntaxe**", value = "!kick <membre> [raison]")
    await ctx.send(embed = em)

@help.command()
async def ban(ctx):
    em = discord.Embed(title = "Ban", description = "Ban un membre du serveur", color = discord.Color.red())
    em.add_field(name = "**Syntaxe**", value = "!ban <membre> [raison]")
    await ctx.send(embed = em)

@help.command()
async def mute(ctx):
    em = discord.Embed(title = "Mute", description = "Mute un membre du serveur", color = discord.Color.red())
    em.add_field(name = "**Syntaxe**", value = "!mute <membre> [raison]")
    await ctx.send(embed = em)

@help.command()
async def pfc(ctx):
    em = discord.Embed(title = "Pierre feuille ciseaux", description = "Fais un pierre feuille ciseaux avec vous", color=0x47E10C)
    em.add_field(name = "**Syntaxe**", value = "!pfc <pierre / feuille / ciseaux>")
    await ctx.send(embed = em)

@help.command()
async def gstart(ctx):
    em = discord.Embed(title = 'Giveaway start', description = 'Lance un giveaway', color = discord.Color.blue())
    em.add_field(name = "**Syntaxe**", value = '!gstart <heures> [récompense]')

@bot.command()
@has_permissions(administrator = True, manage_messages = True, manage_roles = True)
async def ban(ctx, member: discord.Member):
    await member.ban(delete_message_days=0)
    await ctx.send("{} has been banned.".format(str(member)))
    
@ban.error
async def ban_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, "Tu n'as pas les permissions requises pour utiliser cette commande !")

@bot.command()
@has_permissions(administrator = True, manage_messages = True, manage_roles = True)
async def kick(ctx, member: discord.Member, arg2):
    await member.kick(reason=arg2)
    await ctx.send("{} has been kicked.".format(str(member)))

@kick.error
async def kick_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, "Tu n'a pas les permissions requises pour utiliser cette commande !")

@bot.command(pass_context = True)
@has_permissions(administrator = True)
async def mute(ctx, member: discord.Member, reason):
    guild = bot.guilds[0]
    role = get(guild.roles, id = 965648308846616576)
    await member.add_roles(role)
    embed=discord.Embed(
        title="User Muted!", 
        description="**{0}** was muted by **{1}** for reason **{2}** !".format(member, ctx.message.author, reason),
        color=0xff00f6
    )
    await ctx.send(embed=embed)

@mute.error
async def mute_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, "Tu n'a pas les permissions requises pour utiliser cette commande !")

@bot.command()
async def pfc(ctx, argument):
    pfc_list = ['pierre', 'feuille', 'ciseaux']
    r = randrange(0, 3)
    random = pfc_list[r]

    if argument == 'ciseaux' and random == 'pierre':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
J'ai gagné !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'ciseaux' and random == 'feuille':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
Tu as gagné !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'pierre' and random == 'feuille':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
J'ai gagné !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'pierre' and random == 'ciseaux':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
Tu as gagné !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'ciseaux' and random == 'pierre':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
J'ai gagné'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'ciseaux' and random == 'papier':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
Tu as gagné !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'ciseaux' and random == 'ciseaux':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
Egalité !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'pierre' and random == 'pierre':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
Egalité !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.orange()
    )

    elif argument == 'papier' and random == 'papier':
        embed = discord.Embed(
        title = 'Pierre feuille ciseaux',
        description = '''
{0} : {1} 
Moi : {2}
Egalité !'''.format(ctx.author, argument, pfc_list[r]),
        color = discord.Color.gold()
    )

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def gstart(ctx, mins : int, prize: str):
  embed = discord.Embed(
    title = 'Giveaway !',
    description = 'Récompense : {}'.format(prize),
    color = discord.Color.blue()
  )

  end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins * 60 * 60 + 2 * 60 * 60)

  embed.add_field(name='Fin dans :', value=end)

  my_msg = await ctx.send(embed = embed)

  await my_msg.add_reaction("🎉")

  await asyncio.sleep(mins * 60 * 60)

  new_msg = await ctx.fetch_message(my_msg.id)

  users = await new_msg.reactions[0].users().flatten()
  users.pop(users.index(bot.user))

  winner = random.choice(users)

  await ctx.send("Bravo ! {} a gagné : {}".format(winner, prize))

@bot.command()
async def shutdown(ctx):
    await bot.logout()
    print('Succefuly logged out.')

bot.run(token)