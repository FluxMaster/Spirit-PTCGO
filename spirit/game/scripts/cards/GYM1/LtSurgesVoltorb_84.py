"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Voltorb (GYM1 #84): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="456792c8-64cd-5682-91be-3f7bb6ab887e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesVoltorb.Name",
    display_name="Lt. Surge's Voltorb",
    searchable_by=["Lt. Surge's Voltorb", "Basic", "LtSurgesVoltorb"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Spin Ball",
            game_text="Flip 1 coin. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)