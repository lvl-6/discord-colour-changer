###############################################################################
# ccbot.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 24/09/2020
# 
# Description:
# A simple bot to allow non-owners to change their role colour.
#
###############################################################################

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot as BotBase

version = '0.6'
bot_token = os.getenv('CCBOT_TOKEN')


###############################################################################
# Bot Initialisation
###############################################################################

bot = BotBase(
    command_prefix = commands.when_mentioned,
    description = 'I change role colours for minimum wage.',
    owner_ids = 0,
    case_insensitive = True,
    )

@bot.event
async def on_connect():
    print('CCBot has connected to Discord...')


@bot.event
async def on_disconnect():
    print('CCBot has disconnected from Discord...')


@bot.event
async def on_ready():
    print('CCBot is ONLINE.')


###############################################################################
# Bot Commands
###############################################################################

@bot.command()
async def about(ctx):
    """
    Show the "about" message
    """
    embed_about = discord.Embed(
        title = 'About ccbot v' + version,
        description = 'A simple bot for changing role colours.',
        color = 0x00ccff
        )

    embed_about.add_field(
        name = 'Author',
        value = 'John C',
        inline = False
        )
    embed_about.add_field(
        name = 'Source Code',
        value = 'https://www.github.com/lvl-6/',
        inline = False
        )

    await ctx.send(embed=embed_about)


# TODO
# Allow non-role-managers to change their role colour, by using something
# like "@commands.has_any_role(list_of_changeable_roles)"
@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def cc(ctx, colour: str):
    """
    Change the colour of your role
    Pass colour as a hexadecimal RGB value beginning with 0x
    i.e. for red 0xFF0000
    """
    desired_colour = int(colour, 0)

    # Get the highest role of the user
    user_role_list = ctx.message.author.roles
    list_length = len(user_role_list)
    highest_role = user_role_list[list_length-1:]
    highest_role_name = ''
    for role in highest_role:
        highest_role_name = role.name

    # Edit the colour of user's highest role
    for role in ctx.guild.roles:
        if role.name == highest_role_name:
            await role.edit( color = desired_colour )


###############################################################################
# Program Execution
###############################################################################

# Execution
bot.run(bot_token)

# Termination
print('CCBot has been terminated.')
