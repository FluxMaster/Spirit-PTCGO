"""STUB: effect not implemented — do not guess mechanics.
Beldum (EX5 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cc645630-883f-50c2-8b0e-21042d609f2e",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Call",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a Metal Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Beldum is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Metal Charge",
            game_text="Put 1 damage counter on Beldum.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)