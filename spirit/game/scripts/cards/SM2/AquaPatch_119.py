"""STUB: effect not implemented — do not guess mechanics.
Aqua Patch (SM2 #119): trainer effect stubbed.

Card text:
  - Attach a Water Energy card from your discard pile to 1 of your Benched Water Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="073d26a6-da8c-5445-ab3c-897f46bc25a2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item"],
    subtypes=["Item"],
    collector_number=119,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
