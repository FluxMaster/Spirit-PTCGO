"""STUB: effect not implemented — do not guess mechanics.
Pokémon Breeder (BASE1 #76): trainer effect stubbed.

Card text:
  - Put a Stage 2 Evolution card from your hand on the matching Basic Pokémon. You can only play this card when you would be allowed to evolve that Pokémon anyway.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="29584248-5400-52cf-a06d-6585ea159f1b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder"],
    subtypes=[],
    collector_number=76,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
