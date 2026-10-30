"""STUB: effect not implemented — do not guess mechanics.
Buneary (POP6 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ddcf816-f45d-54a6-b35b-f06b0d028017",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    display_name="Buneary",
    searchable_by=["Buneary", "Basic", "Buneary"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="POP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=427,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Jump Kick",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)