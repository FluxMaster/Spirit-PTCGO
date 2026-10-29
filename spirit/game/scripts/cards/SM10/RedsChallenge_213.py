"""STUB: effect not implemented — do not guess mechanics.
Red's Challenge (SM10 #213): trainer effect stubbed.

Card text:
  - You can play this card only if you discard 2 other cards from your hand.
  - Search your deck for a card and put it into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1c25a0e6-dc5b-5480-98b2-48cb7264aa8e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedsChallenge.Name",
    display_name="Red's Challenge",
    searchable_by=["Red's Challenge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=213,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
