"""STUB: effect not implemented — do not guess mechanics.
Articuno ex (NP #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5e7ea981-0f05-5d00-b3d0-40caad4f77ae",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articunoex.Name",
    display_name="Articuno ex",
    searchable_by=["Articuno ex", "Basic", "EX", "Articunoex"],
    subtypes=["Basic", "EX"],
    collector_number=32,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Zapdos ex and Moltres ex in play, the Retreat Cost for Articuno ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ice Gift",
            game_text="You may move a Water Energy attached to Articuno ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Freezing Wing",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)