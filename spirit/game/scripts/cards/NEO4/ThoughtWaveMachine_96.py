"""STUB: effect not implemented — do not guess mechanics.
Thought Wave Machine (NEO4 #96): trainer effect stubbed.

Card text:
  - Flip a coin until you get tails. For each heads, return an Energy card attached to your opponent's Active Pokémon to your opponent's hand. If the Pokémon has fewer attached Energy cards than that, return all of them to your opponent's hand. Your turn is over now (you don't get to attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="98ec0812-e124-51e7-ad24-93e77612bb91",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThoughtWaveMachine.Name",
    display_name="Thought Wave Machine",
    searchable_by=["Thought Wave Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=96,
    set_code="NEO4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
