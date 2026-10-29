"""STUB: effect not implemented — do not guess mechanics.
Misty's Cerulean City Gym (HF #61): trainer effect stubbed.

Card text:
  - The attacks of Starmie-GX (both yours and your opponent's) do 40 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="b418c08c-3243-5178-9945-39d37e5730f1",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysCeruleanCityGym.Name",
    display_name="Misty's Cerulean City Gym",
    searchable_by=["Misty's Cerulean City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
