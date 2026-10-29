"""STUB: effect not implemented — do not guess mechanics.
Pokémon Flute (BASE1 #86): trainer effect stubbed.

Card text:
  - Choose 1 Basic Pokémon card from your opponent's discard pile and put it onto his or her Bench. (You can't play Pokémon Flute if your opponent's Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c0600115-ca94-5116-8c10-f7105ac806f4",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFlute.Name",
    display_name="Pokémon Flute",
    searchable_by=["Pok\u00e9mon Flute"],
    subtypes=[],
    collector_number=86,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
