"""STUB: effect not implemented — do not guess mechanics.
Omanyte (ECARD3 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def metal_reversal(ctx):
    """Optional: switch Defending with a Benched Pokémon, then deal damage."""
    bench = ctx.opponent_bench()
    if bench:
        pick = await ctx.choose_pokemon(
            bench, "You may choose a Benched Pokémon to switch into the Active Spot",
            optional=True,
        )
        if pick:
            await ctx.switch_active(ctx.opponent_id, pick)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="96a7c55e-b512-58d1-8a79-e64545a6b77a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Water of Evolution",
            game_text="Put an Omastar from your hand onto Omanyte. This counts as evolving Omanyte.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=metal_reversal,
        ),
    ],
)