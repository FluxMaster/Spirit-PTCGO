"""STUB: effect not implemented — do not guess mechanics.
Vaporeon-GX (Promo_SM #SM172): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm9 import hydro_pump


card = PokemonCardDef(
    guid="10b9217c-fcec-5f3c-8db6-c4ce6e7ac44c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonGX.Name",
    display_name="Vaporeon-GX",
    searchable_by=["Vaporeon-GX", "Stage 1", "GX", "VaporeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=172,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Hydrating Drops",
            game_text="Once during your turn (before your attack), you may heal 30 damage from your Active Water Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 30 more damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=hydro_pump,
        ),
        Attack(
            title="Cure Shower-GX",
            game_text="Heal all damage from all of your Water Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)