"""STUB: effect not implemented — do not guess mechanics.
Granbull (SM8 #138): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5ebb1a4-6756-57ca-982b-b7ff713a87f7",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1", "Granbull"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Attack(
            title="All Out",
            game_text="If you have no cards in your hand, this attack does 130 more damage.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giant Fangs",
            cost={PokemonTypes.FAIRY: 3},
            damage=110,
        ),
    ],
)