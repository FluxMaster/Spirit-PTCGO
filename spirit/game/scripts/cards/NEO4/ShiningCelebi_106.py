"""STUB: effect not implemented — do not guess mechanics.
Shining Celebi (NEO4 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb104cfa-034b-512e-9601-0fc5fdd76d14",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCelebi.Name",
    display_name="Shining Celebi",
    searchable_by=["Shining Celebi", "Basic", "ShiningCelebi"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Healing Water",
            game_text="Remove a number of damage counters from 1 of your Benched Pok\u00e9mon equal to the number of Water Energy cards attached to Shining Celebi. If the Pok\u00e9mon has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Miracle Leaf",
            game_text="Flip a number of coins equal to the number of Energy attached to the Defending Pok\u00e9mon. If you get 1 or more heads, the Defending Pok\u00e9mon is now Asleep, Confused, or Poisoned (your choice).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)