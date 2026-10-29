"""STUB: effect not implemented — do not guess mechanics.
Wartortle (SM10 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b6753f27-c35f-533e-be65-bcc14ab2a51a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name="Wartortle",
    searchable_by=["Wartortle", "Stage 1", "Wartortle"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Slash",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)