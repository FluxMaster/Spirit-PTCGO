"""STUB: effect not implemented — do not guess mechanics.
Trevenant (SM2 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="8d3b9c10-111c-5d63-9d28-38c585d1cdae",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 30 damage for each Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Horn Leech",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=heal_attack(30, target='self'),
        ),
    ],
)