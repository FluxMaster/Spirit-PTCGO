"""STUB: effect not implemented — do not guess mechanics.
Alolan Ninetales-GX (HF #SV53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb75816d-3b97-50a8-9ac9-37fbf24b0d70",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetalesGX.Name",
    display_name="Alolan Ninetales-GX",
    searchable_by=["Alolan Ninetales-GX", "Stage 1", "GX", "AlolanNinetalesGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=122,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Ice Blade",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blizzard Edge",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ice Path-GX",
            game_text="Move all damage counters from this Pok\u00e9mon to your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)