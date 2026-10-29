"""STUB: effect not implemented — do not guess mechanics.
Smoochum (NEO3 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d18b3ed8-fd1d-5d61-83f4-bae33ec71d81",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Baby", "Smoochum"],
    subtypes=["Baby"],
    collector_number=54,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=238,
    abilities=[
        Attack(
            title="Psykiss",
            game_text="Flip a coin. If heads, choose a Special Energy card attached to 1 of your opponent's Pok\u00e9mon. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)