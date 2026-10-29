"""STUB: effect not implemented — do not guess mechanics.
Tropical Tidal Wave (NP #27): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, discard all Trainer cards your opponent has in play. If tails, discard all Trainer (excluding Supporter cards) you have in play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="27a734ae-6cc5-5c1d-8932-44b5faaf0471",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name",
    display_name="Tropical Tidal Wave",
    searchable_by=["Tropical Tidal Wave", "Item"],
    subtypes=["Item"],
    collector_number=27,
    set_code="NP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
