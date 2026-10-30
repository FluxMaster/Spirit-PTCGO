"""STUB: effect not implemented — do not guess mechanics.
Nuzleaf (EX14 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5fd2238-a581-576a-8528-47922f88db7a",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    display_name="Nuzleaf",
    searchable_by=["Nuzleaf", "Stage 1", "Nuzleaf"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Self Charge",
            game_text="Attach a Darkness Energy card from your hand to Nuzleaf.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)