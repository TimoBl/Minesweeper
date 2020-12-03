import ui
import random
import time
import DefaultTheme
import DarkTheme
import MarineTheme
import DefaultTheme as viewCtrl
import sound
from objc_util import *

UIDevice = ObjCClass('UIDevice')

def taptic_peek():
	sound.play_effect("SoundAsset/explosion.caf")
	d = UIDevice.new()
	t = d._tapticEngine()
	try: 
		t.actuateFeedback_(0)
	except:
		pass
	
def taptic_pop():
	sound.play_effect("SoundAsset/click.caf")
	d = UIDevice.new()
	t = d._tapticEngine()
	try:
		t.actuateFeedback_(1)
	except:
		pass
	
def taptic_triple_knock():
	d = UIDevice.new()
	t = d._tapticEngine()
	try:
		t.actuateFeedback_(2)
	except:
		pass
	
	
class view(ui.View):
	def __init__(self):
		self.present("fullscreen", hide_title_bar=True, animated=False)
		self = viewCtrl.view(self)
		self.background_color = '#676767'
		
	def closing(self, this):
		self.close()
		
		
class menu(ui.View):
	def __init__(self, game):
		if v.height > v.width:
			width = int(4 * v.width / 5)
			height = int(3.5 * v.height / 5)
		else:
			width = int(v.width / 3)
			height = int(3.5 * v.height / 5)
		centerX = (v.width / 2) - (width / 2)
		centerY = (v.height / 2) - (v.height / 2) + game.top
		self.name = "menu"
		self.frame = (centerX, centerY + int(v.height / 20), width, height)
		self.game = game
		self.showing = False
		
		#background
		background = ui.ImageView(name = "menu_background")
		background = viewCtrl.menu_background(background)
		background.width = self.width
		background.height = self.height
		self.add_subview(background)
		
		#title
		title = ui.Label(name = "menu_title")
		title.text = "Settings"
		title.width = self.width
		title.height = self.height / 8
		title.center = (self.width / 2, self.height / 10)
		title = viewCtrl.menu_title(title)
		self.title = title
		self.add_subview(self.title)
		
		#best score
		title = ui.Label(name = "best_score")
		title.width = self.width
		title.height = self.height / 8
		title.center = (self.width / 2, 2 * self.height / 10)
		title = viewCtrl.best_score_title(title)
		self.best_score_title = title
		self.add_subview(self.best_score_title)
		
		#width slider
		#title
		title = ui.Label(name = "width_title")
		title.text = "Width"
		title.width = self.width / 4
		title.height = self.height / 8
		title.center = (self.width / 5, 3 * self.height / 10)
		title = viewCtrl.width_title(title)
		self.width_title = title
		self.add_subview(self.width_title)
		#slider
		slider = ui.Slider(name = "width_slider")
		slider.width = self.width / 2.5
		slider.height = self.height / 8
		slider.center = (4 * self.width / 7, 3 * self.height / 10)
		slider.value = (self.game.width - self.game.minWidth) / self.game.maxWidth
		slider.continuous = True
		slider.action = self.change_width_value
		self.width_slider = slider
		self.add_subview(self.width_slider)
		#value
		label = ui.Label(name = "width_value_label")
		label.text = str(self.game.width)
		label.width = self.width / 4
		label.height = self.height / 8
		label.center = (5 * self.width / 6, 3 * self.height / 10)
		label = viewCtrl.width_value(label)
		self.width_value_label = label
		self.add_subview(self.width_value_label)
		
		#bomb slider
		#title
		title = ui.Label(name = "bomb_title")
		title.text = "Bombs"
		title.width = self.width / 4
		title.height = self.height / 8
		title.center = (self.width / 5, 5 * self.height / 10)
		title = viewCtrl.bomb_title(title)
		self.bomb_title = title
		self.add_subview(self.bomb_title)
		#slider
		slider = ui.Slider(name = "bomb_slider")
		slider.width = self.width / 2.5
		slider.height = self.height / 8
		slider.center = (4 * self.width / 7, 5 * self.height / 10)
		slider.value = (self.game.bombs - self.game.minBombs) / self.game.maxBombs
		slider.continuous = True
		slider.action = self.change_bomb_value
		self.bomb_slider = slider
		self.add_subview(self.bomb_slider)
		#value
		label = ui.Label(name = "bomb_value_label")
		label.text = str(self.game.bombs)
		label.width = self.width / 4
		label.height = self.height / 8
		label.center = (5 * self.width / 6, 5 * self.height / 10)
		label = viewCtrl.bomb_value(label)
		self.bomb_value_label = label
		self.add_subview(self.bomb_value_label)
		
		#buttons for themes
		#Default Theme
		button = ui.Button(name = "DefaultTheme")
		button.title = "Default"
		button.width = self.width / 4
		button.height = self.height / 10
		button.center = (button.width, 7 * self.height / 10)
		button.action = self.game.change_theme
		button = DefaultTheme.new_game_button(button)
		self.new_game_button = button
		self.add_subview(self.new_game_button)
		#Dark theme
		button = ui.Button(name = "DarkTheme")
		button.title = "Dark"
		button.width = self.width / 4
		button.height = self.height / 10
		button.center = (self.width / 2, 7 * self.height / 10)
		button.action = self.game.change_theme
		button = DarkTheme.new_game_button(button)
		self.new_game_button = button
		self.add_subview(self.new_game_button)
		#Marine theme
		button = ui.Button(name = "MarineTheme")
		button.title = "Marine"
		button.width = self.width / 4
		button.height = self.height / 10
		button.center = (self.width-button.width, 7 * self.height / 10)
		button.action = self.game.change_theme
		button = MarineTheme.new_game_button(button)
		self.new_game_button = button
		self.add_subview(self.new_game_button)
		
		#new game
		button = ui.Button(name = "new_game_button")
		button.title = "NewGame"
		button.width = self.width / 2
		button.height = self.height / 10
		button.center = (self.width / 2, self.height - 1.2 * button.height)
		button.action = self.game.new_game
		button = viewCtrl.new_game_button(button)
		self.new_game_button = button
		self.add_subview(self.new_game_button)
		
		#exit (only for developpement purposes)
		exit_button = ui.Button(name = "exit_button")
		exit_button.width = 40
		exit_button.height = 40
		exit_button.center = (25, 25)
		exit_button.action = v.closing
		exit_button.alpha = 0.5
		exit_button.background_image = ui.Image.named('iow:close_256').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		self.exit_button = exit_button
		self.add_subview(exit_button)
		
	def initialize_sliders(self):
		value = float(self.game.width - self.game.minWidth) / float(self.game.maxWidth - self.game.minWidth)
		self.width_slider.value = value
		self.width_value_label.text = str(self.game.width)
		
		value = float(self.game.bombs - self.game.minBombs) / self.game.maxBombs
		self.bomb_slider.value = value
		self.bomb_value_label.text = str(self.game.bombs)
		
	def change_width_value(self, this):
		value = self.game.minWidth + int(this.value * (self.game.maxWidth - self.game.minWidth))
		self.game.width = value
		self.width_value_label.text = str(value)
		self.game.maxBombs = int(self.game.width * self.game.height / 2)
		self.game.bombs = int(self.bomb_slider.value * (self.game.minBombs + self.game.maxBombs))
		if self.game.bombs < self.game.minBombs:
			self.game.bombs = self.game.minBombs
		self.bomb_value_label.text = str(self.game.bombs)
		
	def change_bomb_value(self, this):
		value = int(self.game.minBombs + (this.value * (self.game.maxBombs - self.game.minBombs)))
		self.game.bombs = value
		self.bomb_value_label.text = str(value)
		
	def change_state(self, this):
		if self.showing == False:
			self.show()
		else:
			self.hide()
			
	def show(self):
		if self.game.paused == False:
			self.best_score_title.text = "Best Score: " + str(self.game.best_score)
			button = self.game.top_menu.pause_button
			button = viewCtrl.top_start_button(button)
			self.initialize_sliders()
			self.game.paused = True
			self.game.change_button_state(False)
			self.showing = True
			v.add_subview(self)
			
	def hide(self):
		if self.game.paused == True:
			button = self.game.top_menu.pause_button
			button = viewCtrl.top_pause_button(button)
			self.game.paused = False
			self.showing = False
			if self.game.dead == False:
				self.game.change_button_state(True)
			v.remove_subview(self)
			
