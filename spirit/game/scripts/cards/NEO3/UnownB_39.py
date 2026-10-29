"""STUB: effect not implemented — do not guess mechanics.
Unown [B] (NEO3 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a4387294-7cc1-5974-ae25-facd4e921ec0",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownB.Name",
    display_name="Unown [B]",
    searchable_by=["Unown [B]", "Basic", "UnownB"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Bear]",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon with Unown in its name to Unown [B]. This power can't be used if Unown [B] has 10 HP left. This power can be used even if Unown [B] is Asleep, Confused, or Paralyzed.",
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