"""STUB: effect not implemented — do not guess mechanics.
Power Plant (SM12 #269): trainer effect stubbed.

Card text:
  - Pokémon-GX and Pokémon-EX in play (both yours and your opponent's) have no Abilities.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e8a68e1d-2d9b-5b51-8acc-21cdd274776a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=269,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
