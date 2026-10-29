"""STUB: effect not implemented — do not guess mechanics.
Defender (BASE1 #80): trainer effect stubbed.

Card text:
  - Attach Defender to 1 of your Pokémon. At the end of your opponent's next turn, discard Defender. Damage done to that Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4fb149ab-c3e1-5859-9cc9-62e89c0bafd3",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender"],
    subtypes=[],
    collector_number=80,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
