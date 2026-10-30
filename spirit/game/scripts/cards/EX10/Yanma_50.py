"""STUB: effect not implemented — do not guess mechanics.
Yanma (EX10 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f718f3e5-17f4-5b84-859c-04adf4e43b4e",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic", "Yanma"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=193,
    abilities=[
        Attack(
            title="Grand Loop",
            game_text="Draw 2 cards. You may switch Yanma with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Tail",
            game_text="Flip a coin. If heads, this attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)