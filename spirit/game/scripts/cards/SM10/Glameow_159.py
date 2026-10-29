"""STUB: effect not implemented — do not guess mechanics.
Glameow (SM10 #159): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96588d52-c4c9-5e2b-bcdb-8e5cee39cf4a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    display_name="Glameow",
    searchable_by=["Glameow", "Basic", "Glameow"],
    subtypes=["Basic"],
    collector_number=159,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=431,
    abilities=[
        Attack(
            title="Caturday",
            game_text="Draw a card. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boing Boing Tail",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)