"""STUB: effect not implemented — do not guess mechanics.
Gastly (BASE3 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc590c2d-8e7f-5bc6-a1fd-81a3869f4821",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Energy Conversion",
            game_text="Put up to 2 Energy cards from your discard pile into your hand. Gastly does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)