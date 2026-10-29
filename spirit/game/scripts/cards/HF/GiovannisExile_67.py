"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Exile (HF #67): trainer effect stubbed.

Card text:
  - Discard up to 2 of your Benched Pokémon that have no damage counters on them and all cards attached to them.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="de71ea3b-caf7-5879-adba-979ca5582ede",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=67,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
