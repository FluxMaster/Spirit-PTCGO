"""STUB: effect not implemented — do not guess mechanics.
Drake's Stadium (EX16 #72): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Any damage done to Colorless Active Pokémon (both yours and your opponent's) by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="4e066e60-33ce-58e7-9b45-653258aef9ce",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DrakesStadium.Name",
    display_name="Drake's Stadium",
    searchable_by=["Drake's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=72,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
