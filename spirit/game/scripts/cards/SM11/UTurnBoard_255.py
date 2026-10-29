"""STUB: effect not implemented — do not guess mechanics.
U-Turn Board (SM11 #255): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Retreat Cost of the Pokémon this card is attached to is Colorless less.
  - If this card is discarded from play, put it into your hand instead of the discard pile.
  - You may play as many Item cards as you like during your turn (before your attack).
"""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import uturn_board_passive

card = PokemonToolCardDef(guid='8fdf4d41-7ae5-509e-80f3-d5ff1c04528c', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.UTurnBoard.Name', display_name='U-Turn Board', searchable_by=['U-Turn Board', 'Pokémon Tool'], subtypes=['Pokémon Tool'], collector_number=255, set_code='SM11', rarity=Rarities.RareSecret, passive=uturn_board_passive, return_to_hand_when_discarded_from_play=True)
