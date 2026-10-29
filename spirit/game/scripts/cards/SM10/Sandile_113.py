"""STUB: effect not implemented — do not guess mechanics.
Sandile (SM10 #113): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="babf7cc5-90d1-525f-a2a0-a800549319e9",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic", "Sandile"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=551,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon's attacks do 20 less damage (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)