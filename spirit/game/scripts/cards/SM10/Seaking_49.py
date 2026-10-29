"""STUB: effect not implemented — do not guess mechanics.
Seaking (SM10 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="805079e2-8ca3-56b6-8e02-f97ecb9a8c5f",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name",
    display_name="Seaking",
    searchable_by=["Seaking", "Stage 1", "Seaking"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    family_id=118,
    abilities=[
        Attack(
            title="Enhanced Horn",
            game_text="Flip 2 coins. This attack does 30 damage for each heads. If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, flip 6 coins instead.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)