"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Raichu (GYM1 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="279f9d86-d3d4-529e-a724-ca2e2fc6bf56",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRaichu.Name",
    display_name="Lt. Surge's Raichu",
    searchable_by=["Lt. Surge's Raichu", "Stage 1", "LtSurgesRaichu"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesPikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy cards attached to Lt. Surge's Raichu in order to use this attack.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)