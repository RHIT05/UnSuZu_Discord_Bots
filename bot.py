# bot.py
import os
import subprocess
import uuid

import cached_property
import discord

TOKEN = os.environ["DISCORD_BOT1_TOKEN"]


def new_intern():
    new_nick = subprocess.check_output(["gpw", "1", "13"]).decode().strip()
    return new_nick


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_member_join(self, member):
        print(f"joined: {member} @ {member.guild}")
        await member.edit(nick=new_intern())
        guild = member.guild

        for key in dir(member):
            if key.startswith("_"):
                continue
            attr = getattr(member, key)
            try:
                print(f"member.{key}: {attr()}")
            except:
                print(f"member.{key}: {attr}")

        if guild.system_channel is not None:
            to_send = f"""
Welcome to {guild.name} Intern Program.

Your username is {member.mention}.
Your UUID is {uuid.uuid4()}.

#onboarding Tasks:

0. Share your GPG and SSH Public Keys.
1. Share a dogecoin address. (Coinnomi -> Share -> Discord)
2. LabCoat will be assigned after onboarding.

Your company e-mail address is {member.nick}@unsuzu.xyz.

You can check your e-mail at https://www.mailinator.com/v3/index.jsp?zone=public&query={member.nick}
"""
            await guild.system_channel.send(to_send)

    async def on_member_leave(self, member):
        guild = member.guild

        print(f"departed: {member}")
        channel = client.get_channel("channel id here")
        await channel.edit(name=f"Member count: {channel.guild.member_count()}")

        if guild.system_channel is not None:
            to_send = f"departed: {member.mention} to {guild.name}!"
            await guild.system_channel.send(to_send)


client = MyClient()
client.run(TOKEN)
