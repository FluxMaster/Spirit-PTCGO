"""STUB: effect not implemented — do not guess mechanics.
Snover (SM5 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7d6a12dd-53ae-58b1-9bce-cd4df15b94ae",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=459,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)