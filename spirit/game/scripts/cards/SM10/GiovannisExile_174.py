"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Exile (SM10 #174): trainer effect stubbed.

Card text:
  - Discard up to 2 of your Benched Pokémon that have no damage counters on them and all cards attached to them.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2463937d-37d6-5657-aa43-c6195cfa6a5d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
