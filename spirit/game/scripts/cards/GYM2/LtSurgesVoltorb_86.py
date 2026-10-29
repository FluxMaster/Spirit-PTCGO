"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Voltorb (GYM2 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a68d9b5-d14f-5c65-a307-a557db78ab29",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesVoltorb.Name",
    display_name="Lt. Surge's Voltorb",
    searchable_by=["Lt. Surge's Voltorb", "Basic", "LtSurgesVoltorb"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Bouncing Ball",
            game_text="Flip a coin. If tails, Lt. Surge's Voltorb does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)