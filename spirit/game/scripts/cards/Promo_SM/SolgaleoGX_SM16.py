"""STUB: effect not implemented — do not guess mechanics.
Solgaleo-GX (Promo_SM #SM16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="003e9121-2022-556b-b76f-34187d642b50",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name",
    display_name="Solgaleo-GX",
    searchable_by=["Solgaleo-GX", "Stage 2", "GX", "SolgaleoGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=16,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=791,
    abilities=[
        Ability(
            title="Ultra Road",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sunsteel Strike",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sol Burst-GX",
            game_text="Search your deck for up to 5 Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)