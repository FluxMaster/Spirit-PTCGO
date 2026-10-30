"""STUB: effect not implemented — do not guess mechanics.
Holon Energy WP (EX11 #106): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Holon Energy WP provides Colorless Energy.
  - If the Pokémon that Holon Energy WP is attached to also has a basic Water Energy card attached to it, prevent all effects, excluding damage, done to that Pokémon by your opponent's Pokémon. If the Pokémon that Holon Energy WP is attached to also has a basic Psychic Energy card attached to it, that Pokémon's Retreat Cost is 0. Ignore these effects if Holon Energy WP is attached to Pokémon-ex.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="923b0a11-4523-56dd-a11c-9b696c81042b",
    key="EX11",
    name="Holon Energy WP",
    display_name="Holon Energy WP",
    searchable_by=["Holon Energy WP", "Special"],
    subtypes=["Special"],
    collector_number=106,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
