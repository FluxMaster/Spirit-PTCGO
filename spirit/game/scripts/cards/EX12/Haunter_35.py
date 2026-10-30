"""STUB: effect not implemented — do not guess mechanics.
Haunter (EX12 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="498fb4e8-1fa2-5e60-a009-8e4a5eebdda2",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1", "Haunter"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Time Spiral",
            game_text="If your opponent has any Evolved Pok\u00e9mon in play, choose 1 of them and flip a coin. If heads, remove the highest Stage Evolution card on that Pok\u00e9mon and have your opponent shuffle it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Haunt",
            game_text="Put 2 damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)