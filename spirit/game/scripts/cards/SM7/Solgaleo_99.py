"""STUB: effect not implemented — do not guess mechanics.
Solgaleo (SM7 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c024e725-d68d-57c0-8a81-1a92231da5ee",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name",
    display_name="Solgaleo",
    searchable_by=["Solgaleo", "Stage 2", "Solgaleo"],
    subtypes=["Stage 2"],
    collector_number=99,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=160,
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
            title="Full Metal Body",
            game_text="If this Pok\u00e9mon has any Metal Energy attached to it, it has no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rising Dash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)