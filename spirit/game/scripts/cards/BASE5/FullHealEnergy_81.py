"""STUB: effect not implemented — do not guess mechanics.
Full Heal Energy (BASE5 #81): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - If you play this card from your hand, the Pokémon you attach it to is no longer Asleep, Confused, Paralyzed, or Poisoned.
  - Full Heal Energy provides Colorless energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4246b06b-7bbd-512d-9fb6-ced009bcbd4c",
    key="BASE5",
    name="Full Heal Energy",
    display_name="Full Heal Energy",
    searchable_by=["Full Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=81,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
