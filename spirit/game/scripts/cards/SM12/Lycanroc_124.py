"""STUB: effect not implemented — do not guess mechanics.
Lycanroc (SM12 #124): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm8 import special_blow


card = PokemonCardDef(
    guid="268b4b34-6414-5f0e-8b24-8fede913c5f1",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1", "Lycanroc"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Boiling Blood",
            game_text="If your opponent has any Pok\u00e9mon-GX or Pok\u00e9mon-EX in play, this Pok\u00e9mon's attacks cost ColorlessColorlessColorless less.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Voltage Claw",
            game_text="If your opponent's Active Pok\u00e9mon has any Special Energy attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=special_blow,
        ),
    ],
)