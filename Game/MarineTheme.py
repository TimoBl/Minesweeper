import ui
import time

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
    background.image = ui.Image.named('MarineAsset/BackGround.png').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
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
    v.image = ui.Image.named('MarineAsset/MenuBackground.png').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
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
    v.background_image = ui.Image.named("MarineAsset/TopBackground.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v

#top    
def top_background(v):
    v.image = ui.Image.named("MarineAsset/TopBackground.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_pause_button(v):
    v.background_image = ui.Image.named("MarineAsset/Pause.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_start_button(v):
    ui.Image.named('MarineAsset/RightArrow.png').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_restart_button(v):
    v.background_image = ui.Image.named("MarineAsset/Smile.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_score_label(v):
    v.text_color = '#3300b2'
    v.font = ('Noteworthy', int(v.height)/1.5)
    v.alignment = ui.ALIGN_CENTER
    v.background_color = "white"
    return v
    
def top_time_label(v):
    v.text_color = '#3300b2'
    v.font = ("Noteworthy", int(v.height/1.5))
    v.alignment = ui.ALIGN_CENTER
    v.background_color = "white"
    return v
    
def top_flag_down(v):
    v.background_image = ui.Image.named("MarineAsset/FlagDown.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def top_flag_up(v):
    v.background_image = ui.Image.named("MarineAsset/FlagUp.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def gray_box(v):
    v.background_image = ui.Image.named("MarineAsset/GrayBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    v.font = ('<System-Bold>', int(v.height))
    return v
        
def exploded_bomb(v):
    img = ui.Image.named("MarineAsset/ExplodedBomb.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)

    def show():
        im.frame = (v.x,v.y,v.width,v.height)

    def end():
        v.parent_view.remove_subview(im)
        im.close()
        v.background_image = img
        
    im = ui.ImageView()
    im.image = img
    im.frame = (v.x+v.width/2,v.y+v.height/2,0,0)
    
    v.background_image = None
    v.parent_view.add_subview(im)
    ui.animate(show, 1.0)
    ui.delay(end, 1.0)
    return v
    
def empty_box(v):
    v.background_image = None
    return v
    
def count_box(v):
    img = ui.Image.named("MarineAsset/CountBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)

    def show():
        im.frame = (v.x,v.y,v.width,v.height)
        im.alpha = 1.0
    
    def end():
        v.parent_view.remove_subview(im)
        im.close()
        v.background_image = img
            
    im = ui.ImageView()
    im.image = img
    im.frame = (v.x-v.width, v.y-v.height,v.width*4,v.height*4)
    im.alpha = 0.0
    
    v.background_image = None
    v.parent_view.add_subview(im)
    ui.animate(show, 0.5)
    ui.delay(end, 0.5)
    return v
    
def flagged_box(v):
    img = ui.Image.named("MarineAsset/FlaggedBox.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    
    def show():
        im.frame = (v.x,v.y,v.width,v.height)
        im.alpha = 1.0
    
    def end():
        v.parent_view.remove_subview(im)
        im.close()
        v.background_image = img
            
    im = ui.ImageView()
    im.image = img
    im.frame = (v.x-v.width, v.y-v.height,v.width*4,v.height*4)
    im.alpha = 0.0
    
    v.background_image = None
    v.parent_view.add_subview(im)
    ui.animate(show, 1.0)
    ui.delay(end, 1.0)
    return v
    
def win_smile(v):
    v.background_image = ui.Image.named("MarineAsset/WinSmile.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def bomb(v):
    v.background_image = ui.Image.named("MarineAsset/Bomb.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def lost_smile(v):
    v.background_image = ui.Image.named("MarineAsset/LostSmile.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    return v
    
def none_bomb(v):
    v.background_image = ui.Image.named("MarineAsset/NoneBomb.png").with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
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
