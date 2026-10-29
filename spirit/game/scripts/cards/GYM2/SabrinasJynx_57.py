"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Jynx (GYM2 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b03b6648-0100-5d7e-91f5-dab760c60ea2",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasJynx.Name",
    display_name="Sabrina's Jynx",
    searchable_by=["Sabrina's Jynx", "Basic", "SabrinasJynx"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Attack(
            title="Helping Hand",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Remove any number of damage counters from that Pok\u00e9mon, then draw that many cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hug",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)