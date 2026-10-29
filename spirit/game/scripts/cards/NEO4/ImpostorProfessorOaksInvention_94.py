"""STUB: effect not implemented — do not guess mechanics.
Impostor Professor Oak's Invention (NEO4 #94): trainer effect stubbed.

Card text:
  - Look at your opponent's Prize cards. You may have your opponent shuffle them into his or her deck. If you do, your opponent takes that many cards from the top of his or her deck and sets them aside as his or her new Prize cards (without looking at them).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ebfbca4d-594e-54a6-a20b-6a47a335c9e9",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImpostorProfessorOaksInvention.Name",
    display_name="Impostor Professor Oak's Invention",
    searchable_by=["Impostor Professor Oak's Invention"],
    subtypes=[],
    collector_number=94,
    set_code="NEO4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
