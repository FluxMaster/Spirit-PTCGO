"""STUB: effect not implemented — do not guess mechanics.
Nanu (SM9 #150): trainer effect stubbed.

Card text:
  - Choose a Basic Darkness Pokémon in your discard pile. Switch it with 1 of your Pokémon in play. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f91f713c-dd7e-59a5-9c62-6be92884231f",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nanu.Name",
    display_name="Nanu",
    searchable_by=["Nanu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
