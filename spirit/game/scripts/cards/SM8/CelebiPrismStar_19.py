"""STUB: effect not implemented — do not guess mechanics.
Celebi {*} (SM8 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="85255362-5cac-58ce-ab08-53df0650013d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiPrismStar.Name",
    display_name="Celebi {*}",
    searchable_by=["Celebi {*}", "Basic", "Prism Star", "CelebiPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=19,
    set_code="SM8",
    rarity=Rarities.Prism,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Time Distortion",
            game_text="Devolve any number of your Benched Pok\u00e9mon as many times as you like. Put each Evolution card removed this way into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leech Seed",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=heal_attack(20),
        ),
    ],
)