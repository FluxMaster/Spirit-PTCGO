"""STUB: effect not implemented — do not guess mechanics.
Garchomp (DP2 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2255434f-2280-5efc-b338-d2bbdb279f2f",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="DP2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Rainbow Scale",
            game_text="If an Active Pok\u00e9mon has Weakness to any of the types of Energy attached to Garchomp, Garchomp's attacks do 40 more damage to that Pok\u00e9mon (before applying Weakness and Resistance). Rainbow Scale Pok\u00e9-Body can't be used if Garchomp has any Special Energy cards attached to it.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Fang",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)