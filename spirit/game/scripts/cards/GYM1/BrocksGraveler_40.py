"""STUB: effect not implemented — do not guess mechanics.
Brock's Graveler (GYM1 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b8c1326-634e-586d-a171-1a89c7d0694f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGraveler.Name",
    display_name="Brock's Graveler",
    searchable_by=["Brock's Graveler", "Stage 1", "BrocksGraveler"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGeodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Rock Toss",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)