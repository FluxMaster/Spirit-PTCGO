"""STUB: effect not implemented — do not guess mechanics.
Diancie {*} (SM6 #74): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def sugary_sprinkles(ctx):
    """Heal 30 damage from each of your Benched Pokemon."""
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="6eb6ea32-5340-53d6-b32a-53a8ce66fd29",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DianciePrismStar.Name",
    display_name="Diancie {*}",
    searchable_by=["Diancie {*}", "Basic", "Prism Star", "DianciePrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=74,
    set_code="SM6",
    rarity=Rarities.Prism,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=719,
    abilities=[
        Ability(
            title="Princess's Cheers",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Fighting Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Diamond Rain",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
            # STUB: attack effect not implemented
            effect=sugary_sprinkles,
        ),
    ],
)