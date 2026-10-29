"""STUB: effect not implemented — do not guess mechanics.
Incineroar-GX (Promo_SM #SM38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="33f61adf-d462-5d97-a05b-5dcfff32361c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarGX.Name",
    display_name="Incineroar-GX",
    searchable_by=["Incineroar-GX", "Stage 2", "GX", "IncineroarGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=38,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=727,
    abilities=[
        Attack(
            title="Hustling Strike",
            game_text="This attack does 20 more damage for each of your Benched Fire Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tiger Swing",
            game_text="Flip 2 coins. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Burning Slam-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)