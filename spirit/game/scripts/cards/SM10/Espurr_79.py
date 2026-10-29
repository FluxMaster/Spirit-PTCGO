"""STUB: effect not implemented — do not guess mechanics.
Espurr (SM10 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d573c81-e7eb-53ef-aa27-b9eb56762665",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic", "Espurr"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=677,
    abilities=[
        Attack(
            title="Caturday",
            game_text="Draw a card. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ear Kinesis",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon for each damage counter on that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)