"""STUB: effect not implemented — do not guess mechanics.
Wailmer (SM7 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6b0d3ed-c54b-5559-ab97-a39304cec8db",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=320,
    abilities=[
        Attack(
            title="Wave Swallower",
            game_text="Flip a coin until you get tails. For each heads, heal 50 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)