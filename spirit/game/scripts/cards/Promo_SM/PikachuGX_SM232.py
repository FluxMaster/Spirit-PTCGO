"""STUB: effect not implemented — do not guess mechanics.
Pikachu-GX (Promo_SM #SM232): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="157f63f6-a043-5dc0-a2a7-2a8d34f86013",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuGX.Name",
    display_name="Pikachu-GX",
    searchable_by=["Pikachu-GX", "Basic", "GX", "PikachuGX"],
    subtypes=["Basic", "GX"],
    collector_number=232,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Volt Tackle",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tail Break-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)