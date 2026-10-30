"""STUB: effect not implemented — do not guess mechanics.
Glacia's Stadium (EX16 #76): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player's Water Pokémon (excluding Pokémon-ex) has no Weakness.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="4b488e3f-e650-59ad-9c65-a215393f3d1d",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlaciasStadium.Name",
    display_name="Glacia's Stadium",
    searchable_by=["Glacia's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
