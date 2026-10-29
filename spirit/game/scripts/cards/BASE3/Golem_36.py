"""STUB: effect not implemented — do not guess mechanics.
Golem (BASE3 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5362e7e-9a23-5934-9fcc-657b33a929f7",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name",
    display_name="Golem",
    searchable_by=["Golem", "Stage 2", "Golem"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Avalanche",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 20 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Golem does 100 damage to itself.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)