"""STUB: effect not implemented — do not guess mechanics.
Unidentified Fossil (SM5 #134): trainer effect stubbed.

Card text:
  - Play this card as if it were a 60-HP Colorless Basic Pokémon. At any time during your turn (before your attack), you may discard this card from play.
  - This card can't retreat.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e2ccaf21-019e-5810-a5c6-2140ec999467",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=134,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
