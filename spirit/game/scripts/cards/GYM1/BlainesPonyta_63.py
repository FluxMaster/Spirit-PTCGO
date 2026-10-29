"""STUB: effect not implemented — do not guess mechanics.
Blaine's Ponyta (GYM1 #63): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6f0a7f7-7b36-5bb6-ab0c-7835531ef8af",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesPonyta.Name",
    display_name="Blaine's Ponyta",
    searchable_by=["Blaine's Ponyta", "Basic", "BlainesPonyta"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Blaine's Ponyta.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)