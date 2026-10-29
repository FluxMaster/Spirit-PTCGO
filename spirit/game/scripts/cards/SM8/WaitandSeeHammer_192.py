"""STUB: effect not implemented — do not guess mechanics.
Wait and See Hammer (SM8 #192): trainer effect stubbed.

Card text:
  - You can use this card only if you go second, and only on your first turn.
  - Discard an Energy from 1 of your opponent's Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="47ea1480-4391-564a-bf66-9431401a4f86",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeHammer.Name",
    display_name="Wait and See Hammer",
    searchable_by=["Wait and See Hammer", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
