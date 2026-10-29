"""STUB: effect not implemented — do not guess mechanics.
Brock's Mankey (GYM1 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16c75ec8-108c-56d4-b64d-0fa6ede24fbf",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksMankey.Name",
    display_name="Brock's Mankey",
    searchable_by=["Brock's Mankey", "Basic", "BrocksMankey"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Fidget",
            game_text="Shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Karate Chop",
            game_text="Does 40 damage minus 10 damage for each damage counter on Brock's Mankey.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)