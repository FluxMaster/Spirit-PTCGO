"""STUB: effect not implemented — do not guess mechanics.
Ninetales (BASE4 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="c70a5f78-53dd-593c-b295-24cf7cbf2207",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Lure",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard 1 Fire Energy card attached to Ninetales in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=80,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)