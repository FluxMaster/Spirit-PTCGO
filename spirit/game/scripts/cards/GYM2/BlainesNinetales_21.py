"""STUB: effect not implemented — do not guess mechanics.
Blaine's Ninetales (GYM2 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4021253d-49c8-5b14-ba69-1e66afff701c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesNinetales.Name",
    display_name="Blaine's Ninetales",
    searchable_by=["Blaine's Ninetales", "Stage 1", "BlainesNinetales"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesVulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Healing Fire",
            game_text="Whenever you attach a Fire Energy card from your hand to Blaine's Ninetales, remove 1 damage counter from it, if it has any. This power stops working when Blaine's Ninetales is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Burn Up",
            game_text="Flip a coin. If tails, discard all Fire Energy cards attached to Blaine's Ninetales.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)