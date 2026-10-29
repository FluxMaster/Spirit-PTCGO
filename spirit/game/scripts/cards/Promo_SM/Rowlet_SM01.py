"""STUB: effect not implemented — do not guess mechanics.
Rowlet (Promo_SM #SM01): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="021be855-441f-53b5-86e9-ea55c93ad927",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    display_name="Rowlet",
    searchable_by=["Rowlet", "Basic", "Rowlet"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)