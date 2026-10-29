"""STUB: effect not implemented — do not guess mechanics.
Magikarp (SM4 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.data_utils import evolves_from


def _yoga_guard_pred(calc, carrier):
    return calc.is_attack and calc.target is carrier and not calc.to_active


async def ascension(ctx):
    """Search for a card that evolves from this Pokémon and evolve it onto this Pokémon; shuffle."""
    picks = await ctx.search_deck(
        lambda c: evolves_from(c.archetype_id, "Koffing"),
        count=1, minimum=0,
        prompt="Choose a card that evolves from Koffing.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="6bbdafd3-bfea-5ce5-af64-bf7ee67e4e58",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=prevent_damage_when(_yoga_guard_pred, attacks_only=False),
        ),
        Attack(
            title="Waterfall Evolution",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=ascension,
        ),
    ],
)