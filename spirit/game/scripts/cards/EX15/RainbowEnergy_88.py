"""STUB: effect not implemented — do not guess mechanics.
δ Rainbow Energy (EX15 #88): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - δ Rainbow Energy provides Colorless Energy. While attached to a Pokémon that has δ on its card, δ Rainbow Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d4dfa59a-02cf-5cde-a3a7-f83eb2b8182d",
    key="EX15",
    name="δ Rainbow Energy",
    display_name="δ Rainbow Energy",
    searchable_by=["\u03b4 Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=88,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
