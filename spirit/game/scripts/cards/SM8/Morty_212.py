"""STUB: effect not implemented — do not guess mechanics.
Morty (SM8 #212): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Psychic Pokémon was Knocked Out during your opponent's last turn.
  - Your opponent reveals their hand. Choose 2 cards you find there. Your opponent shuffles those cards into their deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3fcfcc80-8445-5c61-9a80-8610a08e7e1f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morty.Name",
    display_name="Morty",
    searchable_by=["Morty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=212,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
