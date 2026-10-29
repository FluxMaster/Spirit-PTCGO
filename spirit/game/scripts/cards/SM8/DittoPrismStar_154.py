"""STUB: effect not implemented — do not guess mechanics.
Ditto {*} (SM8 #154): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="600ddbd8-4185-502c-a662-cfdae26dc68f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoPrismStar.Name",
    display_name="Ditto {*}",
    searchable_by=["Ditto {*}", "Basic", "Prism Star", "DittoPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=154,
    set_code="SM8",
    rarity=Rarities.Prism,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Almighty Evolution",
            game_text="Once during your turn (before your attack), you may put any Stage 1 card from your hand onto this Pok\u00e9mon to evolve it. You can't use this Ability during your first turn or the turn this Pok\u00e9mon was put into play.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)