"""STUB: effect not implemented — do not guess mechanics.
Rainbow Energy (EX12 #81): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Rainbow Energy to 1 of your Pokémon. While in play, Rainbow Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.) When you attach this card from your hand to 1 of your Pokémon, put 1 damage counter on that Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4bcc3422-7cc2-5502-aa2f-2146c0b49ada",
    key="EX12",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=81,
    set_code="EX12",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
