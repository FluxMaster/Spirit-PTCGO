"""STUB: effect not implemented — do not guess mechanics.
Meganium ex (EX10 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="660886fa-1ebf-5f39-b642-c139200a7ad6",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganiumex.Name",
    display_name="Meganium ex",
    searchable_by=["Meganium ex", "Stage 2", "ex", "Meganiumex"],
    subtypes=["Stage 2", "ex"],
    collector_number=106,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Nurture and Heal",
            game_text="Once during your turn (before your attack), you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon. If you do, remove 1 damage counter from that Pok\u00e9mon. This power can't be used if Meganium ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Power Poison",
            game_text="Discard 1 Energy attached to Meganium ex. The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 3},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)