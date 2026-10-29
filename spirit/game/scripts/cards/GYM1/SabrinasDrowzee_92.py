"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Drowzee (GYM1 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="411e8871-3016-5191-a93f-69ed9b7c8bac",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasDrowzee.Name",
    display_name="Sabrina's Drowzee",
    searchable_by=["Sabrina's Drowzee", "Basic", "SabrinasDrowzee"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Suggestion",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)