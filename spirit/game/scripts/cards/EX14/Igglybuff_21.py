"""STUB: effect not implemented — do not guess mechanics.
Igglybuff (EX14 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="7fa97602-aa2d-5fdb-aef0-bfec8739d36b",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Basic", "Igglybuff"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=174,
    abilities=[
        Ability(
            title="Hover Lift",
            game_text="You pay Colorless less to retreat your Jigglypuff, Wigglytuff, Wigglytuff ex, and Igglybuff.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Jigglypuff from your hand onto Igglybuff (this counts as evolving Igglybuff) and remove all damage counters from Igglybuff.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)