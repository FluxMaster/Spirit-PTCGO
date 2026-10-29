"""STUB: effect not implemented — do not guess mechanics.
Nihilego-GX (HF #SV62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="37485203-2765-52f0-99e8-f8e65e9bd995",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NihilegoGX.Name",
    display_name="Nihilego-GX",
    searchable_by=["Nihilego-GX", "Basic", "GX", "Ultra Beast", "NihilegoGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=131,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=793,
    abilities=[
        Ability(
            title="Empty Light",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may leave both Active Pok\u00e9mon Confused and Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Symbiont-GX",
            game_text="Add the top 2 cards of your opponent's deck to their Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)