"""STUB: effect not implemented — do not guess mechanics.
Channeler (SM11 #190): trainer effect stubbed.

Card text:
  - Remove all effects of attacks on you and each of your Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import channeler

card = SupporterCardDef(guid='8a3e2994-58bf-59b4-919b-4f47f20aeccf', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.Channeler.Name', display_name='Channeler', searchable_by=['Channeler', 'Supporter'], subtypes=['Supporter'], collector_number=190, set_code='SM11', rarity=Rarities.Uncommon, effect=channeler)
