# Program to play Liar's dice
from game_states.id_handler import new_game_id

def new_game(num_players, dice_per_player, num_lost_dice, spot_on, wild_ones):
    'Initializes a new game of Liar\'s dice'

    # Initialize variables
    game_id = new_game_id()
    num_players = int(num_players)
    dice_per_player = int(dice_per_player)
    num_lost_dice = num_lost_dice
    print(spot_on)
    spot_on = bool(spot_on)
    wild_ones = bool(wild_ones)

    # TODO: DECIDE ON REST OF LOGIC AND VARIABLES NEEDED TO FULY DEFINE STATE

    # TODO: STORE STATE INTO JSON FILE IN ./game_states/{game_id}.json

    return game_id



