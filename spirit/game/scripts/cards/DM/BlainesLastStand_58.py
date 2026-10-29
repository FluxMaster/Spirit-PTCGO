"""STUB: effect not implemented — do not guess mechanics.
Blaine's Last Stand (DM #58): trainer effect stubbed.

Card text:
  - You can play this card only when it is the last card in your hand.
  - Draw 2 cards for each Fire Pokémon you have in play.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="87ce236a-7ef6-5bef-b96f-309a975d7373",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=58,
    set_code="DM",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
