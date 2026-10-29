"""STUB: effect not implemented — do not guess mechanics.
Hitmonchan ex (EX1 #98): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86ead38f-ab05-59ad-a84c-c883884f3846",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchanex.Name",
    display_name="Hitmonchan ex",
    searchable_by=["Hitmonchan ex", "Basic", "ex", "Hitmonchanex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Steady Punch",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sky Uppercut",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)