"""STUB: effect not implemented — do not guess mechanics.
Brock's Zubat (GYM1 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62e7a0e0-5d1d-59d8-909a-3a405193531f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksZubat.Name",
    display_name="Brock's Zubat",
    searchable_by=["Brock's Zubat", "Basic", "BrocksZubat"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=41,
    abilities=[
        Attack(
            title="Alert",
            game_text="Draw a card. Then, switch Brock's Zubat with 1 of your Benched Pok\u00e9mon. You can't use this attack if your Bench is empty.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)