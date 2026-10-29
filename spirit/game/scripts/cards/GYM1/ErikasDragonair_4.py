"""STUB: effect not implemented — do not guess mechanics.
Erika's Dragonair (GYM1 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc66e67c-16b9-59d4-b1b5-88871fa43573",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasDragonair.Name",
    display_name="Erika's Dragonair",
    searchable_by=["Erika's Dragonair", "Stage 1", "ErikasDragonair"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasDratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. If tails, this attack does 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Take Away",
            game_text="Shuffle Erika's Dragonair and all cards attached to it into your deck. Then, your opponent shuffles his or her Active Pok\u00e9mon and all cards attached to it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 4},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)