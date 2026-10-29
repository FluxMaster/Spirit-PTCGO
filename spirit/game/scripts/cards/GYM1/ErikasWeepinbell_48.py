"""STUB: effect not implemented — do not guess mechanics.
Erika's Weepinbell (GYM1 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca4bf4af-10d4-5484-8847-3ceb33cc3769",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    display_name="Erika's Weepinbell",
    searchable_by=["Erika's Weepinbell", "Stage 1", "ErikasWeepinbell"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Drool",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Flytrap",
            game_text="Before doing damage, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with his or her Active Pok\u00e9mon. This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)