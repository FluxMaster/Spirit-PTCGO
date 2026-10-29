"""STUB: effect not implemented — do not guess mechanics.
Celesteela (HF #SV32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff462083-b3f3-5670-9c76-9dfd07da83cb",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celesteela.Name",
    display_name="Celesteela",
    searchable_by=["Celesteela", "Basic", "Ultra Beast", "Celesteela"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=101,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=797,
    abilities=[
        Attack(
            title="Moon Raker",
            game_text="If the total of both players' remaining Prize cards is exactly 6, this attack can be used for Metal.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)