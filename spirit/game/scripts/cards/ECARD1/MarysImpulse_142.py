"""STUB: effect not implemented — do not guess mechanics.
Mary's Impulse (ECARD1 #142): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Flip a coin until you get tails. For each heads, draw 2 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="91e720d8-9311-56cb-ae4e-b30e4218c729",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarysImpulse.Name",
    display_name="Mary's Impulse",
    searchable_by=["Mary's Impulse", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
