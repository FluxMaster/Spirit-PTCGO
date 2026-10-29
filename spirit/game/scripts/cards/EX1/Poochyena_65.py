"""STUB: effect not implemented — do not guess mechanics.
Poochyena (EX1 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45fb2973-84f2-5f8d-8022-e9dc4b9a4a62",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    display_name="Poochyena",
    searchable_by=["Poochyena", "Basic", "Poochyena"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=261,
    abilities=[
        Attack(
            title="Shadow Bind",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)