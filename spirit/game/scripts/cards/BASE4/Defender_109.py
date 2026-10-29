"""STUB: effect not implemented — do not guess mechanics.
Defender (BASE4 #109): trainer effect stubbed.

Card text:
  - Attach Defender to 1 of your Pokémon. At the end of your opponent's next turn, discard Defender. Damage done to that Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="aeeaca71-e23c-593c-8c10-31b59816f315",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender"],
    subtypes=[],
    collector_number=109,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
