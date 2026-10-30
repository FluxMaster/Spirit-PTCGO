"""STUB: effect not implemented — do not guess mechanics.
Ludicolo δ (EX14 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import knock_off_random_hand


card = PokemonCardDef(
    guid="3b97a404-b171-58a4-b5be-b93f296e94c4",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo δ",
    searchable_by=["Ludicolo \u03b4", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Overzealous",
            game_text="If your opponent has any Pok\u00e9mon-ex in play, each of Ludicolo's attacks does 30 more damage to the Defending Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Knock Off",
            game_text="Choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=knock_off_random_hand(),
        ),
        Attack(
            title="Fire Punch",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)