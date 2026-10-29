"""STUB: effect not implemented — do not guess mechanics.
Scoop Up (BASE4 #107): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon in play and return its Basic Pokémon card to your hand. (Discard all cards attached to that card.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f7a97997-9557-5ac0-8e72-cfa42680a4ab",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUp.Name",
    display_name="Scoop Up",
    searchable_by=["Scoop Up"],
    subtypes=[],
    collector_number=107,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
