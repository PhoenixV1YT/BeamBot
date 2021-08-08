import discord
from discord import colour
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('BeamBot is Online. YAY!')

@client.command()
async def ping(ctx):
    bot_ping = discord.Embed(
        colour = 0xF7F786,
        description = f'⌛ {round(client.latency * 1000)}ms'
    )
    bot_ping.set_author(name='Pong!')
    await ctx.send(embed=bot_ping)

@client.command()
async def bothelp(ctx):
    help_embed = discord.Embed(
        colour = 0xF7F786,
        title = 'BeemBot Help',
        description = 'Thank you for having me on your Server! I am designed to bring you the best and easiest Moderation Experience. I also come with useful and fun Utility commands for you to use!'
    )
    help_embed.add_field(
        name=':shield: Moderation',
        value='`kick`\n`ban`',
        inline=False
    )
    help_embed.add_field(
        name=':receipt: Utility',
        value='`ping`\n`bothelp`',
        inline=False
    )
    await ctx.send(embed=help_embed)


@client.command(aliases=['km'])
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    kicked_embed = discord.Embed(
        colour = 0x7AF576,
        description = f':white_check_mark: {member.mention} has been **Kicked**'
    )
    kicked_embed.add_field(
        name='Reason',
        value=f'`{reason}`',
        inline=False
    )
    await ctx.send(embed=kicked_embed)

@client.command(aliases=['bm'])
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    banned_embed = discord.Embed(
        colour = 0x7AF576,
        description = f':white_check_mark: {member.mention} has been **Banned**'
    )
    banned_embed.add_field(
        name='Reason',
        value=f'`{reason}`',
        inline=False
    )
    await ctx.send(embed=banned_embed)

@client.command(aliases=['purge', 'delete', 'prune'])
async def clear(ctx, amount=11):
    amount = amount+1
    





client.run('ODczMDAxNDU5ODU4NDMyMDcy.YQyD9w.3rn_bwvIosPWPmMkQLc0n9q11v4')