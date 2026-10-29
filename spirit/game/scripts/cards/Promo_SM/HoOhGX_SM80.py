"""STUB: effect not implemented — do not guess mechanics.
Ho-Oh-GX (Promo_SM #SM80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c1290a7-11d7-50cd-807f-c5f42d71e783",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhGX.Name",
    display_name="Ho-Oh-GX",
    searchable_by=["Ho-Oh-GX", "Basic", "GX", "HoOhGX"],
    subtypes=["Basic", "GX"],
    collector_number=80,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Fire",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Phoenix Burn",
            game_text="This Pok\u00e9mon can't use Phoenix Burn during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Eternal Light-GX",
            game_text="Put 3 in any combination of Fire Pok\u00e9mon-GX or Fire Pok\u00e9mon-EX from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)