"""STUB: effect not implemented — do not guess mechanics.
Slowpoke (BASE3 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ed3486f-46bb-5f11-a1b4-d319b8e07550",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Spacing Out",
            game_text="Flip a coin. If heads, remove a damage counter from Slowpoke. This attack can't be used if Slowpoke has no damage counters on it.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scavenge",
            game_text="Discard 1 Psychic Energy card attached to Slowpoke in order to use this attack. Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)