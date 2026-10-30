"""STUB: effect not implemented — do not guess mechanics.
Sidney's Stadium (EX16 #82): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player's Darkness Pokémon can't be Asleep, Confused, or Paralyzed.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="755abe03-b6d9-5bf6-b528-7d69d32a5e04",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SidneysStadium.Name",
    display_name="Sidney's Stadium",
    searchable_by=["Sidney's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
