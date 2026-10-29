"""STUB: effect not implemented — do not guess mechanics.
Town Volunteers (ECARD2 #136): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Take 5 Baby Pokémon, Basic Pokémon, Evolution, and/or basic Energy cards from your discard pile and then show them to your opponent. Shuffle them into your deck.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5d9ef73a-c3e2-58c5-ab14-6f9d146b056c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownVolunteers.Name",
    display_name="Town Volunteers",
    searchable_by=["Town Volunteers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
