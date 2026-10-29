"""STUB: effect not implemented — do not guess mechanics.
Oricorio (SM2 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def axe_slash(ctx):
    """Discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon."""
    await ctx.deal_damage()
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="ee8df031-bc12-5795-a3d0-ff67484be0d4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Attack(
            title="Passionate Dance",
            game_text="Search your deck for up to 3 Basic Fire Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=axe_slash,
        ),
    ],
)