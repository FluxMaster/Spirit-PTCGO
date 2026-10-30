"""STUB: effect not implemented — do not guess mechanics.
Wigglytuff ex (EX5 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d20a36af-8038-5a1a-a0b8-4d2f61c54395",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuffex.Name",
    display_name="Wigglytuff ex",
    searchable_by=["Wigglytuff ex", "Stage 1", "ex", "Wigglytuffex"],
    subtypes=["Stage 1", "ex"],
    collector_number=101,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Sleepy Song",
            game_text="Each Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Do the Wave",
            game_text="Does 30 damage plus 10 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)