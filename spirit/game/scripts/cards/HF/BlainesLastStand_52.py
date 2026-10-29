"""STUB: effect not implemented — do not guess mechanics.
Blaine's Last Stand (HF #52): trainer effect stubbed.

Card text:
  - You can play this card only when it is the last card in your hand.
  - Draw 2 cards for each Fire Pokémon you have in play.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2aa98f63-7db3-5bbc-ba5c-3c8b93c9da2a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=52,
    set_code="HF",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
