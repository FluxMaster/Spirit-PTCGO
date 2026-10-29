"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Meowth (GYM2 #74): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2f592d4e-cd84-511b-94b9-2c729221f5ab",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMeowth.Name",
    display_name="Giovanni's Meowth",
    searchable_by=["Giovanni's Meowth", "Basic", "GiovannisMeowth"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Cat Fleas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cat Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)