"""STUB: effect not implemented — do not guess mechanics.
Erika's Exeggcute (GYM1 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d0f1309-5021-5403-a38c-0e6b5fd29df1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasExeggcute.Name",
    display_name="Erika's Exeggcute",
    searchable_by=["Erika's Exeggcute", "Basic", "ErikasExeggcute"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=102,
    abilities=[
        Attack(
            title="Deflector",
            game_text="During your opponent's next turn, whenever Erika's Exeggcute takes damage, divide that damage in half (rounded down to the nearest 10). (Any other effects still happen.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Egg Bomb",
            game_text="Flip a coin. If tails, this attack does nothing to the Defending Pok\u00e9mon and Erika's Exeggcute does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)