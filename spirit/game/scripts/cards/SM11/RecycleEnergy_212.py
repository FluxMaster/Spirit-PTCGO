"""STUB: effect not implemented — do not guess mechanics.
Recycle Energy (SM11 #212): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - If this card is discarded from play, put it into your hand instead of the discard pile.
"""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
card = EnergyCardDef(guid='bae61bae-a03e-5bf1-be33-0805061bff01', key='SM11', name='Recycle Energy', display_name='Recycle Energy', searchable_by=['Recycle Energy', 'Special'], subtypes=['Special'], collector_number=212, set_code='SM11', rarity=Rarities.Uncommon, energy_type=PokemonTypes.COLORLESS, is_special=True, return_to_hand_when_discarded_from_play=True)
