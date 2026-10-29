"""STUB: effect not implemented — do not guess mechanics.
Dark Ampharos (NEO4 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="65009733-f597-5fb3-966c-b583ced886d6",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAmpharos.Name",
    display_name="Dark Ampharos",
    searchable_by=["Dark Ampharos", "Stage 2", "DarkAmpharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFlaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Conductivity",
            game_text="Whenever your opponent attaches an Energy card from his or her hand to a Pok\u00e9mon, this power does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power stops working if you have more than 1 Dark Ampharos in play or while Dark Ampharos is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shock Bolt",
            game_text="Discard all Lightning Energy cards attached to Dark Ampharos or this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)