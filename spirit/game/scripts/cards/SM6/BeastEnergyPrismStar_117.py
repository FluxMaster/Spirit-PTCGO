"""STUB: effect not implemented — do not guess mechanics.
Beast Energy {*} (SM6 #117): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to an Ultra Beast, it provides every type of Energy but provides only 1 Energy at a time. The attacks of the Ultra Beast this card is attached to do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="615041ff-89b0-5924-830e-a810d82285ad",
    key="SM6",
    name="Beast Energy {*}",
    display_name="Beast Energy {*}",
    searchable_by=["Beast Energy {*}", "Special", "Prism Star"],
    subtypes=["Special", "Prism Star"],
    collector_number=117,
    set_code="SM6",
    rarity=Rarities.Prism,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
