"""STUB: effect not implemented — do not guess mechanics.
Dark Ivysaur (BP #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="996b26a6-1acf-55fd-bee6-df88830c31a8",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkIvysaur.Name",
    display_name="Dark Ivysaur",
    searchable_by=["Dark Ivysaur", "Stage 1", "DarkIvysaur"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=2,
    abilities=[
        Ability(
            title="Vine Pull",
            game_text="Once during your turn when Dark Ivysaur retreats, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fury Strikes",
            game_text="Your opponent puts 3 markers onto his or her Pok\u00e9mon (divided as he or she chooses). (More than 1 marker can be put on the same Pok\u00e9mon.) Then, this attack does 10 damage to each Pok\u00e9mon for each marker on it. Don't apply Weakness and Resistance. Remove the markers at the end of the turn.",
            cost={PokemonTypes.GRASS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)