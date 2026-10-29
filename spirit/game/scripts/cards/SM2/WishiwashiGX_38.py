"""STUB: effect not implemented — do not guess mechanics.
Wishiwashi-GX (SM2 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="da7ea9c3-a0f9-5708-bc7a-aeb7a079209a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WishiwashiGX.Name",
    display_name="Wishiwashi-GX",
    searchable_by=["Wishiwashi-GX", "Basic", "GX", "WishiwashiGX"],
    subtypes=["Basic", "GX"],
    collector_number=38,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Torrential Vortex",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Blue Surge-GX",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=220,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)