"""STUB: effect not implemented — do not guess mechanics.
Professor Elm's Training Method (ECARD1 #148): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="36532a6a-fb17-52bb-921d-8960bc799bae",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
