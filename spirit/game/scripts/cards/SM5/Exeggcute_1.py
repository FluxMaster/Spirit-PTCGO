"""STUB: effect not implemented — do not guess mechanics.
Exeggcute (SM5 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d8b764bc-7818-53b5-974d-0e2f5cca4212",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic", "Exeggcute"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=102,
    abilities=[
        Attack(
            title="Continuous Eggsplosion",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)