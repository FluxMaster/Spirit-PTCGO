"""STUB: effect not implemented — do not guess mechanics.
Tropical Tidal Wave (NP #36): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, discard all Trainer cards your opponent has in play. If tails, discard all Trainer cards (excluding Supporter cards) you have in play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9f983769-6f1d-59d6-ac67-646e7b6337db",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name",
    display_name="Tropical Tidal Wave",
    searchable_by=["Tropical Tidal Wave", "Item"],
    subtypes=["Item"],
    collector_number=36,
    set_code="NP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
