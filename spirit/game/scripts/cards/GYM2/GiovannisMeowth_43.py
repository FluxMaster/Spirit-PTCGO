"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Meowth (GYM2 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5743de5-b474-5905-96a7-0526f640f853",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMeowth.Name",
    display_name="Giovanni's Meowth",
    searchable_by=["Giovanni's Meowth", "Basic", "GiovannisMeowth"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="False Charity",
            game_text="Flip a coin. If heads, look at the top card of your opponent's deck. If it's a Trainer card, put it in your opponent's discard pile; otherwise, put it into his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)