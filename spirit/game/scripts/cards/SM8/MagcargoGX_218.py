"""STUB: effect not implemented — do not guess mechanics.
Magcargo-GX (SM8 #218): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4318046a-6063-50a4-9254-b9d37428e311",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagcargoGX.Name",
    display_name="Magcargo-GX",
    searchable_by=["Magcargo-GX", "Stage 1", "GX", "MagcargoGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=218,
    set_code="SM8",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Crushing Charge",
            game_text="Once during your turn (before your attack), you may discard the top card of your deck. If it's a basic Energy card, attach it to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lava Flow",
            game_text="Discard any amount of basic Energy from this Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Burning Magma-GX",
            game_text="Discard the top 5 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)