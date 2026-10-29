"""STUB: effect not implemented — do not guess mechanics.
Ariados (SM7 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="efd93e1c-7a4b-5865-9eef-d172f84fae42",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Reactive Poison",
            game_text="This attack does 50 more damage for each Special Condition affecting your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spider Trap",
            game_text="You may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)