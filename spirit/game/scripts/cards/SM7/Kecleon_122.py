"""STUB: effect not implemented — do not guess mechanics.
Kecleon (SM7 #122): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="01cfb2a3-f905-5c36-9f59-43d08d646dc9",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Kecleon"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Unit Color 2",
            game_text="As long as this Pok\u00e9mon has Unit Energy LightningPsychicMetal attached to it, it is a Lightning, Psychic, and Metal Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)