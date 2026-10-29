"""STUB: effect not implemented — do not guess mechanics.
Dewgong (SM10 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="183f0780-c36a-5d81-949e-a786247261c4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Dual Blizzard",
            game_text="Discard 2 Energy from this Pok\u00e9mon. This attack does 60 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)