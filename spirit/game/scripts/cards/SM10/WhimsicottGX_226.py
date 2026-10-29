"""STUB: effect not implemented — do not guess mechanics.
Whimsicott-GX (SM10 #226): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5d7dc60f-489c-5603-9456-867818d29251",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottGX.Name",
    display_name="Whimsicott-GX",
    searchable_by=["Whimsicott-GX", "Stage 1", "GX", "WhimsicottGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=226,
    set_code="SM10",
    rarity=Rarities.RareRainbow,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Ability(
            title="Fluffy Cotton",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Energy Blow",
            game_text="This attack does 30 more damage times the amount of Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Toy Box-GX",
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)