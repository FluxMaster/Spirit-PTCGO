"""STUB: effect not implemented — do not guess mechanics.
Dragonite-GX (Promo_SM #SM156): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cd923f5-73c1-57db-869e-e52c094162ef",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteGX.Name",
    display_name="Dragonite-GX",
    searchable_by=["Dragonite-GX", "Stage 2", "GX", "DragoniteGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=156,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragonporter-GX",
            game_text="Put 3 Dragon Pok\u00e9mon from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)