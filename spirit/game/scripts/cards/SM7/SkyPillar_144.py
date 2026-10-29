"""STUB: effect not implemented — do not guess mechanics.
Sky Pillar (SM7 #144): trainer effect stubbed.

Card text:
  - Prevent all effects of the opponent's attacks, including damage, done to Benched Pokémon (both yours and your opponent's).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="6b6b2fa4-989e-5220-9ea1-5610e33a303e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyPillar.Name",
    display_name="Sky Pillar",
    searchable_by=["Sky Pillar", "Stadium"],
    subtypes=["Stadium"],
    collector_number=144,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
