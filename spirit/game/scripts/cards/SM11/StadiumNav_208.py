"""STUB: effect not implemented — do not guess mechanics.
Stadium Nav (SM11 #208): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import stadium_nav

card = ItemCardDef(guid='154d1a24-64b1-55eb-bddb-17570ccfe640', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.StadiumNav.Name', display_name='Stadium Nav', searchable_by=['Stadium Nav', 'Item'], subtypes=['Item'], collector_number=208, set_code='SM11', rarity=Rarities.Uncommon, effect=stadium_nav)
