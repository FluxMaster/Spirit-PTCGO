"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Secret Plan (GYM2 #107): trainer effect stubbed.

Card text:
  - Put 1 card from your hand face down onto your Bench. (You can't play this card if your Bench is full.) Treat that card as a Basic Pokémon as long as it's face down. Flip the card if either player needs to know what it is in order to use an attack, a Pokémon Power, or a Trainer card. Flip the card if it ever uses an attack or Pokémon Power, evolves, retreats, is damaged by an attack, or is otherwise affected by an attack. At any time during your turn, you may flip the card over. When you flip that card over, if it isn't a Basic Pokémon, discard it and all cards attached to it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a0e81ae8-ebac-5d1c-a34a-374a0ed710d2",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesSecretPlan.Name",
    display_name="Lt. Surge's Secret Plan",
    searchable_by=["Lt. Surge's Secret Plan"],
    subtypes=[],
    collector_number=107,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
