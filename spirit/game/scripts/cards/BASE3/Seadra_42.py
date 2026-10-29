"""STUB: effect not implemented — do not guess mechanics.
Seadra (BASE3 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ebee078-e794-5d1a-a1bd-7f93d40a1a46",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra",
    searchable_by=["Seadra", "Stage 1", "Seadra"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 20 damage plus 10 more damage for each Water Energy attached to Seadra but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Seadra.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)