"""STUB: effect not implemented — do not guess mechanics.
Brock's Pewter City Gym (HF #54): trainer effect stubbed.

Card text:
  - Onix-GX (both yours and your opponent's) take 40 less damage from the opponent's attacks (after applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f9b480aa-f3b2-5e27-95aa-b816005f0e33",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksPewterCityGym.Name",
    display_name="Brock's Pewter City Gym",
    searchable_by=["Brock's Pewter City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=54,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
