"""STUB: effect not implemented — do not guess mechanics.
Happiny (POP8 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="929cd881-27a3-5acf-aa25-8766655fc9f0",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Happiny.Name",
    display_name="Happiny",
    searchable_by=["Happiny", "Basic", "Happiny"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="POP8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=440,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Chansey from your hand onto Happiny (this counts as evolving Happiny) and remove all damage counters from Happiny.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lively",
            game_text="Remove 2 damage counters from 1 of your Pok\u00e9mon.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)