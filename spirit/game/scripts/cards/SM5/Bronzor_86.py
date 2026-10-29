"""STUB: effect not implemented — do not guess mechanics.
Bronzor (SM5 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="485eaaab-eb73-5753-b9d6-ac6b153d1d67",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=436,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)