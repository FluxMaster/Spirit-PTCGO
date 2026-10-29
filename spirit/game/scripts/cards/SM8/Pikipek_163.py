"""STUB: effect not implemented — do not guess mechanics.
Pikipek (SM8 #163): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93539eb7-75b3-5449-8811-25fc5140b839",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    display_name="Pikipek",
    searchable_by=["Pikipek", "Basic", "Pikipek"],
    subtypes=["Basic"],
    collector_number=163,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=731,
    abilities=[
        Attack(
            title="Peck Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)