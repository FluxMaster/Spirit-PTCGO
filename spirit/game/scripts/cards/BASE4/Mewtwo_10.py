"""STUB: effect not implemented — do not guess mechanics.
Mewtwo (BASE4 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per


card = PokemonCardDef(
    guid="0d8c0b3f-142a-5ab4-8b16-031846111949",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psychic",
            game_text="Does 10 damage plus 10 more damage for each Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=damage_per(count_energy('defender', cards=True), 10, base=10),
        ),
        Attack(
            title="Barrier",
            game_text="Discard 1 Psychic Energy card attached to Mewtwo in order to use this attack. During your opponent's next turn, prevent all effects of attacks, including damage, done to Mewtwo.",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)