class top_menu(ui.View):
	def __init__(self, game, menu):
		v.add_subview(self)
		if v.height > v.width:
			self.y = int(game.top / 3)
		else:
			self.y = int(game.top / 8)
		self.width = v.width
		self.height = game.top - self.y
		self.menu = menu
		self.game = game
		
		#background
		background = ui.ImageView(name = "background")
		background.width = v.width
		background.height = self.height
		
		background.center = (v.width / 2, self.height / 2)
		background = viewCtrl.top_background(background)
		self.background = background
		self.add_subview(background)
		
		#pause button
		button = ui.Button(name = "pause_button")
		button.width = self.height
		button.height = 2 * self.height / 3
		button.center = (self.height / 2, self.height / 2)
		button.action = self.menu.change_state
		button = viewCtrl.top_pause_button(button)
		self.pause_button = button
		self.add_subview(self.pause_button)
		
		#restart button
		button = ui.Button(name = "restart_button")
		button.width = int(2 * self.height / 3)
		button.height = int(2 * self.height / 3)
		button.center = (v.width / 2, self.height / 2)
		button.action = self.game.new_game
		button = viewCtrl.top_restart_button(button)
		self.restart_button = button
		self.add_subview(self.restart_button)
		
		#score label
		label = ui.Label(name = "score_label")
		label.text = "0"
		label.width = self.height * 1.2
		label.height = 3 * self.height / 5
		label.center = (v.width / 2 - label.width / 2 - self.restart_button.width / 2, self.height / 2)
		label = viewCtrl.top_score_label(label)
		self.score_label = label
		self.add_subview(self.score_label)
		
		#time label
		label = ui.Label(name = "time_label")
		label.text = "000"
		label.width = self.height * 1.2
		label.height = 3 * self.height / 5
		label.center = (v.width / 2 + label.width / 2 + self.restart_button.width / 2, self.height / 2)
		label = viewCtrl.top_time_label(label)
		self.time_label = label
		self.add_subview(self.time_label)
		
		#flag button
		button = ui.Button(name = "flag_button")
		button.width = 2 * self.height / 3
		button.height = 2 * self.height / 3
		button.center = (v.width - (self.height / 2), self.height / 2)
		button.action = self.change_flag
		button = viewCtrl.top_flag_down(button)
		self.flag_button = button
		self.add_subview(self.flag_button)
		
	def change_flag(self, this):
		if this == True or this == False:
			self.game.flagged = this
		else:
			self.game.flagged = not self.game.flagged
			
		taptic_peek()
		if self.game.flagged:
			self.flag_button = viewCtrl.top_flag_up(self.flag_button)
		else:
			self.flag_button = viewCtrl.top_flag_down(self.flag_button)
			
