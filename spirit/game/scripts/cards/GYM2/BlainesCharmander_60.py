"""STUB: effect not implemented — do not guess mechanics.
Blaine's Charmander (GYM2 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53994bf9-c393-5009-9e93-76724811e7df",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharmander.Name",
    display_name="Blaine's Charmander",
    searchable_by=["Blaine's Charmander", "Basic", "BlainesCharmander"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Fire Tail Slap",
            game_text="Use this attack only if there are any Fire Energy cards attached to Blaine's Charmander. Flip a coin. If tails, discard 1 of those cards.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)