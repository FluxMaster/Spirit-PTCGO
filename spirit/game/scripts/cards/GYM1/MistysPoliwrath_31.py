"""STUB: effect not implemented — do not guess mechanics.
Misty's Poliwrath (GYM1 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3a67e01-ded0-5ff3-bd4e-d71d77a3b340",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwrath.Name",
    display_name="Misty's Poliwrath",
    searchable_by=["Misty's Poliwrath", "Stage 2", "MistysPoliwrath"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Water Ring",
            game_text="Does 10 damage to each Pok\u00e9mon that isn't Water on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)