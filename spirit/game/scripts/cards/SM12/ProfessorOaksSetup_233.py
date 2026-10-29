"""STUB: effect not implemented — do not guess mechanics.
Professor Oak's Setup (SM12 #233): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Basic Pokémon of different types and put them onto your Bench. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="aafdd31e-3a3b-58fa-a406-3eb3bd99f3ab",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name",
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=233,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
