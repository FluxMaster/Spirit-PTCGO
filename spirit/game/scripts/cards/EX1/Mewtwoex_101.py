"""STUB: effect not implemented — do not guess mechanics.
Mewtwo ex (EX1 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df9111d0-e6db-58f3-83c0-925ced43cc33",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "ex", "Mewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=101,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Attach up to 2 Energy cards from your discard pile to Mewtwo ex.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)