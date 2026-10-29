"""STUB: effect not implemented — do not guess mechanics.
Professor Oak's Setup (SM12 #201): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Basic Pokémon of different types and put them onto your Bench. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4d13404d-e3ba-599c-9796-9bd2c3ac4808",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name",
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
