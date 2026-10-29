"""STUB: effect not implemented — do not guess mechanics.
Stakataka (SM10 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def deck_distiller(ctx):
    heads = await ctx.flip_until_tails("Deck Distiller")
    if heads <= 0:
        return
    top_cards = ctx.deck_top(heads, ctx.opponent_id)
    if top_cards:
        await ctx.discard_cards(top_cards)


card = PokemonCardDef(
    guid="8ac69d94-5497-5873-8f74-ef8c1f8a831a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stakataka.Name",
    display_name="Stakataka",
    searchable_by=["Stakataka", "Basic", "Ultra Beast", "Stakataka"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=106,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=805,
    abilities=[
        Ability(
            title="Wall of Stone",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon's maximum HP is 200.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Top Down",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=deck_distiller,
        ),
    ],
)