"""STUB: effect not implemented — do not guess mechanics.
Toxicroak (SM6 #64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="18522fa6-a1e0-5222-b6c9-ad4ad7d421dd",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1", "Toxicroak"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Exact Revenge",
            game_text="If any of your Psychic Pok\u00e9mon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)