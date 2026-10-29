"""STUB: effect not implemented — do not guess mechanics.
Charizard-GX (SM3 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="6476f4c4-7334-5430-be25-d6726fd683d4",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGX.Name",
    display_name="Charizard-GX",
    searchable_by=["Charizard-GX", "Stage 2", "GX", "CharizardGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=20,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
        Attack(
            title="Crimson Storm",
            game_text="Discard 3 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=300,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=3, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Raging Out-GX",
            game_text="Discard the top 10 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)