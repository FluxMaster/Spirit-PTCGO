"""STUB: effect not implemented — do not guess mechanics.
Gengar (EX12 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="30fc2101-e2e0-5b0e-8ec1-83dff32fe87e",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Shadow Curse",
            game_text="If Gengar would be Knocked Out by damage from an opponent's attack, you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cursed Reaction",
            game_text="Put 2 damage counters on your opponent's Pok\u00e9mon in any way you like. If Gengar has any React Energy cards attached to it, put 4 damage counters instead.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)