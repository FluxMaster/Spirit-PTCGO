"""STUB: effect not implemented — do not guess mechanics.
Banette-GX (SM7 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
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
    guid="eef613b6-2b1c-59f3-a3ee-84b9c0387986",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BanetteGX.Name",
    display_name="Banette-GX",
    searchable_by=["Banette-GX", "Stage 1", "GX", "BanetteGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=66,
    set_code="SM7",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Shady Move",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may move 1 damage counter from 1 Pok\u00e9mon to another Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Chant",
            game_text="This attack does 10 more damage for each Supporter card in your discard pile. You can't add more than 100 damage in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tomb Hunt-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=_hollow_hunt,
        ),
    ],
)