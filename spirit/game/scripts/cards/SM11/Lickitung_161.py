"""STUB: effect not implemented — do not guess mechanics.
Lickitung (SM11 #161): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e2fc6203-881c-5480-9a16-8ecfb5f35c4d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Heavy Draw",
            game_text="Draw a card for each of your Pok\u00e9mon in play that has a Retreat Cost of exactly 4.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tongue Slap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)