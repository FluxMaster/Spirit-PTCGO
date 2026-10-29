"""STUB: effect not implemented — do not guess mechanics.
Cresselia (SM5 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b83047d5-eae9-597e-b58a-4886a011b896",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Attack(
            title="Lunar Payback",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch all damage counters on this Pok\u00e9mon with those on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)