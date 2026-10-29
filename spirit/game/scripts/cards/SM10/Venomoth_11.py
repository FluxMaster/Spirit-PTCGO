"""STUB: effect not implemented — do not guess mechanics.
Venomoth (SM10 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6a7e22df-e26b-507d-b362-2bbd5dc8e375",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Assassin Flight",
            game_text="You can use this attack only if your opponent's Active Pok\u00e9mon is affected by a Special Condition. This attack does 90 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)