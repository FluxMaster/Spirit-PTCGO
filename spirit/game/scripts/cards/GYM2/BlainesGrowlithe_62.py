"""STUB: effect not implemented — do not guess mechanics.
Blaine's Growlithe (GYM2 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff8ec12b-a8fc-585e-ab0d-b96d8f4cbe8c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    display_name="Blaine's Growlithe",
    searchable_by=["Blaine's Growlithe", "Basic", "BlainesGrowlithe"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Stoke",
            game_text="Search your deck for a Fire Energy card and attach it to Blaine's Growlithe. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)