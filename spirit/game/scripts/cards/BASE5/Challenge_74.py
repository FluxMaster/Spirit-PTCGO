"""STUB: effect not implemented — do not guess mechanics.
Challenge! (BASE5 #74): trainer effect stubbed.

Card text:
  - Ask your opponent if he or she accepts your challenge. If your opponent declines (or if both Benches are full), draw 2 cards. If your opponent accepts, each of you searches your decks for any number of Basic Pokémon cards and puts them face down onto your Benches. (A player can't do this if his or her Bench is full.) When you both have finished, shuffle your decks and turn those cards face up.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2060a7ff-2386-56b3-ab9f-416fdac1b1a9",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Challenge.Name",
    display_name="Challenge!",
    searchable_by=["Challenge!"],
    subtypes=[],
    collector_number=74,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
