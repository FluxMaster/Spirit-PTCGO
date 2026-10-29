"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Abra (GYM2 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d72e4ce6-c7a4-5b5a-b5d6-f6a7026e35c9",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAbra.Name",
    display_name="Sabrina's Abra",
    searchable_by=["Sabrina's Abra", "Basic", "SabrinasAbra"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Synchronize",
            game_text="This attack can't be used unless Sabrina's Abra and the Defending Pok\u00e9mon have the same number of Energy cards attached to them.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)