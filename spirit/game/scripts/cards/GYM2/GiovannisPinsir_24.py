"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Pinsir (GYM2 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d8f48dd7-cc11-55b6-b9f6-f95b90b23556",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisPinsir.Name",
    display_name="Giovanni's Pinsir",
    searchable_by=["Giovanni's Pinsir", "Basic", "GiovannisPinsir"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Snapping Pincers",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Overhead Toss",
            game_text="If you have any Benched Pok\u00e9mon, flip a coin. If tails, choose 1 of your Benched Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)