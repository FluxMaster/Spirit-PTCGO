"""STUB: effect not implemented — do not guess mechanics.
Alolan Ninetales-GX (SM2 #150): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, self_energy_discard_attack


card = PokemonCardDef(
    guid="628d9258-ab84-5806-bbf5-24c983bd9b0a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetalesGX.Name",
    display_name="Alolan Ninetales-GX",
    searchable_by=["Alolan Ninetales-GX", "Stage 1", "GX", "AlolanNinetalesGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=150,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
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
            effect=snipe_attack(50, pool='any', count=1),
        ),
        Attack(
            title="Blizzard Edge",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=2),
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