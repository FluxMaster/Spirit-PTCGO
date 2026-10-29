"""STUB: effect not implemented — do not guess mechanics.
Lapras ex (EX1 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bce2d383-e9ea-5331-8036-d3957c02ce5b",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Laprasex.Name",
    display_name="Lapras ex",
    searchable_by=["Lapras ex", "Basic", "ex", "Laprasex"],
    subtypes=["Basic", "ex"],
    collector_number=99,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Energy Ball",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Lapras ex but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Confuse Ray",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)