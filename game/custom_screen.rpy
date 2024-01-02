
## Custom transforms specific to your use cases ######################################################################################################

transform rgb_change:
    ease_quad 2.0 matrixcolor TintMatrix(cblue)
    ease_quad 2.0 matrixcolor TintMatrix(cgreen)
    ease_quad 2.0 matrixcolor TintMatrix(cred)
    repeat

## Custom screens specific to your use cases #########################################################################################################

screen hub_choice():
    modal True
    zorder 2
    
    add "multibg"
    
    text "Choose a section":
        color cblue
        size size_h1
        align(0.5, 0.125)
    
    use border_align(0.2, 0.35, 540, 270, width=3, border_color="#fff", alpha=1.0)
    use border_align(0.8, 0.35, 540, 270, width=3, border_color="#fff", alpha=1.0)
    use border_align(0.2, 0.85, 540, 270, width=3, border_color="#fff", alpha=1.0)
    use border_align(0.8, 0.85, 540, 270, width=3, border_color="#fff", alpha=1.0)
    
    use rectangle_pos(1200, 370, 100, 100, alpha=0.25)
    use arrow_pos(1325, 420, 100)
    use rectangle_pos(1450, 370, 100, 100, alpha=1.0)
    
    use rectangle_pos(400, 730, 150, 50, color=cblue)
    use border_pos(400, 860, 150, 50, 5, border_color=cblue)
    use circle_pos(620, 730, 30, color=cgreen)
    use border_pos_circ(620, 850, 30, 5, border_color=cgreen)
    
    use arrow_sin
    
    text "?" at rgb_change:
        color "#fff"
        size 102
        align(0.28, 0.375)
    
    textbutton "1. Colors":
        align(0.255, 0.56)
        action Jump("label_color")
        
    textbutton "2. Transitions & Transform":
        align(0.795, 0.56)
        action Jump("label_transitions")
    
    textbutton "3. Basic Components":
        align(0.227, 0.96)
        action Jump("label_components")
    
    textbutton "4. Advanced Usage":
        align(0.76, 0.96)
        action Jump("label_other")

screen all_colors():
    hbox:
        align(0.5, 0.7)
        spacing 192
        
        vbox:
            spacing 32
            
            text "Blue (cblue)":
                color cblue
            text "Green (cgreen)":
                color cgreen
            text "Yellow (cyellow)":
                color cyellow
            text "Red (cred)":
                color cred
            text "Purple (cpurple)":
                color cpurple
                
        vbox:
            spacing 32
            text "Pink (cpink)":
                color cpink
            text "Brown (cbrown)":
                color cbrown
            text "Gray (cgray)":
                color cgray
            text "Light Blue (clblue)":
                color clblue
            text "Dark Blue (cdblue)":
                color cdblue

default angle_progress = 0.0
default sin_value = 0
screen arrow_sin():
    python:
        sin_value = sin(angle_progress)
        angle_progress += 1
        
        if angle_progress == 360:
            angle_progress = 0
    
    if sin_value > 0.0:
        use arrow_pos(1380, 820, int(120*sin_value))
    else:
        use arrow_pos(1380+int(120*sin_value), 820, int(120*-sin_value), angle=180)
    
    #text "[angle_progress] [sin_value]"
    
    timer timer_dur action renpy.restart_interaction repeat True
    