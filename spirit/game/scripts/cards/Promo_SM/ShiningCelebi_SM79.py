"""STUB: effect not implemented — do not guess mechanics.
Shining Celebi (Promo_SM #SM79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8e353f1b-7773-5e66-9e46-62c8f2c6c6df",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCelebi.Name",
    display_name="Shining Celebi",
    searchable_by=["Shining Celebi", "Basic", "ShiningCelebi"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Time Recall",
            game_text="Each of your evolved Pok\u00e9mon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)