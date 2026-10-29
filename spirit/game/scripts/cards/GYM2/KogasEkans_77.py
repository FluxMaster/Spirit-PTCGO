"""STUB: effect not implemented — do not guess mechanics.
Koga's Ekans (GYM2 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="07f19b35-8498-5516-9e78-a69969cb2ee1",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasEkans.Name",
    display_name="Koga's Ekans",
    searchable_by=["Koga's Ekans", "Basic", "KogasEkans"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=23,
    abilities=[
        Attack(
            title="Fast-Acting Poison",
            game_text="Flip 2 coins. If both are heads, the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)