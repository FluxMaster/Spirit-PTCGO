"""STUB: effect not implemented — do not guess mechanics.
Misty's Dewgong (GYM2 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50b79a97-2949-5632-a867-3717d18c8d1c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysDewgong.Name",
    display_name="Misty's Dewgong",
    searchable_by=["Misty's Dewgong", "Stage 1", "MistysDewgong"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysSeel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Ice Throw",
            game_text="If the Defending Pok\u00e9mon is Fighting, this attack's base damage is doubled.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Take Down",
            game_text="Misty's Dewgong does 20 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)