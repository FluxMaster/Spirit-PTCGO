"""STUB: effect not implemented — do not guess mechanics.
Terrakion (Promo_SM #SM223): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61204674-4056-5d9a-af83-b2dfbd121a41",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terrakion.Name",
    display_name="Terrakion",
    searchable_by=["Terrakion", "Basic", "Terrakion"],
    subtypes=["Basic"],
    collector_number=223,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Cavern Counter",
            game_text="If all of your Benched Pok\u00e9mon have at least 1 damage counter on them, this attack does 150 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)