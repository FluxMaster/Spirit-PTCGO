"""STUB: effect not implemented — do not guess mechanics.
Melmetal (SM10 #129): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8251380c-c6a8-513f-99e0-45f768a13a69",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1", "Melmetal"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Ability(
            title="Metal Eater",
            game_text="Once during your turn (before your attack), you may discard a Metal Pok\u00e9mon from your hand. If you do, heal 100 damage from this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)