"""STUB: effect not implemented — do not guess mechanics.
Shellder (BASE3 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64f2b5bd-f64f-5e8f-b731-eac78aa17f13",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    display_name="Shellder",
    searchable_by=["Shellder", "Basic", "Shellder"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=90,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hide in Shell",
            game_text="Flip a coin. If heads, prevent all damage done to Shellder during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)