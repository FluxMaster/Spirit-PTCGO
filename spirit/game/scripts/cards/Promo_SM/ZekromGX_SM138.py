"""STUB: effect not implemented — do not guess mechanics.
Zekrom-GX (Promo_SM #SM138): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48930db6-53ac-50f4-a169-0e798737cd29",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZekromGX.Name",
    display_name="Zekrom-GX",
    searchable_by=["Zekrom-GX", "Basic", "GX", "ZekromGX"],
    subtypes=["Basic", "GX"],
    collector_number=138,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=644,
    abilities=[
        Attack(
            title="Bullet Uppercut",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-GX or a Pok\u00e9mon-EX, this attack does 60 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Swift Bolt Strike",
            game_text="Flip 2 coins. This attack does 60 more damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rampage Bolt-GX",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)