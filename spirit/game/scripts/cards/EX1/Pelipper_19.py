"""STUB: effect not implemented — do not guess mechanics.
Pelipper (EX1 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d11a5f29-5f0b-51b2-b348-77e3a8c9cc05",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=278,
    abilities=[
        Attack(
            title="Stockpile",
            game_text="During your next turn, Spit Up's base damage is 70 instead of 30, and Swallow's base damage is 60 instead of 20.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spit Up",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Swallow",
            game_text="After your attack, remove from Pelipper the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon. If Pelipper has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)