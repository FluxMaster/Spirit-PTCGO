"""STUB: effect not implemented — do not guess mechanics.
Weakness Guard (ECARD2 #141): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon. Discard it at the end of your opponent's next turn.
  - As long as this card is attached, this Pokémon has no Weakness.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="49aba60a-3e19-5b0a-9239-3e9cf12ee117",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessGuard.Name",
    display_name="Weakness Guard",
    searchable_by=["Weakness Guard"],
    subtypes=[],
    collector_number=141,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