class GameView(ui.View):
	def __init__(self, game):
		self.name = "GameView"
		self.game = game
		self.init_variables()
		self.init_view()
		self = viewCtrl.game_view(self)
		self.init_board_view()
		
	def init_variables(self):
		self.sw = int(v.width / self.game.width)
		self.sh = self.sw
		self.game.height = int((v.height - self.game.top) / self.sh)
		self.aw = (v.width - (self.game.width * self.sw)) / 2
		self.ah = (v.height - self.game.top - (self.game.height * self.sh)) / 2
		
	def init_view(self):
		width = self.game.width * self.sw
		if v.height > v.width:
			height = int(self.game.height * self.sh - 1 * self.sh)
		else:
			height = int(self.game.height * self.sh)
		self.frame = (self.aw, self.ah + self.game.top, width, height)
		v.add_subview(self)
		
	def init_board_view(self):
		self.game.button_board = []
		for h in range(self.game.height):
			line = []
			for w in range(self.game.width):
				w1 = int(self.sw * w + self.sw/2)
				h1 = int(self.sh * h + self.sh/2)
				name = str(h * 100 + w)
				button = ui.Button(name = name)
				button.enabled = False
				button.parent_view = self
				button.width = self.sw
				button.height = self.sh
				button.center = (w1, h1)
				button = viewCtrl.gray_box(button)
				button.action = self.game.button_tapped
				line.append(button)
				self.add_subview(button)
			self.game.button_board.append(line)
			
	def closing(self):
		v.remove_subview(self)
		
		
