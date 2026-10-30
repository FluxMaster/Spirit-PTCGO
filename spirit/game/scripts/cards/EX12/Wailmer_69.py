"""STUB: effect not implemented — do not guess mechanics.
Wailmer (EX12 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30f52cbb-c8b2-5fde-9087-165bf7c78792",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=320,
    abilities=[
        Attack(
            title="Double Tackle",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)