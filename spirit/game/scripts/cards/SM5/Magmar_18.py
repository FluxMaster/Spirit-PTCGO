"""STUB: effect not implemented — do not guess mechanics.
Magmar (SM5 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4950c8e0-5ef0-5623-9065-c0b976a2f7f2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Controlled Burn",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)