"""STUB: effect not implemented — do not guess mechanics.
Volbeat (SM7 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ce95612-967f-54d3-b171-6f9b3e036004",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Pheromone Catch",
            game_text="If your Illumise used Pheromone Signals during your last turn, this attack does 100 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)