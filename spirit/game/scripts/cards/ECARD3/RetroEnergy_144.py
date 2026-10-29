"""STUB: effect not implemented — do not guess mechanics.
Retro Energy (ECARD3 #144): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy. When you play this card from your hand and attach it to 1 of your Evolved Pokémon, you may remove up to 2 damage counters from that Pokémon and discard the top card from it. (This counts as devolving it.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="1bd1bf3f-c2e1-5b3c-abc7-077d2721bb70",
    key="ECARD3",
    name="Retro Energy",
    display_name="Retro Energy",
    searchable_by=["Retro Energy", "Special"],
    subtypes=["Special"],
    collector_number=144,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
