"""STUB: effect not implemented — do not guess mechanics.
Tickling Machine (GYM1 #119): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, your opponent sets aside all the cards in his or her hand face down. Nobody may look at those cards. At the end of your opponent's next turn, your opponent puts those cards back into his or her hand. If tails, your turn ends immediately (you can't attack this turn).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c7315377-2a14-5f14-bc97-679102ca9c77",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TicklingMachine.Name",
    display_name="Tickling Machine",
    searchable_by=["Tickling Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=119,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
