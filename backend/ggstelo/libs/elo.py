from ..models import Match


def calculate_elo(player_a, player_b, outcome):
    """
    Calculates the updated Elo ratings for two players after a match.

    Args:
        rating_a (int): Player A's current Elo rating.
        rating_b (int): Player B's current Elo rating.
        outcome (int): The outcome of the match. 1 if player A won, 0.5 if it was a draw, and 0 if player B won.
        k_factor (int): The K-factor determines how much the Elo ratings change after a match. Calculated based 
                        how many matches the player has as well as their current elo.

    Returns:
        A tuple containing the updated Elo ratings for player A and player B.
    """
    # Calculate K Factor for each player
    pa_match_count = Match.objects.filter(player1__exact=player_a).count(
    ) + Match.objects.filter(player2__exact=player_a).count()

    pb_match_count = Match.objects.filter(player1__exact=player_b).count(
    ) + Match.objects.filter(player2__exact=player_b).count()

    if (pa_match_count > 10 and player_a.highest_elo < 2400):
        player_a_k = 20
    elif (player_a.highest_elo >= 2400):
        player_a_k = 10
    else:
        player_a_k = 40

    if (pb_match_count > 10 & player_b.highest_elo < 2400):
        player_b_k = 20
    elif (player_b.highest_elo >= 2400):
        player_b_k = 10
    else:
        player_b_k = 40

    expected_a = 1 / (1 + 10**((player_b.elo - player_a.elo) / 400))
    expected_b = 1 / (1 + 10**((player_a.elo - player_b.elo) / 400))
    rating_a_new = player_a.elo + player_a_k * (outcome - expected_a)
    rating_b_new = player_b.elo + player_b_k * ((1 - outcome) - expected_b)
    return (int(round(rating_a_new)), int(round(rating_b_new)))
