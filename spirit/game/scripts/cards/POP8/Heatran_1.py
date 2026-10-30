"""STUB: effect not implemented — do not guess mechanics.
Heatran (POP8 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="82160dbe-57d4-5682-b608-185d42b2d112",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic", "Heatran"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="POP8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Basic Energy cards attached to Heatran. (If you can't discard cards, this attack does nothing.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)