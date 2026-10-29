"""STUB: effect not implemented — do not guess mechanics.
Pachirisu (SM5 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c40d1739-36d7-5b6c-b434-5af818973c07",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=417,
    abilities=[
        Attack(
            title="Snuggly Generator",
            game_text="For each of your Benched Pok\u00e9mon that has the Nuzzle attack, search your deck for a Lightning Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Nuzzle",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)