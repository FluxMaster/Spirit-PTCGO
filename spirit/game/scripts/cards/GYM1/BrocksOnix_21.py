"""STUB: effect not implemented — do not guess mechanics.
Brock's Onix (GYM1 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98f07aaf-d8bc-5f6d-b2dd-ab4e9eff35fb",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksOnix.Name",
    display_name="Brock's Onix",
    searchable_by=["Brock's Onix", "Basic", "BrocksOnix"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tunneling",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose up to 2 of them. This attack does 20 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Brock's Onix can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)