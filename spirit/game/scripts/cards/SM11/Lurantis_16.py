"""STUB: effect not implemented — do not guess mechanics.
Lurantis (SM11 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


card = PokemonCardDef(
    guid="4a234618-3e62-545f-9ef9-210be4955c5b",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantis.Name",
    display_name="Lurantis",
    searchable_by=["Lurantis", "Stage 1", "Lurantis"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Attack(
            title="Petal Blizzard",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Sol Slice",
            game_text="If this Pok\u00e9mon has any Fire Energy attached to it, this attack does 50 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)