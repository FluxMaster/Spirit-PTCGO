"""STUB: effect not implemented — do not guess mechanics.
Flareon-GX (Promo_SM #SM171): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d64e09fa-2b87-595d-bfbd-6de809a1582e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonGX.Name",
    display_name="Flareon-GX",
    searchable_by=["Flareon-GX", "Stage 1", "GX", "FlareonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=171,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Heat Stage",
            game_text="You may attach up to 3 Fire Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Burner-GX",
            game_text="This attack does 20 damage for each Fire Energy card in your discard pile. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)