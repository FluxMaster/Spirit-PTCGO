"""STUB: effect not implemented — do not guess mechanics.
Chimecho (NP #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="330f9202-4cdc-566a-ac60-faf255fa6328",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Resonate",
            game_text="Your opponent switches each Defending Pok\u00e9mon with his or her Benched Pok\u00e9mon. If your opponent has only 1 Benched Pok\u00e9mon, you choose the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Healing Sound",
            game_text="Remove 3 damage counters from each of your Active Pok\u00e9mon. Each Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)