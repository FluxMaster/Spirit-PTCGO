"""STUB: effect not implemented — do not guess mechanics.
Unown [Z] (NEO4 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6a685e34-cd42-5261-be19-c18db6bb6872",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownZ.Name",
    display_name="Unown [Z]",
    searchable_by=["Unown [Z]", "Basic", "UnownZ"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Zoom]",
            game_text="As long as Unown [Z] is Benched, you pay no Energy cost to retreat a Pok\u00e9mon with Unown in its name.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)