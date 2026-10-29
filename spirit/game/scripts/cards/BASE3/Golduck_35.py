"""STUB: effect not implemented — do not guess mechanics.
Golduck (BASE3 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4d56b40-31a9-5bd6-8ca7-2c180e2f0376",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Beam",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, choose 1 of them and discard it.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)