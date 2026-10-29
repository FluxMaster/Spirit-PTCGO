"""STUB: effect not implemented — do not guess mechanics.
Raikou-GX (Promo_SM #SM121): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dm import bolt_strike


card = PokemonCardDef(
    guid="7232ee98-1a1f-51ba-bfc7-f25f1b6e404c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaikouGX.Name",
    display_name="Raikou-GX",
    searchable_by=["Raikou-GX", "Basic", "GX", "RaikouGX"],
    subtypes=["Basic", "GX"],
    collector_number=121,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Attack(
            title="Dig Claws",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=bolt_strike,
        ),
        Attack(
            title="Thunderous Rain-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon that has any Energy attached to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 4},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)