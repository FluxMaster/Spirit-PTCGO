"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Gengar (GYM2 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0acba760-827e-55b1-aeb4-9693b222ed82",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGengar.Name",
    display_name="Sabrina's Gengar",
    searchable_by=["Sabrina's Gengar", "Stage 2", "SabrinasGengar"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasHaunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Dark Wave",
            game_text="All Pok\u00e9mon Powers stop working until the end of your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Bind",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)