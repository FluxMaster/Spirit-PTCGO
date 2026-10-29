"""STUB: effect not implemented — do not guess mechanics.
Eevee & Snorlax-GX (SM9 #120): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5e70b586-0ebc-5707-8d64-64ec695892a8",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeSnorlaxGX.Name",
    display_name="Eevee & Snorlax-GX",
    searchable_by=["Eevee & Snorlax-GX", "Basic", "TAG TEAM", "GX", "EeveeSnorlaxGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=120,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Attach an Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dump Truck Press",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Megaton Friends-GX",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), draw cards until you have 10 cards in your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=210,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)