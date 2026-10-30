"""STUB: effect not implemented — do not guess mechanics.
Wynaut (EX12 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="1462a754-f6dd-5f9c-ae9b-464db453e275",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wynaut.Name",
    display_name="Wynaut",
    searchable_by=["Wynaut", "Basic", "Wynaut"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=360,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Wobbuffet from your hand onto Wynaut (this counts as evolving Wynaut) and remove all damage counters from Wynaut.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Confusion Wave",
            game_text="Both Wynaut and the Defending Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)