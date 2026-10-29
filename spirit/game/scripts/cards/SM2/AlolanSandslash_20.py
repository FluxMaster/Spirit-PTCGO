"""STUB: effect not implemented — do not guess mechanics.
Alolan Sandslash (SM2 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="3df81b5e-f607-5b46-8b6e-12b582208417",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name",
    display_name="Alolan Sandslash",
    searchable_by=["Alolan Sandslash", "Stage 1", "AlolanSandslash"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Slush Rush",
            game_text="Once during your turn (before your attack), you may draw a card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Smash Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=switch_self_attack(),
        ),
    ],
)