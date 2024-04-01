# -*- coding: utf-8 -*-
import disnake


def profile_btn():
    opendota_btn = disnake.ui.Button(style=disnake.ButtonStyle.primary, 
                                     label="Настройка OpenDota", 
                                     custom_id='opendota_btn'
                                     )
    # reserve0_btn = disnake.ui.Button(style=disnake.ButtonStyle.primary, 
    #                                  label="Резерв", 
    #                                  custom_id='reserve0_btn'
    #                                  )
    # reserve1_btn = disnake.ui.Button(style=disnake.ButtonStyle.primary, 
    #                                  label="Резерв", 
    #                                  custom_id='reserve1_btn'
    #                                  )
    profile = disnake.ui.View()
    profile.add_item(opendota_btn)
    
    return profile

def rules_btn(): 
    rules_btn = disnake.ui.Button(style=disnake.ButtonStyle.green, 
                                  label='Я прочитал(а) правила! ✅', 
                                  custom_id='rules_btn')
    rules = disnake.ui.View()
    rules.add_item(rules_btn)
    
    return rules