"""STUB: effect not implemented — do not guess mechanics.
Happiny (SM10 #161): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cb5427ab-f488-5c6e-9f81-8950e7ed6615",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Happiny.Name",
    display_name="Happiny",
    searchable_by=["Happiny", "Basic", "Happiny"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=440,
    abilities=[
        Ability(
            title="Playhouse Heal",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, heal 60 damage from 1 of your Pok\u00e9mon. If you use this Ability, your turn ends.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)