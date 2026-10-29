"""STUB: effect not implemented — do not guess mechanics.
Honchkrow (SM5 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df5e8ab0-f74a-5278-b211-4fe6be951ec3",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Rip and Run",
            game_text="Discard a random card from your opponent's hand. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)