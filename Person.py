screen _set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5

$ name = renpy.call_screen("set_name",title="이름 입력바람", init_name="이름입력해주세요")
$ na = Character(name, color = "#ffffff")
na "낯설지 않아 너의 오묘한 눈빛, 평행한 느낌"
