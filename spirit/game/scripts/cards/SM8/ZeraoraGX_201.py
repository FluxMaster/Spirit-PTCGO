"""STUB: effect not implemented — do not guess mechanics.
Zeraora-GX (SM8 #201): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fc459dbd-5b12-5d1b-95a7-8e26cd775a2f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraGX.Name",
    display_name="Zeraora-GX",
    searchable_by=["Zeraora-GX", "Basic", "GX", "ZeraoraGX"],
    subtypes=["Basic", "GX"],
    collector_number=201,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=807,
    abilities=[
        Ability(
            title="Thunderclap Zone",
            game_text="Each of your Pok\u00e9mon that has any Lightning Energy attached to it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Plasma Fists",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Full Voltage-GX",
            game_text="Attach 5 basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)