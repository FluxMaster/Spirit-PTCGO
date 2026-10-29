"""STUB: effect not implemented — do not guess mechanics.
Chatot (SM10 #162): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54cf8247-7691-5ee7-97dc-1ee0d101db83",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=162,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=441,
    abilities=[
        Attack(
            title="Mimic",
            game_text="Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tone-Deaf",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)