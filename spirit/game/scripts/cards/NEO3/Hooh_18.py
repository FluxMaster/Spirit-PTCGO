"""STUB: effect not implemented — do not guess mechanics.
Ho-oh (NEO3 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2deff919-9ea6-5755-b211-f13c53158418",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Rainbow Burn",
            game_text="This attack does 30 damage plus 10 more damage for each type of Basic Energy card, if any, attached to Ho-Oh.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)