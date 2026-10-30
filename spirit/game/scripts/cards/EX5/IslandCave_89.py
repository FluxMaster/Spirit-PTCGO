"""STUB: effect not implemented — do not guess mechanics.
Island Cave (EX5 #89): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Whenever any player attaches an Energy card from his or her hand to Water Pokémon, Fighting Pokémon, or Metal Pokémon, remove any Special Conditions from that Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="92a822a3-e4e5-5d8e-b154-743db8902ecf",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandCave.Name",
    display_name="Island Cave",
    searchable_by=["Island Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
