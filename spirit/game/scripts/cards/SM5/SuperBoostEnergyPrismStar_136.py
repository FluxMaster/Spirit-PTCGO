"""STUB: effect not implemented — do not guess mechanics.
Super Boost Energy {*} (SM5 #136): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to a Stage 2 Pokémon, it provides every type of Energy but provides only 1 Energy at a time. If you have 3 or more Stage 2 Pokémon in play, it provides every type of Energy but provides 4 Energy at a time.
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2a37d903-7ba4-5b1b-a10c-41793795b9a4",
    key="SM5",
    name="Super Boost Energy {*}",
    display_name="Super Boost Energy {*}",
    searchable_by=["Super Boost Energy {*}", "Special", "Prism Star"],
    subtypes=["Special", "Prism Star"],
    collector_number=136,
    set_code="SM5",
    rarity=Rarities.Prism,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
