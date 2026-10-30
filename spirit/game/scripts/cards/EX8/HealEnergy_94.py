"""STUB: effect not implemented — do not guess mechanics.
Heal Energy (EX8 #94): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Heal Energy provides Colorless Energy. When you attach this card from your hand to 1 of your Pokémon, remove 1 damage counter and all Special Conditions from that Pokémon. If Heal Energy is attached to Pokémon-ex, Heal Energy has no effect other than providing Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5ef7ae06-0829-5bfa-9ed4-d97d1b9ce0fd",
    key="EX8",
    name="Heal Energy",
    display_name="Heal Energy",
    searchable_by=["Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
