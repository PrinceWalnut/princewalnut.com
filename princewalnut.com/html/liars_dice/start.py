from flask import Flask, request, redirect
from liars_dice import new_game

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def set_params():
    'Set parameters for a game of liar\'s dice.'
    req = request.form

    num_players = req['num_players']
    dice_per_player = req['dice_per_player']
    num_lost_dice = req['num_lost_dice']
    spot_on = False
    if( req.get('spot_on') == "1" ):
        spot_on = True
    wild_ones = False
    if( req.get('wild_ones') == "1" ):
        wild_ones = True

    game_id = new_game(num_players, dice_per_player, num_lost_dice, spot_on, wild_ones)
    
    return redirect(f"https://www.princewalnut.com/liars_dice/play.html?game_id={game_id}")

@app.route('/take_turn', methods=['POST'])
def take_turn(game_id, face_value, bid):
    'Take a turn in liar\'s dice'

    finished = False
    # game logic
    finished = True
    
    return finished

app.run()
