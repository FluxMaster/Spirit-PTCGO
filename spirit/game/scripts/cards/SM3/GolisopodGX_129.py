"""STUB: effect not implemented — do not guess mechanics.
Golisopod-GX (SM3 #129): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="15191989-67ce-5628-969d-03243592e1c4",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GolisopodGX.Name",
    display_name="Golisopod-GX",
    searchable_by=["Golisopod-GX", "Stage 1", "GX", "GolisopodGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=129,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="First Impression",
            game_text="If this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Armor Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Crossing Cut-GX",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)