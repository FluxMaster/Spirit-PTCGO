"""STUB: effect not implemented — do not guess mechanics.
Murkrow (SM5 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9801ec82-9bf1-55ba-a8ae-29e7594fc9e2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=198,
    abilities=[
        Attack(
            title="Mean Look",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)