"""STUB: effect not implemented — do not guess mechanics.
Xurkitree-GX (SM5 #160): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="94b817e3-38b7-5ec0-abb6-26391c0e4430",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XurkitreeGX.Name",
    display_name="Xurkitree-GX",
    searchable_by=["Xurkitree-GX", "Basic", "GX", "Ultra Beast", "XurkitreeGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=160,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=796,
    abilities=[
        Ability(
            title="Flashing Head",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have any Special Energy attached to them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rumbling Wires",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lighting-GX",
            game_text="Your opponent reveals their hand. Add a card you find there to their Prize cards face down. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)