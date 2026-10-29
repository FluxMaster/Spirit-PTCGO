"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Eevee (GYM2 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7527019f-73f2-5d3f-987c-027cb08443d2",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesEevee.Name",
    display_name="Lt. Surge's Eevee",
    searchable_by=["Lt. Surge's Eevee", "Basic", "LtSurgesEevee"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=133,
    abilities=[
        Attack(
            title="Surprise",
            game_text="Look at a random card from your opponent's hand. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)