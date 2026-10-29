"""STUB: effect not implemented — do not guess mechanics.
Chansey (BASE4 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4debeb28-62fa-5017-8a22-3013c3cb6a90",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=113,
    abilities=[
        Attack(
            title="Scrunch",
            game_text="Flip a coin. If heads, prevent all damage done to Chansey during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Chansey does 80 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)