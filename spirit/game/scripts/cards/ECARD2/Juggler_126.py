"""STUB: effect not implemented — do not guess mechanics.
Juggler (ECARD2 #126): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard up to 2 basic Energy cards from your hand. If you discarded 1 basic Energy card, draw 3 cards. If you discarded 2 basic Energy cards, draw 5 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7c18debc-aa03-5c09-bcbc-d2590b55bd96",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Juggler.Name",
    display_name="Juggler",
    searchable_by=["Juggler", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
