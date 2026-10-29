"""STUB: effect not implemented — do not guess mechanics.
Reshiram-GX (Promo_SM #SM137): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d406bd43-81a2-5c6c-9a3a-bf65d2018e56",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramGX.Name",
    display_name="Reshiram-GX",
    searchable_by=["Reshiram-GX", "Basic", "GX", "ReshiramGX"],
    subtypes=["Basic", "GX"],
    collector_number=137,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for up to 2 Fire Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Column",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Vermilion-GX",
            game_text="You may attach up to 5 Fire Energy cards from your hand to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)