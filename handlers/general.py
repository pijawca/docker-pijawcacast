# -*- coding: utf-8 -*-
from misc import bot
from handlers import embeds
from re import findall
import handlers.buttons as buttons
import disnake
import core.handlers_db as core
import requests
import json
from config import admins


class events():
    @bot.event
    async def on_ready():
        await bot.change_presence(
            status=disnake.Status.idle, 
            activity=disnake.Activity(
                type=disnake.ActivityType.watching, 
                name='t.me/pijawca'
                )
            )

    @bot.event
    async def on_button_click(interaction):
        if isinstance(interaction, disnake.MessageInteraction):
            custom_id = interaction.data['custom_id']
            if custom_id == 'opendota_btn':
                await interaction.response.send_message('Отправьте свою ссылку на профиль в OpenDota через команду **!castopendota**\n'
                                                        'Пример: !castopendota https://www.opendota.com/players/153762083', 
                                                        ephemeral=True)
            # if custom_id == 'reserve0_btn':
            #     await interaction.response.send_message('Резерв. Кнопка обновится в следующем крупном обновлении', 
            #                                             ephemeral=True)
            # if custom_id == 'reserve1_btn':
            #     await interaction.response.send_message('Резерв. Кнопка обновится в следующем крупном обновлении', 
            #                                             ephemeral=True)
        if custom_id == 'rules_btn':
            role = disnake.utils.get(interaction.guild.roles, name='Участник')
            await interaction.author.add_roles(role)
            await interaction.response.send_message('Вы теперь участник сообщества!', ephemeral=True)

    @bot.event
    async def on_voice_state_update(member, before, after):
        if before.channel is None and after.channel is not None:
            core.on_voice_state_update(before.channel, after.channel, member.id)
        if before.channel is not None and after.channel is None:
            core.update_experience(member.id)

class administration():
    @bot.command() 
    async def rules(ctx):
        user_id = int(ctx.author.id)
        if user_id == admins[0]:
            await ctx.send(embed = embeds.rules())
            await ctx.send(embed = embeds.attempt_rules(), view=buttons.rules_btn())

    @bot.command()
    async def dbconn(ctx):
        if ctx.author.bot:
            return
        user_id = int(ctx.author.id)
        if user_id == admins[0]:
            message = core.dbconn()
            await ctx.send(message)
    
    @bot.command()
    async def patch(ctx):
        user_id = int(ctx.author.id)
        if user_id == admins[0]:
            await ctx.send(embed = embeds.patchEmbed())
        
class commands():
    @bot.command()
    async def start(ctx):
        if ctx.author.bot:
            return
        user_id = ctx.author.id
        nickname = ctx.author.display_name
        # avatar_url = 'https://static.vecteezy.com/system/resources/previews/022/058/960/non_2x/no-image-available-icon-vector.jpg'
        try:
            avatar_url = ctx.author.avatar.url
        except AttributeError:
            pass
        
        message = core.start(user_id, nickname, subscription=0, admin_on=0, avatar_url=avatar_url, experience=0)
        
        if message == 0:
            await ctx.send(embed=embeds.startEmbed0())
        else:
            await ctx.send(embed=embeds.startEmbed1())

    @bot.command()
    async def help(ctx):
        await ctx.send(
            embed=embeds.helpEmbed()
            )

    @bot.command()
    async def profile(ctx):
        if ctx.author.bot:
            return
        user_id = ctx.author.id
        
        for row in core.profile(user_id)[0]:
            nickname = row[2]
            avatar_url = row[5]
            experience = row[6]
            subscription = row[3]
            
            if subscription == 1:
                subscription = 'Да'
            else:
                subscription = 'Нет'
                
            if experience <= 9:
                experience = row[6] // 10
                for placehold in core.profile(user_id)[1]:
                    if placehold:
                        user_rank = placehold
                    
                        await ctx.send(embed = embeds.profileEmbed(f'• {nickname.upper()}', avatar_url, experience, user_rank, subscription), 
                        view = buttons.profile_btn())
            else:
                for placehold in core.profile(user_id)[1]:
                    if placehold:
                        user_rank = placehold
                    
                        await ctx.send(embed = embeds.profileEmbed(f'• {nickname.upper()}', avatar_url, experience, user_rank, subscription), 
                        view = buttons.profile_btn())

    @bot.command()
    async def rank(ctx):
        if ctx.author.bot:
            return
        user_id = ctx.author.id
        
        if core.rank(user_id)[0] is not None:
            experience = core.rank(user_id)[0]
            level = experience // 60
        await ctx.send(embed = embeds.rankEmbed(level, experience))
        
    @bot.command()
    async def castopendota(ctx):
        if ctx.author.bot:
            return
        user_id = ctx.author.id
        
        user_message = (ctx.message.content).replace('!castopendota ', '')
        user_message = findall(r'\d+', user_message)[0]
        core.castopendota(user_message, user_id)
        await ctx.send(embed = embeds.castopendotaEmbed())
    
    @bot.command()
    async def castlast(ctx):
        if ctx.author.bot:
            return
        user_id = ctx.author.id
        
        for row in core.fetchall(user_id):
            opendota_id = row[7]
            
        api_url = f'https://api.opendota.com/api/players/{opendota_id}/matches?limit=1'
        response = requests.get(api_url)
        latest_match = response.json()[0]

        match_id = latest_match['match_id']
        
        duration = latest_match['duration']
        minutes = duration // 60
        seconds = duration % 60
        duration = f'{minutes}:{seconds}'
        
        kills = latest_match['kills']

        deaths = latest_match['deaths']

        assists = latest_match['assists']

        party_size = latest_match['party_size']
        if party_size == None:
            party_size = 'Неизвестно'

        game_mode = latest_match['game_mode']
        if game_mode is not None:
            with open('json/game_mode.json', 'r') as f:
               json_data = json.load(f)
            game_mode = json_data.get(str(game_mode)).get('type')
        else:
            print(Exception)

        lobby_type = latest_match['lobby_type']
        if lobby_type is not None:
            with open('json/lobby_type.json', 'r') as f:
               json_data = json.load(f)
            lobby_type = json_data.get(str(lobby_type)).get('type')
        else:
            print(Exception)

        hero_id = latest_match['hero_id']
        if hero_id is not None:
            with open('json/heroes.json', 'r') as f:
               json_data = json.load(f)
            hero_id = json_data.get(str(hero_id)).get('localized_name')
        else:
            print(Exception)
        
        await ctx.send(embed = embeds.castlastEmbed(
            match_id, duration, party_size, game_mode, lobby_type, hero_id, kills, deaths, assists)
                       )
        