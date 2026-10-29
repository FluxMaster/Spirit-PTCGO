"""STUB: effect not implemented — do not guess mechanics.
Brock's Geodude (GYM2 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="29b13534-5891-54af-b7d2-31cdbfc88157",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGeodude.Name",
    display_name="Brock's Geodude",
    searchable_by=["Brock's Geodude", "Basic", "BrocksGeodude"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=74,
    abilities=[
        Attack(
            title="Rock Toss",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)