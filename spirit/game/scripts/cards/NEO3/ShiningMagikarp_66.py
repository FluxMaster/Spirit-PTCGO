"""STUB: effect not implemented — do not guess mechanics.
Shining Magikarp (NEO3 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce1a8c36-f05b-5ff3-a170-9449d8474419",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningMagikarp.Name",
    display_name="Shining Magikarp",
    searchable_by=["Shining Magikarp", "Basic", "ShiningMagikarp"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="NEO3",
    rarity=Rarities.Shining,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Gold Scale",
            game_text="Your opponent may draw 2 cards. Either way, you may draw 2 cards.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Bond",
            game_text="Search your deck for a card named Gyarados, Dark Gyarados, or Shining Gyarados. Show it to your opponent and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)