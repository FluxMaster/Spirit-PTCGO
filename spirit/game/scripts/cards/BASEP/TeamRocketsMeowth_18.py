"""STUB: effect not implemented — do not guess mechanics.
Team Rocket's Meowth (BASEP #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb39866f-97e4-5d09-bfc8-8209a92272ef",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMeowth.Name",
    display_name="Team Rocket's Meowth",
    searchable_by=["Team Rocket's Meowth", "Basic", "TeamRocketsMeowth"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Miraculous Comeback",
            game_text="Flip a number of coins equal to the number of Pok\u00e9mon in play. This attack does 10 damage times the number of heads. Then Team Rocket's Meowth does 10 damage times the number of tails to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)