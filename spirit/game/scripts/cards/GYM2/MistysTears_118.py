"""STUB: effect not implemented — do not guess mechanics.
Misty's Tears (GYM2 #118): trainer effect stubbed.

Card text:
  - Discard 1 of the other cards in your hand in order to search your deck for up to 2 Water Energy cards. Show those cards to your opponent, then put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="96464e84-d474-5522-959b-e8322a411ce4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysTears.Name",
    display_name="Misty's Tears",
    searchable_by=["Misty's Tears"],
    subtypes=[],
    collector_number=118,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
