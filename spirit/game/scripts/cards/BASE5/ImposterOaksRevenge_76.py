"""STUB: effect not implemented — do not guess mechanics.
Imposter Oak's Revenge (BASE5 #76): trainer effect stubbed.

Card text:
  - Discard a card from your hand in order to play this card. Your opponent shuffles his or her hand into his or her deck, then draws 4 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="649ff12a-4b3e-52ca-9ad6-840072930d2f",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterOaksRevenge.Name",
    display_name="Imposter Oak's Revenge",
    searchable_by=["Imposter Oak's Revenge"],
    subtypes=[],
    collector_number=76,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
