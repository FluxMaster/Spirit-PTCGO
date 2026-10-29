"""STUB: effect not implemented — do not guess mechanics.
Cleffa (SM10 #131): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="bd8722fd-d2d0-594b-85e8-af69dddf3e9e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=173,
    abilities=[
        Ability(
            title="Excitable Draw",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, shuffle your hand into your deck and then draw 6 cards. If you use this Ability, your turn ends.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)