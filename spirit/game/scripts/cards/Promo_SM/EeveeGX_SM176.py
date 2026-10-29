"""STUB: effect not implemented — do not guess mechanics.
Eevee-GX (Promo_SM #SM176): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def _hollow_hunt(ctx):
    """Put 3 cards from your discard pile into your hand."""
    cards = list(ctx.discard_pile())
    if not cards:
        return
    n = min(3, len(cards))
    picks = await ctx.choose_cards(cards, n, minimum=n,
                                   prompt="Choose 3 cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="54e8b3b1-aa69-56f1-9274-f10c8b92bc4c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeGX.Name",
    display_name="Eevee-GX",
    searchable_by=["Eevee-GX", "Basic", "GX", "EeveeGX"],
    subtypes=["Basic", "GX"],
    collector_number=176,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Ascension DNA",
            game_text="Once during your turn (before your attack), if you have a Pok\u00e9mon in your hand that evolves from Eevee, you may put that card onto this Pok\u00e9mon to evolve it. Before evolving, heal all damage from this Pok\u00e9mon. You can't use this Ability during your first turn or on the turn this Pok\u00e9mon was put into play.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boost Dash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="Joy Maker-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=_hollow_hunt,
        ),
    ],
)