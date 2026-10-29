"""STUB: effect not implemented — do not guess mechanics.
Grubbin (SM10 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a64627b2-85d7-531a-a58a-372a8a26bba5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    display_name="Grubbin",
    searchable_by=["Grubbin", "Basic", "Grubbin"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=736,
    abilities=[
        Attack(
            title="Electrical Signal",
            game_text="Search your deck for up to 2 Lightning Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)