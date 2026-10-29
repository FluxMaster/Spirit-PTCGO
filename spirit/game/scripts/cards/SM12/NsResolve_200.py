"""STUB: effect not implemented — do not guess mechanics.
N's Resolve (SM12 #200): trainer effect stubbed.

Card text:
  - Discard the top 6 cards of your deck. If any of those cards are basic Energy cards, attach them to 1 of your Benched Dragon Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="274dde60-f147-5ff6-8a63-ebc1e5b0f749",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsResolve.Name",
    display_name="N's Resolve",
    searchable_by=["N's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
