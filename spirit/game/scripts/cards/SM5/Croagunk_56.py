"""STUB: effect not implemented — do not guess mechanics.
Croagunk (SM5 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c331173-0a0d-53e0-9082-c0aa73d4ec06",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic", "Croagunk"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Swagger",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)