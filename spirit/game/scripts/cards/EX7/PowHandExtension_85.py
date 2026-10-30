"""STUB: effect not implemented — do not guess mechanics.
Pow! Hand Extension (EX7 #85): trainer effect stubbed.

Card text:
  - You may use this card only if you have more Prize cards left than your opponent.
  - Move 1 Energy card attached to the Defending Pokémon to another of your opponent's Pokémon. Or, switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon. Your opponent chooses the Defending Pokémon to switch.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7e5e9565-b7a2-5ea7-9eab-5f90610f75d8",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowHandExtension.Name",
    display_name="Pow! Hand Extension",
    searchable_by=["Pow! Hand Extension", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=85,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
