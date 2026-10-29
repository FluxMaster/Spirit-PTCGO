"""STUB: effect not implemented — do not guess mechanics.
Blaine's Vulpix (GYM1 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="65a0b244-2116-5ce9-8f8d-a2b80449f2bb",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesVulpix.Name",
    display_name="Blaine's Vulpix",
    searchable_by=["Blaine's Vulpix", "Basic", "BlainesVulpix"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Ability(
            title="Natural Healing",
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from Blaine's Vulpix. This power can't be used if Blaine's Vulpix is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tail Fan",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)