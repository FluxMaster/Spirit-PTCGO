"""STUB: effect not implemented — do not guess mechanics.
Cyndaquil (ECARD1 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd82867e-82a4-5f1c-9648-339a5288d996",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    display_name="Cyndaquil",
    searchable_by=["Cyndaquil", "Basic", "Cyndaquil"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Ember",
            game_text="Discard a Fire Energy card attached to Cyndaquil.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)