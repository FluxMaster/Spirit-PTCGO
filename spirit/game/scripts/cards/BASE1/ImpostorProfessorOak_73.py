"""STUB: effect not implemented — do not guess mechanics.
Impostor Professor Oak (BASE1 #73): trainer effect stubbed.

Card text:
  - Your opponent shuffles his or her hand into his or her deck, then draws 7 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e16799ba-3669-5cd4-85d3-19b374cb8623",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImpostorProfessorOak.Name",
    display_name="Impostor Professor Oak",
    searchable_by=["Impostor Professor Oak"],
    subtypes=[],
    collector_number=73,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
