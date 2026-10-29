"""STUB: effect not implemented — do not guess mechanics.
Latias {*} (SM7 #107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed5d024d-0e2c-5d1c-bde9-540046b533a4",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiasPrismStar.Name",
    display_name="Latias {*}",
    searchable_by=["Latias {*}", "Basic", "Prism Star", "LatiasPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=107,
    set_code="SM7",
    rarity=Rarities.Prism,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=380,
    abilities=[
        Attack(
            title="Dreamy Mist",
            game_text="Attach a basic Energy card from your discard pile to each of your Basic Benched Dragon Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)