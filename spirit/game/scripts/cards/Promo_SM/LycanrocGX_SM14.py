"""STUB: effect not implemented — do not guess mechanics.
Lycanroc-GX (Promo_SM #SM14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d61e758-2a44-5767-b3da-ddcc84805658",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=14,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Accelerock",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Lycanfang-GX",
            game_text="Discard 2 Energy from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)