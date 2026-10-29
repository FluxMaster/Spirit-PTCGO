"""STUB: effect not implemented — do not guess mechanics.
Celebi & Venusaur-GX (SM9 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ea10e50d-f1ec-54ae-a56d-a10766bbc462",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiVenusaurGX.Name",
    display_name="Celebi & Venusaur-GX",
    searchable_by=["Celebi & Venusaur-GX", "Basic", "TAG TEAM", "GX", "CelebiVenusaurGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=1,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Pollen Hazard",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
        Attack(
            title="Evergreen-GX",
            game_text="Heal all damage from this Pok\u00e9mon. If this Pok\u00e9mon has at least 1 extra Grass Energy attached to it (in addition to this attack's cost), shuffle all cards from your discard pile into your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)