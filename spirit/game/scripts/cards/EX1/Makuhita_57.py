"""STUB: effect not implemented — do not guess mechanics.
Makuhita (EX1 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a168eb8-b829-504d-9bcb-69e0ed8ef982",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    display_name="Makuhita",
    searchable_by=["Makuhita", "Basic", "Makuhita"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=296,
    abilities=[
        Attack(
            title="Fling",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)