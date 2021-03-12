init:
    #Ressource Joueur
    $ bouffe = 0
    $ eau = 0
    $ argent = 0
    $ membre = 0

    #Portrait Joueur défini dans le label test_choix_clan
    $ portraitJoueur = ""

    #Ressource Clan adverse
    $ bouffeAdv = 25
    $ eauAdv = 35
    $ argentAdv = 44
    $ membreAdv = 29


    $ listScene = ["oui", "non", "peut-etre"]


screen choix_clan:
    imagebutton:
        xpos 140
        idle "image_clan_1"
        #hover "image_clan_1_hover"
        action SetVariable ("bouffe", 125), SetVariable ("eau", 100), SetVariable ("argent", 150), SetVariable ("membre", 33), SetVariable("portraitJoueur", "portrait_clan_1.png"), Jump("test_ecran_dialogue")


    imagebutton:
        xpos 140+333
        idle "image_clan_2"
        #hover "image_clan_1_hover"
        action SetVariable ("bouffe", 100), SetVariable ("eau", 100), SetVariable ("argent", 250), SetVariable ("membre", 27), SetVariable("portraitJoueur", "portrait_clan_2.png"), Jump("test_ecran_dialogue")


    imagebutton:
        xpos 140+666
        idle "image_clan_3"
        #hover "image_clan_1_hover"
        action SetVariable ("bouffe", 75), SetVariable ("eau", 100), SetVariable ("argent", 200), SetVariable ("membre", 40), SetVariable("portraitJoueur", "portrait_clan_3.png"), Jump("test_ecran_dialogue")


screen dialogue: #Ecran lors d'un dialogue
    add "frame_ressource": #background des ressources
        xpos 887

    hbox: #Ressources en haut à droite de l'écran
        xpos 887
        add "icone_ressource"

        text " [bouffe]" :
            size 20
            yalign 0.5

        add "icone_ressource"

        text " [eau] ":
            size 20
            yalign 0.5

        add "icone_ressource"

        text " [argent] ":
            size 20
            yalign 0.5

        add "icone_ressource"

        text " [membre] ":
            size 20
            yalign 0.5

    add portraitJoueur : #Portrait a gauche
        yalign 0.3

    add "textbox":  #Boite de dialogue au milieu
        xpos 264
        yalign 0.3

    add "ressource":    #FIX ressource a droite pour les nego (retirer pour juste les dialogue et le copié collé dans le screen des negociation quand il sera créer
        xpos 264+842
        yalign 0.3

    add "territoire_frame"  #Territoire en haut à gauche

    grid 2 3:   #Grille des logo de clan/pourcentage de territoire

        add "territoire":
            xpos 10
            ypos 10

        text " 29%":
            ypos 15

        add "territoire":
            xpos 10
            ypos 15

        text " 29%":
            ypos 20

        add "territoire":
            xpos 10
            ypos 19

        text " 29%":
            ypos 24

screen boutton_vole_bouffe:
    frame:
        xalign 0.1
        yalign 0.55
        textbutton "Voler":
            action SetVariable("bouffe", bouffe+bouffeAdv)

screen boutton_vole_eau:
    frame:
        xalign 0.1
        yalign 0.65
        textbutton "Voler":
            action SetVariable("eau", eau+eauAdv)

screen boutton_vole_argent:
    frame:
        xalign 0.1
        yalign 0.75
        textbutton "Voler":
            action SetVariable("argent", argent+argentAdv)

screen boutton_vole_territoire:
    frame:
        xalign 0.1
        yalign 0.85
        textbutton "Voler":
            action SetVariable("membre", membre+membreAdv)

#--------------------------------------------------------------------------------------------------------

label start:    

    jump test_choix_clan

    return

label test_choix_clan:  #Choix du clan en début de partie
    scene white_background

    show screen choix_clan

    "Test"

label test_ecran_dialogue:  #Placeholder de l'écran de dialogue
    hide screen choix_clan
    scene white_background

    show screen dialogue
    show screen boutton_vole_bouffe
    show screen boutton_vole_eau
    show screen boutton_vole_argent
    show screen boutton_vole_territoire

    menu:

        e "sdf sdgdfg dfgdf dfgdf fffgdf dfgffg dfgdf f fff gfd dfgfddfg dfg dffdfd dg dfgTest de text long de ses morts alors que je ne n'ai pas d'idée de texte et il est même pas si long que ça au final !"

        "OUI !":
            jump oui

        "NON !":
            jump non

        "PEUT-ÊTRE !":
            jump peut_etre

label oui:
    e "OUI"

label non:
    e "NON"

label peut_etre:
    e "PEUT-ÊTRE"


label test_random_jump:  #jump dans un label aléatoire présent dans la variable listScene

    $ randomNum = renpy.random.randint(0,2)
    jump expression listScene[randomNum]


label test_random_ressource:    #Ressource aléatoire quand on affronte un clan

    $ bouffeAdv = renpy.random.randint(membreAdv*2-10,membreAdv*2+10)
    "Ressource adverse : [bouffeAdv]"
    $ eauAdv = renpy.random.randint(0,100)
    "Ressource adverse : [eauAdv]"
    $ argentAdv = renpy.random.randint(membreAdv*2-10,membreAdv*2+10)
    "Ressource adverse : [argentAdv]"
    $ bouffeAdv = renpy.random.randint(membreAdv*2-10,membreAdv*2+10)
    "Ressource adverse : [bouffeAdv]"


    return
