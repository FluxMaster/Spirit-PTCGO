"""STUB: effect not implemented — do not guess mechanics.
Poké Ball (BASE2 #64): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, you may search your deck for any Basic Pokémon or Evolution card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4b0489f7-d7e0-5b1c-a27b-a73dc98e6867",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball"],
    subtypes=[],
    collector_number=64,
    set_code="BASE2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
