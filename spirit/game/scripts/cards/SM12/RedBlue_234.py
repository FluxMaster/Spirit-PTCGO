"""STUB: effect not implemented — do not guess mechanics.
Red & Blue (SM12 #234): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon-GX that evolves from 1 of your Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck. (You can't use this card during your first turn or on a Pokémon that was put into play this turn.)
  - When you play this card, you may discard 2 other cards from your hand. If you do, search your deck for up to 2 basic Energy cards and attach them to the Pokémon you evolved in this way.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="42a54f77-ffd1-51ac-8175-70de265f2b2c",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedBlue.Name",
    display_name="Red & Blue",
    searchable_by=["Red & Blue", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=234,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
