"""STUB: effect not implemented — do not guess mechanics.
Spiritomb (SM5 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3eb8b390-d51a-528e-8e01-4667ef815966",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title="Lightless World",
            game_text="Put 2 Supporter cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Terrify",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)