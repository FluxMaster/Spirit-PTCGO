"""STUB: effect not implemented — do not guess mechanics.
Machamp-GX (SM3 #135): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_evolution_pokemon


card = PokemonCardDef(
    guid="001b6bde-09a2-50de-a48d-d9179959e3eb",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampGX.Name",
    display_name="Machamp-GX",
    searchable_by=["Machamp-GX", "Stage 2", "GX", "MachampGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=135,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=68,
    abilities=[
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(active_is(is_evolution_pokemon), 60),
        ),
        Attack(
            title="Bedrock Breaker",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Muscle Punch-GX",
            game_text="This attack's damage isn't affected by Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)