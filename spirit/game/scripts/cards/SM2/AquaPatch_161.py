"""STUB: effect not implemented — do not guess mechanics.
Aqua Patch (SM2 #161): trainer effect stubbed.

Card text:
  - Attach a Water Energy card from your discard pile to 1 of your Benched Water Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9fb81d10-cb62-52ca-97f8-af0e1ad772fe",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
