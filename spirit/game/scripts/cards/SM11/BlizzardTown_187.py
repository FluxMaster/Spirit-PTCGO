"""STUB: effect not implemented — do not guess mechanics.
Blizzard Town (SM11 #187): trainer effect stubbed.

Card text:
  - Pokémon with 40 HP or less remaining (both yours and your opponent's) can't attack.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import blizzard_town_passive

card = StadiumCardDef(guid='ffa144f0-2019-5f28-aae1-162235036ea5', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.BlizzardTown.Name', display_name='Blizzard Town', searchable_by=['Blizzard Town', 'Stadium'], subtypes=['Stadium'], collector_number=187, set_code='SM11', rarity=Rarities.Uncommon, passive=blizzard_town_passive)
