import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import random
import asyncio
import time

class FunCommands(commands.Cog):
    """Fun commands for members to use!!"""
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)



    @checks.has_permissions(PermissionLevel.MODERATOR)
    @commands.command()
    async def ranklog(self, ctx, member: discord.Member, gamertag = None, purchase = None , amount = None):
        """
        logs smp ranks
        """
        if member == None:
            await ctx.send_help(ctx.command)
        channel = member.guild.get_channel(960482007379497040) 
        embed = discord.Embed(title="Rank Purchase",
                color=self.bot.main_color,
                description =(
                    f"Discord Tag : {member.mention}\n"
                     f"Discord User ID : {member.id}\n"
                     f"Gamer Tag : {gamertag}\n"
                     f"Amount : {amount}\n"
                     f"Purchase type : {purchase}\n")
                )
        embed.set_footer(text="Fun Plugin v1.0")

        await channel.send(embed=embed) 
        amethyst = "amethyst" 
        ruby = "ruby"
        obsidian = "obsidian"
        carneline = "carneline"
        epidote = "epidote"
        amazonite = "amazonite"
        smprank = member.guild.get_role(1003196550220099654)       
        if purchase == amethyst.lower():                 
            purchase = member.guild.get_role(1034474426902794321)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == ruby.lower():                 
            purchase = member.guild.get_role(1034474078754570353)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == obsidian.lower():                 
            purchase = member.guild.get_role(1034474068998631454)
            await member.add_roles(purchase)
            await member.add_roles(smprank)            
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)            
        elif purchase == epidote.lower():                 
            purchase = member.guild.get_role(1034474059645329481)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == carneline.lower():                 
            purchase = member.guild.get_role(1034473986211467271)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == amazonite.lower():                 
            purchase = member.guild.get_role(1034473906863607889)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)                  
        else:
            embed = discord.Embed(
                    description = (
                       f"Couldn’t add roles to {member.mention} due to incorrect log format!\n"
                       f"Please give them roles manually"))
            await channel.send(embed=embed)
     
    @checks.has_permissions(PermissionLevel.MODERATOR)       
    @commands.command()
    async def say2(self, ctx, *, message):
        """ModMail says what you want it to say."""
        await ctx.message.delete()
        await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")


    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @commands.command()
    async def userid(self, ctx):
        thread = ctx.thread
        if thread == None:
            member = ctx.author
        await ctx.send(f"{member.mention}'s ID is {member.id}")
        else:
            member = thread.recipient
            await ctx.message.delete()
            await ctx.send(f"{member.mention}'s ID is {member.id}", delete_after=15)

            
async def setup(bot):
    await bot.add_cog(FunCommands(bot))
