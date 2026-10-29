"""STUB: effect not implemented — do not guess mechanics.
Dark Dragonite (BASE5 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ef516fea-f80a-5a17-ba91-d112c8b03549",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonite.Name",
    display_name="Dark Dragonite",
    searchable_by=["Dark Dragonite", "Stage 2", "DarkDragonite"],
    subtypes=["Stage 2"],
    collector_number=22,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Summon Minions",
            game_text="When you play Dark Dragonite from your hand, search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giant Tail",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)