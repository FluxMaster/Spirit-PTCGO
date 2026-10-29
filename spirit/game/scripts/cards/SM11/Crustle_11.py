"""STUB: effect not implemented — do not guess mechanics.
Crustle (SM11 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="47c291a1-ec38-56d4-9140-a83bfa52c0c3",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1", "Crustle"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Ability(
            title="Shell Armor",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 40 more damage. If 2 of them are heads, this attack does 80 more damage. If all of them are heads, this attack does 150 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)