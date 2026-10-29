"""STUB: effect not implemented — do not guess mechanics.
Hydreigon (DM #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="0ce390b2-5ae0-531d-9a13-d927e11a289c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=635,
    abilities=[
        Ability(
            title="Weed Out",
            game_text="Once during your turn (before your attack), you may choose 3 of your Benched Pok\u00e9mon. Then, discard your other Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Destruction",
            game_text="You may discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)