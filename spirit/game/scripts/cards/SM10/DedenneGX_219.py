"""STUB: effect not implemented — do not guess mechanics.
Dedenne-GX (SM10 #219): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e5fc70af-0a6c-5c35-b50f-00379a8016e9",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DedenneGX.Name",
    display_name="Dedenne-GX",
    searchable_by=["Dedenne-GX", "Basic", "GX", "DedenneGX"],
    subtypes=["Basic", "GX"],
    collector_number=219,
    set_code="SM10",
    rarity=Rarities.RareRainbow,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Ability(
            title="Dedechange",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard your hand and draw 6 cards. You can't use more than 1 Dedechange Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Tingly Return-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. Put this Pok\u00e9mon and all cards attached to it into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)