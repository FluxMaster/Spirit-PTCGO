"""STUB: effect not implemented — do not guess mechanics.
Magby (EX12 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ab4f4e06-0fe1-57e9-984b-6d721be19614",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic", "Magby"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Magmar from your hand onto Magby (this counts as evolving Magby) and remove all damage counters from Magby.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ignite",
            game_text="If Full Flame is in play, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)