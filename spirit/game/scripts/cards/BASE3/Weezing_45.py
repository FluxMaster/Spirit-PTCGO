"""STUB: effect not implemented — do not guess mechanics.
Weezing (BASE3 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6c005f6-0c4e-5979-85b3-0c604512ca13",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=110,
    abilities=[
        Attack(
            title="Smog",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 10 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Weezing does 60 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)