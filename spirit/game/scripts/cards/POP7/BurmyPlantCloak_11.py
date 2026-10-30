"""STUB: effect not implemented — do not guess mechanics.
Burmy Plant Cloak (POP7 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c34ebe46-8fce-5567-8fdc-dcf9928a2d08",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name",
    display_name="Burmy Plant Cloak",
    searchable_by=["Burmy Plant Cloak", "Basic", "BurmyPlantCloak"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Ability(
            title="Wear Cloak",
            game_text="Once during your turn (before your attack), if Burmy Plant Cloak is your Active Pok\u00e9mon, you may search your discard pile for a basic Grass Energy card and attach it to Burmy Plant Cloak.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Plant Cloak Tackle",
            game_text="If Burmy Plant Cloak has any Grass Energy attached to it, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)