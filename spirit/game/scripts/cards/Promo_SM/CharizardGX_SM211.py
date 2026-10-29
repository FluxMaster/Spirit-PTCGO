"""STUB: effect not implemented — do not guess mechanics.
Charizard-GX (Promo_SM #SM211): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48d45b43-9688-558a-88bc-02813df2dbb6",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGX.Name",
    display_name="Charizard-GX",
    searchable_by=["Charizard-GX", "Stage 2", "GX", "CharizardGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=211,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Flamethrower",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
        Attack(
            title="Flare Blitz-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=300,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)