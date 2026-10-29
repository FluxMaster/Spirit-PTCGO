"""STUB: effect not implemented — do not guess mechanics.
Wait and See Hammer (SM8 #236): trainer effect stubbed.

Card text:
  - You can use this card only if you go second, and only on your first turn.
  - Discard an Energy from 1 of your opponent's Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="041f6216-a404-59e5-8716-2673b7e51768",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeHammer.Name",
    display_name="Wait and See Hammer",
    searchable_by=["Wait and See Hammer", "Item"],
    subtypes=["Item"],
    collector_number=236,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
