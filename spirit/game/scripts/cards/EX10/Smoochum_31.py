"""STUB: effect not implemented — do not guess mechanics.
Smoochum (EX10 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="46ca6b14-216a-5526-a593-9325b9233539",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=238,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Jynx from your hand onto Smoochum (this counts as evolving Smoochum) and remove all damage counters from Smoochum.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blown Kiss",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)