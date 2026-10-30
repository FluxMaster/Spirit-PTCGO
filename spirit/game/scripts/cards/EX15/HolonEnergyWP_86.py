"""STUB: effect not implemented — do not guess mechanics.
Holon Energy WP (EX15 #86): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Holon Energy WP provides Colorless Energy.
  - If the Pokémon that Holon Energy WP is attached to also has a basic Water Energy card attached to it, prevent all effects of attacks, excluding damage, done to that Pokémon by your opponent's Pokémon. If the Pokémon that Holon Energy WP is attached to also has a basic Psychic Energy card attached to it, that Pokémon's Retreat Cost is 0. Ignore these effects if Holon Energy WP is attached to Pokémon-ex.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c4e565ba-8199-543c-8f27-7d9299b7930d",
    key="EX15",
    name="Holon Energy WP",
    display_name="Holon Energy WP",
    searchable_by=["Holon Energy WP", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX15",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
