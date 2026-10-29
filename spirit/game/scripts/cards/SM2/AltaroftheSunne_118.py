"""STUB: effect not implemented — do not guess mechanics.
Altar of the Sunne (SM2 #118): trainer effect stubbed.

Card text:
  - Fire Pokémon and Metal Pokémon (both yours and your opponent's) have no Weakness.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="28c092f5-d671-5e44-9cd2-70284abb38a9",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheSunne.Name",
    display_name="Altar of the Sunne",
    searchable_by=["Altar of the Sunne", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
