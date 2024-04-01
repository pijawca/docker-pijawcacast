# -*- coding: utf-8 -*-
from disnake import Embed, Color
import requests


def startEmbed0():
    embed = Embed(description='<a:verif:1223971639587377232> Профиль был добавлен', 
                  color = Color.yellow()).set_footer(text='pijawca • t.me/pijawca • version beta', icon_url='https://i.imgur.com/N85ryui.jpeg')
    return embed

def startEmbed1():
    embed = Embed(description='<a:verif:1223971639587377232> Данные были обновлены', 
                  color = Color.yellow()).set_footer(text='pijawca • t.me/pijawca • version beta', icon_url='https://i.imgur.com/N85ryui.jpeg')
    return embed 

def helpEmbed():
    helpEmbed = Embed(
        description='[Github](https://github.com/pijawca/) • [Telegram](https://t.me/pijawca)', 
        color=Color.yellow())

    helpEmbed.add_field(
        name = '!start', value = 'Знакомство с ботом', inline = True)
    
    helpEmbed.add_field(
        name = '!profile', value = 'Профиль пользователя', inline = True)
    
    helpEmbed.add_field(
        name = '!castlast', value = 'Показать последний сыгранный матч', inline = True)
    
    helpEmbed.add_field(
        name = '!castopendota', value = 'Доступ к просмотру вашей статистика на сайте [OpenDota](https://www.opendota.com)', inline = True)
    
    helpEmbed.add_field(
        name = '!rank', value = 'Показывает ваше место в таблице на данном канале', inline = True)
    
    helpEmbed.add_field(
        name = '!patch', value = 'Что поменялось', inline = True)
    
    helpEmbed.set_footer(
        text = 'pijawca • t.me/pijawca • version beta', icon_url = "https://i.imgur.com/N85ryui.jpeg")
    
    return helpEmbed

def profileEmbed(title, thumbnail, level, position, subscription):
    profileEmbed = Embed(title = f'**{title}**', color = Color.yellow()).set_thumbnail(url=thumbnail).set_footer(text='pijawca • t.me/pijawca • version beta',
                            icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    profileEmbed.add_field(
        name='Уровень пользователя', value=f'**{level}**', inline=True)
    
    profileEmbed.add_field(
        name='Место в таблице', value=f'**{position}**', inline=True)
    
    profileEmbed.add_field(
        name='Подписка CAST', value=f'**{subscription}**', inline=True)
    
    return profileEmbed

def patchEmbed():
    with open("patches/latest", "r+") as f:
        latest = f.read()
    patchEmbed = Embed(description=latest,
    color = Color.yellow())
    patchEmbed.set_footer(text='pijawca • t.me/pijawca • version beta', icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    return patchEmbed

def castlastEmbed(match_id, duration, party_size, game_mode, lobby_type, hero_id, kills, deaths, assists):
    castlastEmbed = Embed(
        title = '**Статистика о последнем матче**',
        description=f'[Перейти на сайт Opendota](https://www.opendota.com/matches/{match_id})\n'
        f'Матч длился: **{duration}**\n'
        f'Размер лобби: {party_size} | Режим игры: **{game_mode}** | Тип лобби: {lobby_type}\n'
        f'Играя за **{hero_id}** закончил со счетом:\n'
        f'Убийств: **{kills}** | Смертей: **{deaths}** | Помощи: **{assists}**',
        color = Color.yellow())
    
    castlastEmbed.set_footer(text='pijawca • t.me/pijawca • version beta',
                            icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    return castlastEmbed
    

def rankEmbed(level, experience):
    rankEmbed = Embed(
        description=f'Уровень: {level}\nВсего опыта: {experience}',
        color = Color.yellow())
    
    rankEmbed.set_footer(text='pijawca • t.me/pijawca • version beta',
                            icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    return rankEmbed

def castopendotaEmbed():
    castopendotaEmbed = Embed(
        description='Профиль был добавлен',
        color = Color.yellow())
    
    castopendotaEmbed.set_footer(text='pijawca • t.me/pijawca • version beta',
                            icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    return castopendotaEmbed

def rules():
    rulesEmbed = Embed(
        description='''
        **Правила сервера**
        1・Будьте уважительны к другим участникам сервера. Не беспокойте их без веской на то причины, не оскорбляйте и не проявляйте агрессию или дискриминацию в их сторону.

        2・Старайтесь избегать общения на темы, касающиеся религии, философии, политики и иных вещей, способных стать поводом для конфликтов, которые негативно повлияют на атмосферу сервера.

        3・Запрещено распространять откровенный шокирующий контент, ярко демонстрирующий жестокость, расчленение, насилие, а также другие материалы, которые могут быть оскорбительными или неприемлемыми для некоторых участников.

        4・Запрещено распространять чужую личную информацию в публичном виде, в личных сообщениях или любым другим способом без согласия.
        • Под личной информацией подразумеваются различные медиа-файлы, личные переписки, паспортные данные, номера телефонов и т.д.

        5・Запрещено использование ботов или скриптов, которые могут нанести ущерб серверу или другим участникам.

        6・Запрещено размещение ссылок на вредоносные сайты и программное обеспечение, а также любой другой ссылки без соглашения с администрацией сервера.

        7・Если у вас есть какие-либо проблемы с другими участниками сервера, пожалуйста, обратитесь к администратору или модератору сервера для решения конфликта.

        8・Не пытайтесь обойти правила сервера или нарушать их намеренно.

        9・Незнание правил не освободит от ответственности.

        10・Нарушение правил сервера может привести к временному или постоянному исключению из сервера.
        • Если вы не согласны с решением администрации, вы можете написать просьбу об обжаловании в личные сообщения руководителям.

        11・Пожалуйста, помните, что цель сервера - создание приятной и безопасной среды для общения и развлечения. Пожалуйста, соблюдайте правила и помогайте сохранить эту среду для всех участников.
        ''',
    color = Color.yellow())
    
    rulesEmbed.set_footer(text='pijawca • t.me/pijawca • version beta',
                          icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    return rulesEmbed
    
def attempt_rules():
    attempt_rules = Embed(
        description='''
        А также наш сервер придерживается правил [Discord ToS](https://discord.com/terms) & [Community Guidelines](https://discord.com/guidelines)
        Если вы ознакомились с правилами сервера и соглашаетесь с ними, нажмите на реакцию "**Я прочитал правила!** <a:loadingaccept:1218770819937730670>", и вы автоматически станете участником.    
        ''',
    color = Color.yellow())
    
    attempt_rules.set_footer(text='pijawca • t.me/pijawca • version beta',
                          icon_url='https://i.imgur.com/N85ryui.jpeg')
    
    return attempt_rules