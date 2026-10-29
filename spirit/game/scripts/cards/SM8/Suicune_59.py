"""STUB: effect not implemented — do not guess mechanics.
Suicune (SM8 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="6b73c1ac-823d-5757-9802-23c78efd05a7",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=245,
    abilities=[
        Ability(
            title="Frozen Flow",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Gain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=heal_attack(30),
        ),
    ],
)