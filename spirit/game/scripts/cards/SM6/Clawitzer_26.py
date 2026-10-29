"""STUB: effect not implemented — do not guess mechanics.
Clawitzer (SM6 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="2b434a01-9a57-53bb-aba1-1a783193f3b1",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1", "Clawitzer"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=692,
    abilities=[
        Attack(
            title="Standing By",
            game_text="During your next turn, this Pok\u00e9mon's Sharpshooting attack does 120 damage instead of 40.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharpshooting",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(40, pool='any', count=1),
        ),
    ],
)