"""STUB: effect not implemented — do not guess mechanics.
Poké Ball (BASE4 #121): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, you may search your deck for any Basic Pokémon or Evolution card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ea0157c8-db2a-5fe7-b8a7-246b6f96f09d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball"],
    subtypes=[],
    collector_number=121,
    set_code="BASE4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
