"""STUB: effect not implemented — do not guess mechanics.
Professor Elm's Lecture (SM8 #188a): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Pokémon with 60 HP or less, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="77a3fea0-b17b-573f-9dbd-2f80f71c884d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsLecture.Name",
    display_name="Professor Elm's Lecture",
    searchable_by=["Professor Elm's Lecture", "Supporter"],
    subtypes=["Supporter"],
    collector_number=239,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
