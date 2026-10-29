"""STUB: effect not implemented — do not guess mechanics.
Misty's Psyduck (GYM1 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3221de7-403d-5312-947c-1127a3609db1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPsyduck.Name",
    display_name="Misty's Psyduck",
    searchable_by=["Misty's Psyduck", "Basic", "MistysPsyduck"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Call for Friend",
            game_text="Flip a coin. If heads, you may search your deck for a Basic Pok\u00e9mon with Misty in its name and put it onto your Bench. (You can't use this attack if your Bench is full.) Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)