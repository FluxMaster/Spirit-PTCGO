"""STUB: effect not implemented — do not guess mechanics.
Charizard-GX (Promo_SM #SM60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c72fc37-6481-5f47-a3e5-97fa88c7d328",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGX.Name",
    display_name="Charizard-GX",
    searchable_by=["Charizard-GX", "Stage 2", "GX", "CharizardGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=60,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
        Attack(
            title="Crimson Storm",
            game_text="Discard 3 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=300,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Raging Out-GX",
            game_text="Discard the top 10 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)