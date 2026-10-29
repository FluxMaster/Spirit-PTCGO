"""STUB: effect not implemented — do not guess mechanics.
Blaine (GYM2 #100): trainer effect stubbed.

Card text:
  - During this turn, instead of attaching your free Energy card, you may instead attach 2 Fire Energy cards to 1 of your Pokémon with Blaine in its name. (Playing additional copies of this card this turn has no effect.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b52f1787-5bbe-5950-9039-2ce8435f6434",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blaine.Name",
    display_name="Blaine",
    searchable_by=["Blaine"],
    subtypes=[],
    collector_number=100,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
