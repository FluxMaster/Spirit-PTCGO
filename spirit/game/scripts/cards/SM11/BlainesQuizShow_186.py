"""STUB: effect not implemented — do not guess mechanics.
Blaine's Quiz Show (SM11 #186): trainer effect stubbed.

Card text:
  - Put a Pokémon from your hand face down in front of you and tell your opponent the name of an attack it has. Your opponent guesses the name of that Pokémon, and then you reveal it. If your opponent guessed right, they draw 4 cards. If they guessed wrong, you draw 4 cards. Return the Pokémon to your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import blaines_quiz_show, blaines_quiz_show_condition

card = SupporterCardDef(guid='a8f982cb-3831-5788-97f0-2abb7064c632', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuizShow.Name', display_name="Blaine's Quiz Show", searchable_by=["Blaine's Quiz Show", 'Supporter'], subtypes=['Supporter'], collector_number=186, set_code='SM11', rarity=Rarities.Uncommon, effect=blaines_quiz_show, condition=blaines_quiz_show_condition)
