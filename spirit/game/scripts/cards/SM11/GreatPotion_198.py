"""STUB: effect not implemented — do not guess mechanics.
Great Potion (SM11 #198): trainer effect stubbed.

Card text:
  - Heal 50 damage from your Active Pokémon-GX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import great_potion, great_potion_condition

card = ItemCardDef(guid='5595381a-0377-5a0c-99aa-3bcec45efb8f', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.GreatPotion.Name', display_name='Great Potion', searchable_by=['Great Potion', 'Item'], subtypes=['Item'], collector_number=198, set_code='SM11', rarity=Rarities.Uncommon, effect=great_potion, condition=great_potion_condition)
