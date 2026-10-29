"""STUB: effect not implemented — do not guess mechanics.
Venonat (NEO4 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="84c78a9d-6b9c-5f96-9f88-2e97bf67de1a",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    display_name="Venonat",
    searchable_by=["Venonat", "Basic", "Venonat"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Poisonpowder",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)