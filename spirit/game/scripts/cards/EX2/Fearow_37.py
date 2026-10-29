"""STUB: effect not implemented — do not guess mechanics.
Fearow (EX2 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def super_slap_push(ctx):
    """Does 20 damage to each Defending Pok\u00e9mon (no printed damage)."""
    await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="d520e1f1-2567-5ae8-974b-0143c7ed1712",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow",
    searchable_by=["Fearow", "Stage 1", "Fearow"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=21,
    abilities=[
        Attack(
            title="Double Wing Attack",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=super_slap_push,
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon has any damage counters on it, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)