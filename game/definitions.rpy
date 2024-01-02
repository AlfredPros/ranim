
## General ##########################################################################################################################################
define start_at_label = "start"
define timer_dur = 0.0325  # Screens refresh rate

## Colors ###########################################################################################################################################
define cblue = "#4AB2D7"
define cgreen = "#4AB8A7"
define cyellow = "#F8E500"
define cred = "#FF6F51"
define cpurple = "#D575C4"
define cpink = "#CA6C7A"
define cbrown = "#746357"
define cgray = "#1F1F1F"
define clblue = "#9ED5E6"  # Light blue
define cdblue = "#269DC8"  # Dark blue

## Sizes ############################################################################################################################################
define size_h1 = 72
define size_h2 = 64  # Default text size
define size_h3 = 56
define size_h4 = 48
define size_h5 = 42
define size_h6 = 36

## Transitions ######################################################################################################################################
define diss_diag = ImageDissolve("disslr", 1.0, ramplen=256)
define diss = Dissolve(1.0)

## Custom Text ######################################################################################################################################
style dialogue_text:
    size size_h2
    align(0.5, 0.875)
    text_align 0.5
    slow_cps True
    slow_abortable True  # Skippable only if a normal text is also skippable in the background. ""
    outlines [ (9, "#0f0f0f17", absolute(0), absolute(0)), (6, "#0f0f0f30", absolute(0), absolute(0)),  (3, "#0f0f0f90", absolute(0), absolute(0)) ]
    font "cmunss.ttf"
image dialogue = ParameterizedText(style="dialogue_text")

## Mouse configuration ##############################################################################################################################
define config.mouse = {}
define config.mouse["say"] = [("images/util/empty32.png", 0, 0)]
define config.mouse["with"] = [("images/util/empty32.png", 0, 0)]
define config.mouse["pause"] = [("images/util/cursor32.png", 0, 0)]
define config.mouse["button"] = [("images/util/cursor32.png", 0, 0)]

## Transforms #######################################################################################################################################
## Despite screens already have premade properties in them, you can use transform to customize how they look as you like ############################
transform moveup(y=0.5):
    yalign y+0.02
    ease_quad 1.0 yalign y
    
transform arrowhead(angle, color, alpha=1.0):  # This transform is made only for arrow head
    matrixcolor TintMatrix(color)
    rotate angle
    alpha alpha
    
transform diss_show(dur=1.0):
    alpha 0.0
    ease_quad dur alpha 1.0

# Use this transform if you plan on using color_change transform afterwards.
# ex. Having red square. Then change the color to blue.
transform color_base(color="#fff"):
    matrixcolor TintMatrix(color)

# Mind you that this color change is dependent on the displayable color property. 
# ex. If red square (color="#f00") changed to blue (color="#00f") will result in grey because the red square doesn't have any blue value.
transform color_change(dur=1.0, color_from="#fff", color_to="#fff"):
    matrixcolor TintMatrix(color_from)
    ease_quad dur matrixcolor TintMatrix(color_to)

