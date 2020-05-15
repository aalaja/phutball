# Tensorflow solely for the Progress Bar (totally worth it)
from tensorflow.keras.utils import Progbar

from .testing_utilities import create_state
from .move_selection import get_next_move_training

class ProgressBar:
  '''Wrapper for tf.keras.progbar that accounts for unknown length of game

  For simplicity, the interface is slightly changed and not all features are
  supported.

  Methods
  -------

  step: increment the bar by one step. Will extend the target length if
        the bar is more than 90% of the way done.

  terminate: step the bar AND cause it to end

  Attributes
  ----------

  move_num: number of moves made so far

  '''

  def __init__(self, estimated_length, verbose = True):
    self._bar     = Progbar(estimated_length)
    self._move_num = 0
    self.verbose = verbose

  @property
  def move_num(self):
    return self._move_num

  def step(self):
    self._move_num += 1

    curr_target = self._bar.target
    if self._move_num >= curr_target:
      self._bar.target += curr_target // 10 + 1
    
    if self.verbose:
      self._bar.update(self._move_num)

  def terminate(self):
    self._move_num += 1
    self._bar.target = self._move_num

    if self.verbose:
      self._bar.update(self._move_num)

def training_loop(model, optimizer, num_games, device, off_policy = lambda _ : None):
  
  initial_state = create_state('H10').to(device)
  for i in range(num_games):
    print(f'\nPlaying game {i+1} of {num_games}:')
    game_loop(initial_state, model, optimizer, device, off_policy)

def game_loop(initial_state, model, optimizer, device, off_policy):
  '''Training loop that plays one game'''
  # Just in case
  optimizer.zero_grad()
  
  # Initialization
  state    = initial_state
  score, _ = model(state.unsqueeze(0))
  v_t      = optimizer.restart(score)
  
  # Progress Bar
  bar      = ProgressBar(284)
  
  while True:

    # Determine the next move
    game_over, moved_off_policy, new_state, score = \
      get_next_move_training(state, model, device, off_policy = off_policy)
    
    if game_over:      
      delta = 1 - v_t
      optimizer.step(delta, update_trace = False)
      
      # Terminate the progress bar
      bar.terminate()

      break
    
    elif moved_off_policy:
      # Equivalent to starting a new game
      v_t = optimizer.restart(score)
      
    else:
      score.backward()
      delta = (1 - score) - v_t
      optimizer.step(delta)
      optimizer.zero_grad()
      
      v_t   = score.item()
      state = new_state
      
    # Progress bar
    bar.step()
    

