"""STUB: effect not implemented — do not guess mechanics.
Groudon ex (NP #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="593a0993-c363-5349-a1eb-42f314a8c31a",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "EX", "Groudonex"],
    subtypes=["Basic", "EX"],
    collector_number=2,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Major Earthquake",
            game_text="Discard a Fighting Energy card attached to Groudon ex. Does 10 damage to your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 4},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)