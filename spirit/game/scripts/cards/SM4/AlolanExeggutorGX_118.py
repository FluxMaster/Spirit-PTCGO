"""STUB: effect not implemented — do not guess mechanics.
Alolan Exeggutor-GX (SM4 #118): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, condition_attack
from spirit.game.attributes import SpecialConditions


async def power_whip(ctx):
    """20 times this Pokémon's Energy, to 1 of the opponent's Pokémon."""
    amount = 20 * count_energy()(ctx)
    if amount <= 0:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a Pokémon to take damage",
    )
    if picks:
        await ctx.deal_damage(amount, target=picks[0])


card = PokemonCardDef(
    guid="42333db9-d131-5502-9468-7f3cd6fd4252",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorGX.Name",
    display_name="Alolan Exeggutor-GX",
    searchable_by=["Alolan Exeggutor-GX", "Stage 1", "GX", "AlolanExeggutorGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=118,
    set_code="SM4",
    rarity=Rarities.RareRainbow,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tropical Head",
            game_text="This attack does 20 damage times the amount of Energy attached to this Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=power_whip,
        ),
        Attack(
            title="Dragon Hammer",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Tower-Go-Round-GX",
            game_text="Move any number of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)