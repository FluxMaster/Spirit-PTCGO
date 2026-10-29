"""STUB: effect not implemented — do not guess mechanics.
Morelull (SM5 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04e1e207-3d71-5c6d-9c28-32c9474e409a",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    display_name="Morelull",
    searchable_by=["Morelull", "Basic", "Morelull"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=755,
    abilities=[
        Attack(
            title="Flickering Spores",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)