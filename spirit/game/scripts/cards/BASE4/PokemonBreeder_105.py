"""STUB: effect not implemented — do not guess mechanics.
Pokémon Breeder (BASE4 #105): trainer effect stubbed.

Card text:
  - Put a Stage 2 Evolution card from your hand on the matching Basic Pokémon. You can only play this card when you would be allowed to evolve that Pokémon anyway.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="16a36a55-836c-5f77-86ae-db29a5e8637c",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder"],
    subtypes=[],
    collector_number=105,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
