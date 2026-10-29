"""STUB: effect not implemented — do not guess mechanics.
Aether Paradise Conservation Area (HF #SV87): trainer effect stubbed.

Card text:
  - Basic Grass and Basic Lightning Pokémon (both yours and your opponent's) take 30 less damage from the opponent's attacks (after applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="cbac4046-2668-59a5-b542-d1518ce3bc41",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name",
    display_name="Aether Paradise Conservation Area",
    searchable_by=["Aether Paradise Conservation Area", "Stadium"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="HF",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
