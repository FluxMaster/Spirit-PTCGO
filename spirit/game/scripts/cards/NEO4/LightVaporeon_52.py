"""STUB: effect not implemented — do not guess mechanics.
Light Vaporeon (NEO4 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e9cb56d-0b16-5c23-95f6-97ff9398833f",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightVaporeon.Name",
    display_name="Light Vaporeon",
    searchable_by=["Light Vaporeon", "Stage 1", "LightVaporeon"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=134,
    abilities=[
        Attack(
            title="Wash Away",
            game_text="If you have any Benched Pok\u00e9mon, flip a coin. If heads, remove all damage counters from 1 of your Benched Pok\u00e9mon and discard all Energy cards attached to it.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hypnoshower",
            game_text="The Defending Pok\u00e9mon is now Asleep. Remove 1 damage counter from each Benched Pok\u00e9mon (yours and your opponent's) with any damage counters on it.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)