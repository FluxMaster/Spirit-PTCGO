"""STUB: effect not implemented — do not guess mechanics.
Celebi (NEO3 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7fa13428-a5f2-5cbd-8083-80a0f35d7b01",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Psychic Leaf",
            game_text="Flip a coin for each Energy attached to the Defending Pok\u00e9mon. This attack does 10 damage plus 10 more damage for each heads. Remove a number of damage counters from Celebi equal to the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance). If Celebi has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)