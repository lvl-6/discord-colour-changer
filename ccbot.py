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

version = '0.0.1'
bot_token = os.getenv('CCBOT_TOKEN')
#bot_token = os.environ['CCBOT_TOKEN'] # try this if it fails on Windows


###############################################################################
# Bot Class
###############################################################################

class Bot(BotBase):
    def __init__(self):
        self.ready = False


        super().__init__(
            command_prefix = commands.when_mentioned,
            description = 'I change role colours for minimum wage.',
            owner_ids = 0,
            case_insensitive = True,
            )

        def run(self, version):
            self.VERSION = version
            super().run(bot_token, reconnect=True)

        async def on_connect(self):
            print('CCBot has connected to Discord...')

        async def on_disconnect(self):
            print('CCBot has disconnected from Discord...')

        async def on_ready(self):
            if not self.ready:
                self.ready = True
                print('CCBot is ONLINE.')
            else:
                print('CCBot reconnected.')


###############################################################################
# Python functions
###############################################################################




###############################################################################
# Program Execution
###############################################################################

# Define bot and run
bot = Bot()
bot.run(bot_token)

# Termination
