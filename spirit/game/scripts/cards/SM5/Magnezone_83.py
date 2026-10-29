"""STUB: effect not implemented — do not guess mechanics.
Magnezone (SM5 #83): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2db45f46-7f37-5c0f-9c67-83142fbe17d9",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=83,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetic Circuit",
            game_text="As often as you like during your turn (before your attack), you may attach a Metal Energy card from your hand to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Zap Cannon",
            game_text="This Pok\u00e9mon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)