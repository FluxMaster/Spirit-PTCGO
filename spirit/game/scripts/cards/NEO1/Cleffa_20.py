"""STUB: effect not implemented — do not guess mechanics.
Cleffa (NEO1 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f0c86280-175d-52eb-81ae-9d332e91d5f7",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Baby", "Cleffa"],
    subtypes=["Baby"],
    collector_number=20,
    set_code="NEO1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=173,
    abilities=[
        Attack(
            title="Eeeeeeek",
            game_text="Shuffle your hand into your deck, then draw 7 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)