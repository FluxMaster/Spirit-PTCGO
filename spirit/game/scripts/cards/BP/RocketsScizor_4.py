"""STUB: effect not implemented — do not guess mechanics.
Rocket's Scizor (BP #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9c226a5-6403-538a-8247-11e28eae0ad5",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScizor.Name",
    display_name="Rocket's Scizor",
    searchable_by=["Rocket's Scizor", "Basic", "RocketsScizor"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=212,
    abilities=[
        Attack(
            title="Focus",
            game_text="During your next turn, Rocket's Scizor's Agility attack's damage is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Rocket's Scizor.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)