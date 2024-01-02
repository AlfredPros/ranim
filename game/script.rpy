
# This is a basic label, but you can change where the first label goes to in definition.rpy
label start:

    scene black
    
    show text "Welcome to {color=[cblue]}Ranim{/color}!" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "Feel free to look around!" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
label hub:
    
    scene multibg
    show screen hub_choice
    with diss
    
    pause
    
    return
    
label label_color:
    
    hide screen hub_choice
    scene black
    with diss
    
    pause
    
    show text "Default colors":
        align(0.5, 0.2)
    show screen all_colors
    with diss_diag
    
    pause
    
    hide screen all_colors
    scene black
    with diss_diag

    jump hub
    
label label_transitions:
    hide screen hub_choice
    scene black
    with diss
    
    pause
    
    show text "Default transitions" as text1 with diss_diag:
        align(0.5, 0.2)
    
    pause
    
    # Dissolve
    show text "diss" as text2 with diss:
        align(0.5, 0.45)
    
    pause
    
    # Dissolve Diagonal
    show text "diss_diag" as text3 with diss_diag:
        align(0.5, 0.65)
    
    pause
    
    scene black with diss_diag
    
    show text "Default transforms" as text1 with diss_diag:
        align(0.5, 0.15)
    
    pause
    
    # Move Up Align
    show text "moveup(y=0.35)" as text2 at moveup(y=0.35)
    
    pause
    
    # Dissolve Show
    show text "diss_show(dur=1.0)" as text3 at diss_show(dur=1.0):
        align(0.5, 0.5)
    
    pause
    
    # Base Color
    show text "color_base(color=cblue)" as text4 at color_base(color=cblue):
        align(0.5, 0.65)
    
    pause
    
    # Change Color
    show text "color_change(dur=1.0, color_from=cred, color_to=cgreen)" as text5 at color_change(dur=1.0, color_from=cred, color_to=cgreen):
        align(0.5, 0.8)
    
    pause
    
    scene black with diss_diag

    jump hub
    
label label_components:
    hide screen hub_choice
    scene black
    with diss
    
    pause
    
    show text "rectangle_pos" as text1:
        align(0.2, 0.1)
    show text "rectangle_align" as text2:
        align(0.8, 0.1)
    show text "border_pos" as text3:
        align(0.21, 0.6)
    show text "border_align" as text4:
        align(0.79, 0.6)
    
    show screen rectangle_pos(400, 250, 200, 200)
    show screen rectangle_align(0.765, 0.3, 200, 200)
    show screen border_pos(400, 750, 200, 200)
    show screen border_align(0.765, 0.84, 200, 200)
    
    pause
    
    hide screen rectangle_pos
    hide screen rectangle_align
    hide screen border_pos
    hide screen border_align
    scene black
    
    pause
    
    show text "circle_pos" as text1:
        align(0.214, 0.1)
    show text "circle_align" as text2:
        align(0.785, 0.1)
    show text "border_pos_circ" as text3:
        align(0.186, 0.6)
    show text "border_align_circ" as text4:
        align(0.816, 0.6)
    
    show screen circle_pos(400, 250, 100)
    show screen circle_align(0.765, 0.3, 100)
    show screen border_pos_circ(400, 750, 100)
    show screen border_align_circ(0.765, 0.85, 100)
    
    pause
    
    hide screen circle_pos
    hide screen circle_align
    hide screen border_pos_circ
    hide screen border_align_circ
    scene black
    
    pause
    
    show text "line_pos" as text3:
        align(0.225, 0.1)
    show text "line_align" as text4:
        align(0.775, 0.1)
    show text "arrow_pos" as text1:
        align(0.212, 0.6)
    show text "arrow_align" as text2:
        align(0.788, 0.6)
    
    show screen line_pos(400, 210, 200)
    show screen line_align(0.765, 0.25, 200)
    show screen arrow_pos(400, 800, 200)
    show screen arrow_align(0.765, 0.8, 200)
    
    
    pause
    
    hide screen line_pos
    hide screen line_align
    hide screen arrow_pos
    hide screen arrow_align
    scene black
    
    pause
    
    show text "border_pos_morph" as text1:
        align(0.165, 0.1)
    show text "border_pos_circ_morph" as text2:
        align(0.85, 0.1)
    show text "audio_progress" as text3:
        align(0.19, 0.6)
    show text "show_code" as text4:
        align(0.81, 0.6)
    
    show screen border_pos_morph(300, 250, 50, 100,  400, 250, 200, 200)
    show screen border_pos_circ_morph(1200, 250, 50,  1300, 250, 100)
    show screen audio_progress(400, 735, 200)
    $ code_text = ["string = \"{color=[cgreen]}Hello World!{/color}\"",
        "{color=[cyellow]}print{/color}(string)"]
    show screen show_code(1130, 735)
    
    pause
    
    show screen border_pos_morph(400, 250, 200, 200,  500, 250, 300, 50)
    show screen border_pos_circ_morph(1300, 250, 100,  1400, 250, 150)
    play music "<silence .5>"
    $ code_text += ["{color=[cbrown]}# Cool codes ahead{/color}"]
    
    pause
    
    stop music
    hide screen border_pos_morph
    hide screen border_pos_circ_morph
    hide screen audio_progress
    hide screen show_code
    scene black
    
    pause
    
    show dialogue "Instead of using {font=cmunbtl.ttf}{color=[cyellow]}show{/color} text{/font}, you can \nuse {font=cmunbtl.ttf}{color=[cyellow]}show{/color} dialogue{/font} to simulate a dialogue text!"
    
    pause
    
    show dialogue "It is possible to {outlinecolor=[cgray]}change{/outlinecolor} text outline {outlinecolor=[cbrown]}midsentence{/outlinecolor}!"
    
    pause
    
    hide dialogue

    jump hub
    
label label_other:
    hide screen hub_choice
    scene black
    with diss
    
    pause
    
    show text "Multiple transform component" as text1 with diss_diag:
        align(0.5, 0.15)
    
    pause
    
    show screen rectangle_pos(450, 400, 300, 400, transform_names=(color_change(color_from=cred, color_to=cblue), diss_show(0.5))) 
    
    pause
    
    show screen line_pos(700, 400, 400, angle=90, transform_names=(color_change(color_from=cpurple, color_to=cyellow), diss_show(0.5))) 
    
    pause
    
    show screen border_pos_circ(1050, 400, 200, transform_names=(rgb_change, diss_show(0.5), moveup(0.6))) 
    
    pause
    
    hide screen rectangle_pos 
    hide screen line_pos
    hide screen border_pos_circ
    scene black
    with diss_diag
    
    pause
    
    show text "Border morph with color change" as text1 with diss_diag:
        align(0.5, 0.15)
    
    pause
    
    show screen border_pos_morph(200, 200, 200, 200,  200, 200, 200, 200, transform_names=(color_base(cblue))) with diss_diag
    
    pause
    
    show screen border_pos_morph(200, 200, 200, 200,  400, 400, 400, 300, transform_names=(color_change(color_from=cblue, color_to=cred)))
    
    pause
    
    show screen border_pos_morph(400, 400, 400, 300,  800, 300, 500, 600, transform_names=(color_change(color_from=cred, color_to=cgreen)))
    
    pause
    
    show screen border_pos_morph(800, 300, 500, 600,  1500, 250, 300, 700, transform_names=(color_change(color_from=cgreen, color_to=cyellow)))
    
    pause
    
    hide screen border_pos_morph 
    scene black
    with diss_diag
    
    jump hub
    