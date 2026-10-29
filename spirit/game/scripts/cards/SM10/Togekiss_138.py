"""STUB: effect not implemented — do not guess mechanics.
Togekiss (SM10 #138): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="1bb6993e-eabf-51e3-8c02-72c981c5005c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=138,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Fairy Feast",
            game_text="Once during your turn (before your attack), you may heal 30 damage from each of your Fairy Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)