class Game:
	def __init__(self):
		#global variables
		self.best_score = 0
		self.theme = 0
		
		self.minWidth = 6
		self.width = 0
		self.maxWidth = 20
		
		self.minBombs = 2
		self.bombs = 0
		self.maxBombs = 40
		
		#set variables
		self.get_settings()
		self.init_variables()
		
		#set theme
		self.set_theme()
		
		#set menus
		self.menu = menu(self)
		self.top_menu = top_menu(self, self.menu)
		
		#make new game
		self.new_game(None)
		self.update()
		
	def new_game(self, this):
		self.menu.hide()
		self.init_view()
		self.init_variables()
		self.init_board()
		button = self.top_menu.restart_button
		button = viewCtrl.top_restart_button(button)
		self.empty_spaces = (self.width * self.height) - self.bombs
		self.top_menu.change_flag(False)
		self.setScore()
		self.change_button_state(True)
		
	def set_theme(self):
		global viewCtrl
		if self.theme == 1:
			import DarkTheme as viewCtrl
		elif self.theme == 2:
			import MarineTheme as viewCtrl
		else:
			import DefaultTheme as viewCtrl
		self.set_settings()
		
	def change_theme(self, sender):
		try:
			name = sender.name
			if name == "DefaultTheme":
				self.theme = 0
			if name == "DarkTheme":
				self.theme = 1
			elif name == "MarineTheme":
				self.theme = 2
		except:
			pass
			
		self.set_theme()
		v.remove_subview(self.menu)
		v.remove_subview(self.top_menu)
		v.remove_subview(self.game_view)
		self.menu = menu(self)
		self.top_menu = top_menu(self, self.menu)
		self.new_game(None)
		
	def init_view(self):
		try:
			self.game_view.closing()
		except:
			pass
		self.game_view = GameView(self)
		
	def init_variables(self):
		self.paused = False
		self.dead = False
		self.flagged = False
		self.first_press = True
		self.delta_time = 0
		if v.height > v.width:
			self.top = int(v.height / 8)
		else:
			self.top = int(v.height / 5)
		self.empty_count = 0
		
	def init_board(self):
		#init_board
		self.board = []
		for h in range(self.height):
			line = []
			for w in range(self.width):
				line.append("empty")
			self.board.append(line)

	def init_bombs(self, not_w, not_h):
		#init_bombs
		self.first_press = False
		x = self.bombs
		while x > 0:
			w = random.randrange(self.width)
			h = random.randrange(self.height)
			if self.board[h][w] == "empty" and not (abs(w - not_w) <= 1 and abs(h - not_h) <= 1):
				self.board[h][w] = "bomb"
				x -= 1
			else:
				pass
				
	def button_tapped(self, sender):
		if self.paused == False and self.dead == False:
			n = int(sender.name)
			h = int(n / 100)
			w = n - h * 100
			if self.first_press == True:
				self.init_bombs(w, h)
			
			if self.flagged == False:
				if self.board[h][w] == "bomb":
					self.board[h][w] = "exploded_bomb"
					sender = viewCtrl.exploded_bomb(sender)
					taptic_triple_knock()
					self.death()
				elif self.board[h][w] == "empty":
					self.board[h][w] = "uncovered"
					self.empty_count += 1
					bomb_count = self.get_bomb_count(w, h)
					sender.action = None
					taptic_pop()
					if bomb_count > 0:
						sender = viewCtrl.count_box(sender)
						sender.tint_color = viewCtrl.get_text_color(bomb_count)
						sender.title = str(bomb_count)
					else:
						sender = viewCtrl.empty_box(sender)
						sender.enabled = False
						self.reveal(w, h)
				elif self.board[h][w] == "flagged" or self.board[h][w] == "flagged_bomb":
					pass
			else:
				if self.board[h][w] == "flagged":
					self.board[h][w] = "empty"
					sender = viewCtrl.gray_box(sender)
				elif self.board[h][w] == "empty":
					self.board[h][w] = "flagged"
					sender = viewCtrl.flagged_box(sender)
				elif self.board[h][w] == "bomb":
					self.board[h][w] = "flagged_bomb"
					sender = viewCtrl.flagged_box(sender)
				elif self.board[h][w] == "flagged_bomb":
					self.board[h][w] = "bomb"
					sender = viewCtrl.gray_box(sender)
					
			self.setScore()
			
			if self.empty_count == self.empty_spaces:
				self.win()
		else:
			pass
			
	def setScore(self):
		score = self.empty_spaces - self.empty_count
		if score < 100 and score >= 10:
			score_str = "0" + str(score)
		elif score < 10:
			score_str = "00" + str(score)
		else:
			score_str = str(score)
		self.top_menu.score_label.text = score_str
		
	def change_button_state(self, state):
		if self.button_board != None:
			taptic_peek()
			for h in range(self.height):
				for w in range(self.width):
					try:
						self.button_board[h][w].enabled = state
					except:
						pass
						
	def get_bomb_count(self, w, h):
		bomb_count = 0
		for h1 in range(-1, 2):
			for w1 in range(-1, 2):
				h2 = h + h1
				w2 = w + w1
				if h2 < 0 or h2 >= self.height or w2 < 0 or w2 >= self.width:
					pass
				elif self.board[h2][w2] == "bomb" or self.board[h2][w2] == "flagged_bomb":
					bomb_count += 1
		return bomb_count
		
	def update(self):
		while True:
			if self.paused == False and self.dead == False:
				self.delta_time += 1
				
				minutes = int(self.delta_time / 60)
				seconds = self.delta_time - minutes * 60
				
				if minutes < 10:
						#change label
					minutes_str = str(minutes)
					if seconds < 10:
						seconds_str = "0" + str(seconds)
					else:
						seconds_str = str(seconds)
					self.top_menu.time_label.text = minutes_str + ":" + seconds_str
				else:
					#time limit
					self.death()
					
				time.sleep(1)
				
	def reveal(self, w, h):
		positions = []
		positions.append([w, h])
		while len(positions) > 0:
			new_positions = []
			for i in range(len(positions)):
				w = positions[i][0]
				h = positions[i][1]
				list_w = [1, -1, 0, 0]
				list_h = [0, 0, 1, -1]
				for i2 in range(len(list_w)):
					w1 = list_w[i2] + w
					h1 = list_h[i2] + h
					if h1 >= 0 and h1 < self.height and w1 >= 0 and w1 < self.width:
						if self.board[h1][w1] == "empty":
							button = self.button_board[h1][w1]
							self.board[h1][w1] = "uncovered"
							self.empty_count += 1
							bomb_count = self.get_bomb_count(w1, h1)
							button.action = None
							if bomb_count > 0:
								button = viewCtrl.count_box(button)
								button.tint_color = viewCtrl.get_text_color(bomb_count)
								button.title = str(bomb_count)
							else:
								button = viewCtrl.empty_box(button)
								button.enabled = False
								if [w1, h1] not in new_positions:
									new_positions.append([w1, h1])
							
			positions = new_positions
			
	def win(self):
		button = self.top_menu.restart_button
		button = viewCtrl.win_smile(button)
		score = self.get_score()
		if score > self.best_score:
			self.best_score = score
		self.won_games += 1
		self.dead = True
		self.top_menu.score_label.text = "Won!"
		self.set_settings()
		self.change_button_state(False)
		for h in range(self.height):
			for w in range(self.width):
				if self.board[h][w] == "bomb" or self.board[h][w] == "flagged_bomb":
					#mark the found bombs
					button = self.button_board[h][w]
					button = viewCtrl.bomb(button)
					
	def death(self):
		button = self.top_menu.restart_button
		button = viewCtrl.lost_smile(button)
		self.dead = True
		self.lost_games += 1
		self.top_menu.score_label.text = "Lost"
		self.set_settings()
		self.change_button_state(False)
		self.reveal_final()
		
	def reveal_final(self):
		for h in range(self.height):
			for w in range(self.width):
				button = self.button_board[h][w]
				if self.board[h][w] == "bomb":
					#mark the unfound bombs
					button = viewCtrl.exploded_bomb(button)
				elif self.board[h][w] == "flagged":
					#mark the false flagged bombs
					button = viewCtrl.none_bomb(button)
					
	def get_score(self):
		w = self.width
		h = self.height
		b = self.bombs
		t = self.delta_time
		if t != 0:
			score = int((w * h * (b**2)) / t)
		else:
			score = 0
		return score
		
	def get_settings(self):
		file = open("Settings.txt", "r")
		text = file.readlines()
		try:
			best_score = int(text[0])
			width = int(text[1])
			bombs = int(text[2])
			theme = int(text[3])
			won_games = int(text[4])
			lost_games = int(text[5])
		except:
			best_score = 0
			width = 5
			bombs = 5
			theme = 0
			won_games = 0
			lost_games = 0
		self.width = width
		self.bombs = bombs
		self.theme = theme
		self.won_games = won_games
		self.lost_games = lost_games
		file.close()
		
	def set_settings(self):
		file = open("Settings.txt", "w")
		text = str(self.best_score) + "\n" + str(self.width) + "\n" + str(self.bombs) + "\n" + str(self.theme) + "\n" + str(self.won_games) + "\n" + str(self.lost_games)
		file.write(text)
		file.close()
		
v = view()
newGame = Game()