## Utility Python Functions #########################################################################################################################
init python:
    import math
    def sin(angle):
        return math.sin(math.radians(angle))
    def cos(angle):
        return math.cos(math.radians(angle))
        
    def round_num(num, dec_point=2):
        return (num//pow(10, -dec_point)) / float(pow(10, dec_point))
        
    def quad_left_side(x):  # Input: [0.0, 0.5] Output: [0.0, 0.5]. Based on ease_quad.
        return 2 * x * x
    def quad_right_side(x):  # Input: [0.5, 1.0]. Output: [0.5, 1.0]. Based on ease_quad.
        return 1 - pow(-2 * x + 2, 2) / 2
    def pan_denormalize(x):  # Input: [0.0, 1.0]. Output: [-1.0, 1.0]. Convert from 0 to 1 into -1 to 1
        return x * 2 - 1
        
    def distance(x, y):
        return math.sqrt((x*x)+(y*y))
    
## Utility Screens ##################################################################################################################################
screen rectangle_pos(x, y, sizex, sizey, color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    add "whi" at transform_names:
        alpha alpha
        matrixcolor TintMatrix(color)
        pos(x, y)
        size(sizex, sizey)

screen rectangle_align(x, y, sizex, sizey, color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    add "whi" at transform_names:
        alpha alpha
        matrixcolor TintMatrix(color)
        align(x, y)
        size(sizex, sizey)
        
screen circle_pos(x, y, radius, color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    add "whicirl" at transform_names:
        alpha alpha
        matrixcolor TintMatrix(color)
        pos(x, y)
        size(radius*2, radius*2)
        
screen circle_align(x, y, radius, color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    add "whicirl" at transform_names:
        alpha alpha
        matrixcolor TintMatrix(color)
        align(x, y)
        size(radius*2, radius*2)

screen border_pos(x, y, sizex, sizey, width=3, border_color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    use rectangle_pos(x, y, sizex, sizey, border_color, alpha, transform_names)
    use rectangle_pos(x=x+width, y=y+width, sizex=sizex-width*2, sizey=sizey-width*2, color="#000", transform_names=transform_names)
        
screen border_align(x, y, sizex, sizey, width=3, border_color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    use rectangle_align(x, y, sizex, sizey, border_color, alpha, transform_names)
    use rectangle_pos(x=int((window_width*x) - (sizex*x-width)), y=int((window_height*y) - (sizey*y-width)), sizex=sizex-width*2, sizey=sizey-width*2, color="#000", transform_names=transform_names)
        
screen border_pos_circ(x, y, radius=540, width=4, border_color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    use circle_pos(x, y, radius, color=border_color, alpha=1.0, transform_names=transform_names)
    use circle_pos(x+width, y+width, radius-width, color="#000", alpha=1.0, transform_names=transform_names)
    
screen border_align_circ(x, y, radius=540, width=4, border_color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
    
    use circle_align(x, y, radius, color=border_color, alpha=1.0, transform_names=transform_names)
    use circle_pos(x=int((window_width*x) - (radius*2*x-width)), y=int((window_height*y) - (radius*2*y-width)), radius=radius-width, color="#000", transform_names=transform_names)

default morph_progress = 0.0
default morph_change = 0.0
default curr_x = 0
default curr_y = 0
default curr_sizex = 0
default curr_sizey = 0
default curr_radius = 0
screen border_pos_morph(from_x, from_y, from_sizex, from_sizey, to_x, to_y, to_sizex, to_sizey, duration_multiplier=1.0, width=4, border_color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
 
    python:
        morph_progress += (timer_dur/2)*duration_multiplier
        if morph_progress > 1.0:
            morph_progress = 1.0
            
        if morph_progress < 0.5:
            morph_change = quad_left_side(morph_progress)
        else:
            morph_change = quad_right_side(morph_progress)
        
        curr_x = from_x + int((to_x-from_x)*morph_change)
        curr_y = from_y + int((to_y-from_y)*morph_change)
        curr_sizex = from_sizex + int((to_sizex-from_sizex)*morph_change)
        curr_sizey = from_sizey + int((to_sizey-from_sizey)*morph_change)
            
    use border_pos(curr_x, curr_y, curr_sizex, curr_sizey, width, border_color, alpha, transform_names)
 
    if morph_progress != 1.0:
        timer timer_dur/2 action renpy.restart_interaction repeat True
        
screen border_pos_circ_morph(from_x, from_y, from_radius, to_x, to_y, to_radius, duration_multiplier=1.0, width=4, border_color="#fff", alpha=1.0, transform_names=(None)):
    zorder 1
 
    python:
        morph_progress += (timer_dur/2)*duration_multiplier
        if morph_progress > 1.0:
            morph_progress = 1.0
            
        if morph_progress < 0.5:
            morph_change = quad_left_side(morph_progress)
        else:
            morph_change = quad_right_side(morph_progress)
        
        curr_x = from_x + int((to_x-from_x)*morph_change)
        curr_y = from_y + int((to_y-from_y)*morph_change)
        curr_radius = from_radius + int((to_radius-from_radius)*morph_change)
    
    use border_pos_circ(curr_x, curr_y, curr_radius, width, border_color, alpha, transform_names)
 
    if morph_progress != 1.0:
        timer timer_dur/2 action renpy.restart_interaction repeat True
    
screen line_pos(x, y, length, width=3, angle=0, color="#fff", grad=False, transform_names=(None)):
    zorder 1
    
    if grad:
        add "gradline" at transform_names:
            matrixcolor TintMatrix(color)
            pos(x, y)
            size(length, width)
            rotate angle
    else:
        add "whi" at transform_names:
            matrixcolor TintMatrix(color)
            pos(x, y)
            size(length, width)
            rotate angle

screen line_align(x, y, length, width=3, angle=0, color="#fff", grad=False, offx=0, offy=0, transform_names=(None)):
    zorder 1
    
    if grad:
        add "gradline" at transform_names:
            matrixcolor TintMatrix(color)
            align(x, y)
            size(length, width)
            rotate angle
            offset(offx, offy)
    else:
        add "whi" at transform_names:
            matrixcolor TintMatrix(color)
            align(x, y)
            size(length, width)
            rotate angle
            offset(offx, offy)

screen arrow_pos(x, y, length, width=32, angle=0, color="#fff", alpha=1.0):
    zorder 1
    
    frame at (arrowhead(angle, color, alpha)):
        background Frame("arrowhead", Borders(0, 1, 31, 1))
        area(x, y-(length//2), length, width)
        
screen arrow_align(x, y, length, width=32, angle=0, color="#fff"):
    zorder 1
    
    frame at arrowhead(angle, color):
        background Frame("arrowhead", Borders(0, 1, 31, 1))
        area(int((1920*x) - (max(length, width) * x)), int((1080*y) - (max(length, width) * y)), length, width)  # A hacky implementation of positioning.

default dur = 0.0
default curr = 0.0
default progress = 0.0
default amplitude = 1.0
screen audio_progress(x, y, width=720, height=80, channel="music", color="#fff", show_text=False, transform_names=(None)):
    zorder 1
    
    python:
        dur = renpy.music.get_duration(channel=channel)
        curr = renpy.music.get_pos(channel=channel)
        
        
        if dur != None and curr != None and dur != 0:
            progress = curr/dur
        else:
            progress = 0.0
            
        if renpy.music.is_playing(channel=channel):
            amplitude = renpy.audio.audio.get_channel(channel).context.secondary_volume + 0.25
        else:
            amplitude = 0.25
        
    # Box
    use border_pos(x, y, width, height, 5, color, alpha=amplitude, transform_names=transform_names)
    
    # Line
    use line_pos(x+int(width*progress)-(height//2), y, height, 5, angle=90, transform_names=transform_names)
    
    if show_text:
        text channel + " (" + str((progress // 0.001) / 10.0) + "%)":
            color color
            pos(x+width+32, y+height-80)

    timer timer_dur action renpy.restart_interaction repeat True

default code_text = [""]
screen show_code(x, y, size=size_h3, code_text=code_text):
    zorder 2
    vbox:
        spacing size//4
        pos(x, y)
        
        for i in code_text:
            text i at diss_show:
                size size
                font "cmunbtl.ttf"






