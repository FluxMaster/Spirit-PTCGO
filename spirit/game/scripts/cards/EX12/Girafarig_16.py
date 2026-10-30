"""STUB: effect not implemented — do not guess mechanics.
Girafarig (EX12 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c8737ac4-fb67-51d8-a1fa-e0e8cecf2a66",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Ability(
            title="Rear Sensor",
            game_text="Each player's Active Basic Pok\u00e9mon (excluding Pok\u00e9mon-ex) can't use any Pok\u00e9-Powers.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Foresight",
            game_text="Look at the top 5 cards on either player's deck and put them back on top of that player's deck in any order you like.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Disorder",
            game_text="If the Defending Pok\u00e9mon has any Special Energy cards attached to it, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)