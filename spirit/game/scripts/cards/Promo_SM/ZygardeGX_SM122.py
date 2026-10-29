"""STUB: effect not implemented — do not guess mechanics.
Zygarde-GX (Promo_SM #SM122): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5a96fb64-d01d-5301-962a-7f4222ed7189",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name",
    display_name="Zygarde-GX",
    searchable_by=["Zygarde-GX", "Basic", "GX", "ZygardeGX"],
    subtypes=["Basic", "GX"],
    collector_number=122,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Vibration",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Cell Storm",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Liberation-GX",
            game_text="Your opponent reveals their hand. This attack does 120 damage for each Energy card you find there. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)