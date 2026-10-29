"""STUB: effect not implemented — do not guess mechanics.
Koga's Arbok (GYM2 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c47d79d6-99a6-56c9-b852-2ea555b9bb3d",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasArbok.Name",
    display_name="Koga's Arbok",
    searchable_by=["Koga's Arbok", "Stage 1", "KogasArbok"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasEkans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Poison Buildup",
            game_text="Koga's Arbok is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Power",
            game_text="If Koga's Arbok is Poisoned, this attack's base damage is 40 instead of 20 and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)