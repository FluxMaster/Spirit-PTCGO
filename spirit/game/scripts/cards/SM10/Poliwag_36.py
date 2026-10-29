"""STUB: effect not implemented — do not guess mechanics.
Poliwag (SM10 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3c440d3e-54b2-5b0a-8ecd-64e848013588",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    display_name="Poliwag",
    searchable_by=["Poliwag", "Basic", "Poliwag"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=60,
    abilities=[
        Ability(
            title="Round \u2018n' Round",
            game_text="You can use this Ability only if you go second. Once during your first turn (before your attack), you may leave your opponent's Active Pok\u00e9mon Confused.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Watering",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)