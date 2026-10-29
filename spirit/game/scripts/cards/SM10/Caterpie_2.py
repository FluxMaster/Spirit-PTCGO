"""STUB: effect not implemented — do not guess mechanics.
Caterpie (SM10 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4c4d98f5-8a0c-570d-bb56-ae453fae85f5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    display_name="Caterpie",
    searchable_by=["Caterpie", "Basic", "Caterpie"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=10,
    abilities=[
        Ability(
            title="Pupate",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)