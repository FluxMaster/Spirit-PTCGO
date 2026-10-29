"""STUB: effect not implemented — do not guess mechanics.
Relic Hunter (ECARD3 #120): trainer effect stubbed.

Card text:
  - You can play only 1 Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 Supporter and/or Stadium cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="426d434b-96f3-56a4-9227-e7ef2e735d67",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RelicHunter.Name",
    display_name="Relic Hunter",
    searchable_by=["Relic Hunter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
