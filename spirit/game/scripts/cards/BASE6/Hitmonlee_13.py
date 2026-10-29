"""STUB: effect not implemented — do not guess mechanics.
Hitmonlee (BASE6 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03607480-55e9-5592-a0e7-4f0979d2dbb6",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name",
    display_name="Hitmonlee",
    searchable_by=["Hitmonlee", "Basic", "Hitmonlee"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=106,
    abilities=[
        Attack(
            title="Stretch Kick",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon, and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
        ),
    ],
)