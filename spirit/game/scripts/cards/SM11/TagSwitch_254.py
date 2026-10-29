"""STUB: effect not implemented — do not guess mechanics.
Tag Switch (SM11 #254): trainer effect stubbed.

Card text:
  - Move up to 2 Energy from 1 of your TAG TEAM Pokémon to another of your Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import tag_switch, tag_switch_condition

card = ItemCardDef(guid='c9760d1a-d5ec-50d6-be73-46592e9b8d57', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.TagSwitch.Name', display_name='Tag Switch', searchable_by=['Tag Switch', 'Item'], subtypes=['Item'], collector_number=254, set_code='SM11', rarity=Rarities.RareSecret, effect=tag_switch, condition=tag_switch_condition)
