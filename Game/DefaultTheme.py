import ui

#view
def view(v):
    background = ui.ImageView(name = "background")
    background.width = v.width
    background.height = v.height
    v.add_subview(background)
    return v
    
#game view
def game_view(v):
    background = ui.ImageView(name = "background")
    background.width = v.width
    background.height = v.height
    background.background_color = '#434343'
    v.add_subview(background)
    return v

#menu
def menu_title(v):
	v.text_color = "white"
	v.font = ("Helvetica", 2 * v.height / 3)
	v.alignment = ui.ALIGN_CENTER
	return v
	
def best_score_title(v):
	v.text_color = "white"
	v.font = ("Helvetica", v.height / 4)
	v.alignment = ui.ALIGN_CENTER
	return v

def menu_background(v):
	v.image = ui.Image.named('DefaultAsset/MenuBackground.png').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
	return v

def width_title(v):
    v.text_color = "white"
    v.font = ("Helvetica", int(v.height / 3.5))
    v.alignment = ui.ALIGN_CENTER
    return v
    
def width_value(v):
    v.text_color = "white"
    v.font = ("Helvetica", int(v.height / 3))
    v.alignment = ui.ALIGN_CENTER
    return v
  
def bomb_title(v):
    v.text_color = "white"
    v.font = ("Helvetica", int(v.height / 3.5))
    v.alignment = ui.ALIGN_CENTER
    return v
    
def bomb_value(v):
    v.text_color = "white"
    v.font = ("Helvetica", int(v.height / 3))
    v.alignment = ui.ALIGN_CENTER
    return v
     
def new_game_button(v):
    v.tint_color = "white"
    v.font = ("Helvetica", int(v.height / 3))
    v.background_image = ui.Image.named("DefaultAsset/TopBackground.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v

#top    
def top_background(v):
    v.image = ui.Image.named("DefaultAsset/TopBackground.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_pause_button(v):
    v.background_image = ui.Image.named("DefaultAsset/Pause.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_start_button(v):
    ui.Image.named('DefaultAsset/RightArrow.png').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_restart_button(v):
    v.background_image = ui.Image.named("DefaultAsset/Smile.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_score_label(v):
    v.text_color = "red"
    v.font = ("DIGITALDREAM", int(v.height/2))
    v.alignment = ui.ALIGN_CENTER
    v.background_color = "black"
    return v
    
def top_time_label(v):
    v.text_color = "red"
    v.font = ("DIGITALDREAM", int(v.height/2))
    v.alignment = ui.ALIGN_CENTER
    v.background_color = "black"
    return v
    
def top_flag_down(v):
    v.background_image = ui.Image.named("DefaultAsset/FlagDown.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_flag_up(v):
    v.background_image = ui.Image.named("DefaultAsset/FlagUp.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def gray_box(v):
    v.background_image = ui.Image.named("DefaultAsset/GrayBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    v.font = ('<System-Bold>', int(v.height))
    return v
    
def exploded_bomb(v):
    v.background_image = ui.Image.named("DefaultAsset/ExplodedBomb.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def empty_box(v):
    v.background_image = ui.Image.named("DefaultAsset/EmptyBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def count_box(v):
    v.background_image = ui.Image.named("DefaultAsset/EmptyBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def flagged_box(v):
    v.background_image = ui.Image.named("DefaultAsset/FlaggedBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def win_smile(v):
    v.background_image = ui.Image.named("DefaultAsset/WinSmile.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def bomb(v):
    v.background_image = ui.Image.named("DefaultAsset/Bomb.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def lost_smile(v):
    v.background_image = ui.Image.named("DefaultAsset/LostSmile.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def none_bomb(v):
    v.background_image = ui.Image.named("DefaultAsset/NoneBomb.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def get_text_color(index):
    count_color = {
        0: '#b2b2b2',
        1: '#0db500',
        2: '#f0da00',
        3: '#ff6800',
        4: '#e70000',
        5: '#4c0089',
        6: '#000000'
    }
    return count_color[index]
