"""STUB: effect not implemented — do not guess mechanics.
Scizor (SM8 #126): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="09cfa82f-17c4-5aaf-ab21-3d48f985769a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=126,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Special Blow",
            game_text="If your opponent's Active Pok\u00e9mon has any Special Energy attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)