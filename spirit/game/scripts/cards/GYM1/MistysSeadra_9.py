"""STUB: effect not implemented — do not guess mechanics.
Misty's Seadra (GYM1 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9478334-4a46-5e11-a56f-abf053f54de2",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysSeadra.Name",
    display_name="Misty's Seadra",
    searchable_by=["Misty's Seadra", "Stage 1", "MistysSeadra"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysHorsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Tail Snap",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Knockout Needle",
            game_text="Flip 2 coins. If both of them are heads, this attack does 30 damage plus 60 more damage. If 1 or both of them are tails, this attack does 30 damage.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)