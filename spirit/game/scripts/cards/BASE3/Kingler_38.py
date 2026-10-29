"""STUB: effect not implemented — do not guess mechanics.
Kingler (BASE3 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ac6770e-49b1-5c00-983a-14ceca6e0937",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler",
    searchable_by=["Kingler", "Stage 1", "Kingler"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Kingler.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)