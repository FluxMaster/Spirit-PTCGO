"""STUB: effect not implemented — do not guess mechanics.
Brock's Sandslash (GYM1 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="56391853-75f0-5bf3-b0e0-4455b5a17017",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksSandslash.Name",
    display_name="Brock's Sandslash",
    searchable_by=["Brock's Sandslash", "Stage 1", "BrocksSandslash"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksSandshrew.Name",
    family_id=27,
    abilities=[
        Attack(
            title="Needles",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sandstorm",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)