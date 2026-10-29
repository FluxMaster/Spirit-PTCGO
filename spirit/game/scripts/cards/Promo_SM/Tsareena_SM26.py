"""STUB: effect not implemented — do not guess mechanics.
Tsareena (Promo_SM #SM26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="67d41376-f9b5-5cbc-ad0a-731fe2904684",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name",
    display_name="Tsareena",
    searchable_by=["Tsareena", "Stage 2", "Tsareena"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=763,
    abilities=[
        Ability(
            title="Queenly Majesty",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have your opponent reveal their hand. Then, discard a card from it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Trop Kick",
            game_text="Heal 20 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)