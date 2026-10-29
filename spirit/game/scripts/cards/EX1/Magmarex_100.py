"""STUB: effect not implemented — do not guess mechanics.
Magmar ex (EX1 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6a35759-74d2-507e-b8b0-bc8b6d72dc0c",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmarex.Name",
    display_name="Magmar ex",
    searchable_by=["Magmar ex", "Basic", "ex", "Magmarex"],
    subtypes=["Basic", "ex"],
    collector_number=100,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Super Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)