"""STUB: effect not implemented — do not guess mechanics.
Koga's Koffing (GYM2 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7d26fbc-0e84-5bc9-b2ad-b9b7414cff1b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasKoffing.Name",
    display_name="Koga's Koffing",
    searchable_by=["Koga's Koffing", "Basic", "KogasKoffing"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Obscuring Gas",
            game_text="Flip a coin. If heads, shuffle Koga's Koffing and all cards attached to it into your deck (after doing damage).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)