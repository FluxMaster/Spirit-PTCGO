"""STUB: effect not implemented — do not guess mechanics.
Alolan Meowth (Promo_SM #SM51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d8d395d-4dcd-59ca-ae40-372f54faf01f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    display_name="Alolan Meowth",
    searchable_by=["Alolan Meowth", "Basic", "AlolanMeowth"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)