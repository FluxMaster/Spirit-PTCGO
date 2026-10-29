"""STUB: effect not implemented — do not guess mechanics.
Brock's Diglett (GYM2 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="24f0220e-cccf-5b1e-aee7-5346cc7fe6ab",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksDiglett.Name",
    display_name="Brock's Diglett",
    searchable_by=["Brock's Diglett", "Basic", "BrocksDiglett"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=50,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tremor",
            game_text="Does 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)