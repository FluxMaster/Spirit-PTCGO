"""STUB: effect not implemented — do not guess mechanics.
Mount Lanakila (SM3 #118): trainer effect stubbed.

Card text:
  - The Retreat Cost of each Basic Pokémon in play (both yours and your opponent's) is Colorless more.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="80e89095-915b-574b-bdd4-5bc875641b9f",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MountLanakila.Name",
    display_name="Mount Lanakila",
    searchable_by=["Mount Lanakila", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
