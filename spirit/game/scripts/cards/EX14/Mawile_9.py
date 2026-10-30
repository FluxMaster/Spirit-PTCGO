"""STUB: effect not implemented — do not guess mechanics.
Mawile (EX14 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88c90d2c-f691-5fe5-ac71-31f2352d2492",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=303,
    abilities=[
        Attack(
            title="Mining",
            game_text="Search your deck for a Trainer card, show it to your opponent, and put it into your hand. If that card is a Pok\u00e9mon Tool card, you may attach it to 1 of your Pok\u00e9mon instead. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bite Off",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)