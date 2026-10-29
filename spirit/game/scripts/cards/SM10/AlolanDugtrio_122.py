"""STUB: effect not implemented — do not guess mechanics.
Alolan Dugtrio (SM10 #122): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="1105f2ee-f27b-5bb1-8de2-5d266fcfb7bc",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1", "AlolanDugtrio"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Hair Wall",
            game_text="Your Metal Pok\u00e9mon take 10 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)