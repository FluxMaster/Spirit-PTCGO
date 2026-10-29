"""STUB: effect not implemented — do not guess mechanics.
Dark Gengar (NEO4 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="00fef6d4-4729-5323-b7a7-32579b822862",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGengar.Name",
    display_name="Dark Gengar",
    searchable_by=["Dark Gengar", "Stage 2", "DarkGengar"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHaunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Deep Sleep",
            game_text="As long as any Dark Gengar are in play, a player flips 2 coins for each of his or her Pok\u00e9mon that is Asleep at the end of each turn. If either of them is tails, that Pok\u00e9mon is still Asleep. This power stops working if Dark Gengar is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pull In",
            game_text="If your opponent has any Benched Pok\u00e9mon, you may choose 1 of them and switch it with the Defending Pok\u00e9mon (before doing damage or other effects of this attack). Either way, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)