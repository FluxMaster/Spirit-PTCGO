"""STUB: effect not implemented — do not guess mechanics.
Dark Vileplume (BASE5 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b00d2943-c9f6-5984-9346-2103001187e5",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkVileplume.Name",
    display_name="Dark Vileplume",
    searchable_by=["Dark Vileplume", "Stage 2", "DarkVileplume"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Hay Fever",
            game_text="No Trainer cards can be played. This power stops working while Dark Vileplume is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Petal Whirlwind",
            game_text="Flip a coins. This attack does 30 damage times the number of heads. If you get 2 or more heads, Dark Vileplume is now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)