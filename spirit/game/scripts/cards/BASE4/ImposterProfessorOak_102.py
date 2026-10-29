"""STUB: effect not implemented — do not guess mechanics.
Imposter Professor Oak (BASE4 #102): trainer effect stubbed.

Card text:
  - Your opponent shuffles his or her hand into his or her deck, then draws 7 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="801f371c-6e63-56bf-beb9-32e261154a44",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterProfessorOak.Name",
    display_name="Imposter Professor Oak",
    searchable_by=["Imposter Professor Oak"],
    subtypes=[],
    collector_number=102,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
