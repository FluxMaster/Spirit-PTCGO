"""STUB: effect not implemented — do not guess mechanics.
Poké Maniac (SM11 #204): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Pokémon that have a Retreat Cost of exactly 4, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="34c81731-196f-51d0-b671-e79bf01a74b0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeManiac.Name",
    display_name="Poké Maniac",
    searchable_by=["Pok\u00e9 Maniac", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
