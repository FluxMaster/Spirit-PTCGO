"""STUB: effect not implemented — do not guess mechanics.
Primarina-GX (Promo_SM #SM39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a58d58f8-c280-5a1a-9a3c-03b6790b962d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimarinaGX.Name",
    display_name="Primarina-GX",
    searchable_by=["Primarina-GX", "Stage 2", "GX", "PrimarinaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=39,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=730,
    abilities=[
        Attack(
            title="Bubble Beat",
            game_text="This attack does 20 more damage times the amount of Water Energy attached to your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Roaring Seas",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Grand Echo-GX",
            game_text="Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)