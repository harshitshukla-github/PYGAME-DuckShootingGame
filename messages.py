def victory(score, time_duration):
  return ("Congratulations! You have the Game.", 
          f"Your score is {score}.", 
          f"You have killed {score} ducks.", 
          f"You're able to do this thing in {time_duration} seconds.")

def defeat(score, total_ducks):
  return (f"Your time is UP! You lost the game. Your score is {score}.",
          f"You have killed {score} ducks.",
          f"The total ducks you have to killed were {total_ducks}.")