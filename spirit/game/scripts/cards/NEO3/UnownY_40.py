"""STUB: effect not implemented — do not guess mechanics.
Unown [Y] (NEO3 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="075404a5-af98-503a-a189-7caa41512370",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownY.Name",
    display_name="Unown [Y]",
    searchable_by=["Unown [Y]", "Basic", "UnownY"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Yield]",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon with Unown in its name. Shuffle your deck afterward. This power can be used even if Unown [Y] is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)