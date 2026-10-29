"""STUB: effect not implemented — do not guess mechanics.
Passimian (SM5 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="0e8b2e70-f5fe-5c93-9a9e-2afc21c8fca7",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Passimian"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Ability(
            title="Power Huddle",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Passimian's attacks do 30 more damage to your opponent's Active Evolution Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=feint,
        ),
    ],
)