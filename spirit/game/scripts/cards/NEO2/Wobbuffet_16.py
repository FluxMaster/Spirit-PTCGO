"""STUB: effect not implemented — do not guess mechanics.
Wobbuffet (NEO2 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="957f0198-fcb0-5c74-837b-6871295c37a9",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Attack(
            title="Counter",
            game_text="If an attack damages Wobbuffet during your opponent's next turn (even if Wobbuffet is Knocked Out), flip a coin. If heads, Wobbuffet attacks the Defending Pok\u00e9mon for an equal amount of damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)