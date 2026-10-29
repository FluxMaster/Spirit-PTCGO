"""STUB: effect not implemented — do not guess mechanics.
Power Plant (SM10 #183): trainer effect stubbed.

Card text:
  - Pokémon-GX and Pokémon-EX in play (both yours and your opponent's) have no Abilities.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="247b5520-cbb1-5b07-8890-00e4bf8b64a4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=183,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
