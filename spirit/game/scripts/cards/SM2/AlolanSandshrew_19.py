"""STUB: effect not implemented — do not guess mechanics.
Alolan Sandshrew (SM2 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c50c7425-dc1b-5df3-b348-126ce210fb74",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    display_name="Alolan Sandshrew",
    searchable_by=["Alolan Sandshrew", "Basic", "AlolanSandshrew"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=27,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)