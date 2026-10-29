"""STUB: effect not implemented — do not guess mechanics.
Bounce Energy (ECARD3 #142): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides ColorlessColorless Energy. You can attach this card to your Pokémon that has basic Energy cards attached to it. When you play this card from your hand and attach it to 1 of your Pokémon, return a basic Energy card attached to that Pokémon to your hand.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="211abfd4-15dd-55e5-a362-46f2c7f70ac8",
    key="ECARD3",
    name="Bounce Energy",
    display_name="Bounce Energy",
    searchable_by=["Bounce Energy", "Special"],
    subtypes=["Special"],
    collector_number=142,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
