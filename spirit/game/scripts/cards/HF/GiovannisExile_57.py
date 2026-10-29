"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Exile (HF #57): trainer effect stubbed.

Card text:
  - Discard up to 2 of your Benched Pokémon that have no damage counters on them and all cards attached to them.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b81603de-d01a-550f-b459-e432994f862a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=57,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
