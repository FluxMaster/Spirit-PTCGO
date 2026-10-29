"""STUB: effect not implemented — do not guess mechanics.
Slumbering Forest (SM11 #207): trainer effect stubbed.

Card text:
  - If a Pokémon is Asleep, its owner flips 2 coins instead of 1 for that Special Condition between turns. If either of them is tails, that Pokémon is still Asleep.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import slumbering_forest_passive

card = StadiumCardDef(guid='6bcf5df3-745f-5e2a-be09-5c2424b23593', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.SlumberingForest.Name', display_name='Slumbering Forest', searchable_by=['Slumbering Forest', 'Stadium'], subtypes=['Stadium'], collector_number=207, set_code='SM11', rarity=Rarities.Uncommon, passive=slumbering_forest_passive)
