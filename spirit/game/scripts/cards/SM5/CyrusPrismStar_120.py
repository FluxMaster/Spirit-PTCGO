"""STUB: effect not implemented — do not guess mechanics.
Cyrus {*} (SM5 #120): trainer effect stubbed.

Card text:
  - You can play this card only if your Active Pokémon is a Water or Metal Pokémon.
  - Your opponent chooses 2 Benched Pokémon and shuffles the others, and all cards attached to them, into their deck.
  - You may play only 1 Supporter card during your turn (before your attack).
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4e7ff502-56ef-5e9c-aaaf-42e068e827a4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyrusPrismStar.Name",
    display_name="Cyrus {*}",
    searchable_by=["Cyrus {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=120,
    set_code="SM5",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
