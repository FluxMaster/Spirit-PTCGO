"""STUB: effect not implemented — do not guess mechanics.
Audino (SM11 #177): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="3318452a-657a-5640-9837-3b8642f7539a",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=177,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Ability(
            title="Hearing",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may draw a card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Drain Slap",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=heal_attack(30),
        ),
    ],
)