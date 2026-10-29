"""STUB: effect not implemented — do not guess mechanics.
Komala (Promo_SM #SM41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="50ea346f-fd23-5e30-ae8c-297ca0b75c17",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name",
    display_name="Komala",
    searchable_by=["Komala", "Basic", "Komala"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="Comatose",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever you attach an Energy from your hand to it, it is now Asleep.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hypno Roll",
            game_text="This attack can be used if this Pok\u00e9mon is Asleep. If it is not Asleep, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)