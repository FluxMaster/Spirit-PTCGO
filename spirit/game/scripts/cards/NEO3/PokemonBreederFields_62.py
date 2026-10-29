"""STUB: effect not implemented — do not guess mechanics.
Pokémon Breeder Fields (NEO3 #62): trainer effect stubbed.

Card text:
  - Flip a coin for 1 or 2 of your non-Baby Pokémon that can evolve. For each heads, search your deck for a later-Stage card that matches that Pokémon. Then put that card into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8090d85b-69f9-5447-b33f-50706305fadc",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreederFields.Name",
    display_name="Pokémon Breeder Fields",
    searchable_by=["Pok\u00e9mon Breeder Fields"],
    subtypes=[],
    collector_number=62,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
