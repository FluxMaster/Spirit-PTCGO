"""STUB: effect not implemented — do not guess mechanics.
Greninja (SM10 #117): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="60205043-1258-5fc2-b854-918b5b4eb47f",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    display_name="Greninja",
    searchable_by=["Greninja", "Stage 2", "Greninja"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Bring Down",
            game_text="The Pok\u00e9mon that has the least HP remaining, except for this Pok\u00e9mon, is Knocked Out. (If multiple Pok\u00e9mon are tied, choose one.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mist Slash",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)