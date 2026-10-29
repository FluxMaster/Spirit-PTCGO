"""STUB: effect not implemented — do not guess mechanics.
Koga's Zubat (GYM2 #83): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4f37489b-c384-5b60-936e-b8cda63de5ba",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasZubat.Name",
    display_name="Koga's Zubat",
    searchable_by=["Koga's Zubat", "Basic", "KogasZubat"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=41,
    abilities=[
        Attack(
            title="Group Attack",
            game_text="Does 10 damage times the number of Koga's Zubats you have in play. Before doing damage, you may search your deck for any number of Basic Pok\u00e9mon named Koga's Zubat and put them onto your Bench. (You can't get more cards with this attack than you have room on your Bench.) If you do, shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)