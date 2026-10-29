"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Gengar (GYM1 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7a411622-7b6a-596f-a792-9fe03f42c0fa",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGengar.Name",
    display_name="Sabrina's Gengar",
    searchable_by=["Sabrina's Gengar", "Stage 2", "SabrinasGengar"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasHaunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Pain Amplifier",
            game_text="Put a damage counter on each of your opponent's Pok\u00e9mon has already has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Call of the Night",
            game_text="Unless this attack Knocks Out the Defending Pok\u00e9mon, flip 2 coins. If both of them are heads, your opponent shuffles his or her Active Pok\u00e9mon and all cards attached to it into his or her deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)