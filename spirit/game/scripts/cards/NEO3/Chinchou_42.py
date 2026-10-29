"""STUB: effect not implemented — do not guess mechanics.
Chinchou (NEO3 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d9d88eb3-4217-5007-b71f-9b93ee9ef397",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic", "Chinchou"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=170,
    abilities=[
        Attack(
            title="Positive Ion",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage. If tails, this attack does 10 damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Negative Ion",
            game_text="If the Defending Pok\u00e9mon attacks Chinchou during your opponent's next turn, any damage done to Chinchou is reduced by 10 (before applying Weakness and Resistance). (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)