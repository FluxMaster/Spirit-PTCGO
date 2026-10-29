"""STUB: effect not implemented — do not guess mechanics.
Molayne (SM10 #181): trainer effect stubbed.

Card text:
  - You can play this card only if you discard 2 Metal Energy cards from your hand.
  - Shuffle a Trainer card from your discard pile into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="dfe1a87f-2507-5d8a-a85b-5e03f17d3f63",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Molayne.Name",
    display_name="Molayne",
    searchable_by=["Molayne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
