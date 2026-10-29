"""STUB: effect not implemented — do not guess mechanics.
Pichu (ECARD1 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4d46bfb-2054-5198-9982-eb849e4d796b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Baby", "Pichu"],
    subtypes=["Baby"],
    collector_number=22,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=172,
    abilities=[
        Attack(
            title="Energy Patch",
            game_text="Take a basic Energy card attached to 1 of your Pok\u00e9mon and attach it to another of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)