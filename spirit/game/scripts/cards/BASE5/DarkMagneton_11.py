"""STUB: effect not implemented — do not guess mechanics.
Dark Magneton (BASE5 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6289380b-836e-5cfb-a512-5c22cb16a091",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagneton.Name",
    display_name="Dark Magneton",
    searchable_by=["Dark Magneton", "Stage 1", "DarkMagneton"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Sonicboom",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magnetic Lines",
            game_text="If the Defending Pok\u00e9mon has any basic Energy cards attached to it, choose 1 of them. If your opponent has any Benched Pok\u00e9mon, choose 1 of them and attach that Energy card to it.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)