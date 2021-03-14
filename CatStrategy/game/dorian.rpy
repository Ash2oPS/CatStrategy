init:
    #Ressource Joueur
    $ nourriture = int(0)
    $ eau = int(0)
    $ argent = int(0)
    $ membre = int(0)

    #Portrait Joueur défini dans le label test_choix_clan
    $ portraitJoueur = ""

    #Ressource Clan adverse
    $ nourritureAdv = 25
    $ eauAdv = 35
    $ argentAdv = 44
    $ membreClan1 = int(40)
    $ membreClan2 = int(27)


    $ listScene = ["dialog1", "dialog2", "dialog3", "dialog4", "dialog5", "dialog6"] #Liste des différents dialogues
    $ listPortrait = ["portrait_clan_1","portrait_clan_2","portrait_clan_3"]    #Liste des portrait de chat
    $ choixClan = False #Choix du clan du joueur
    $ dialogue = 0  #Nombre de dialogue dans une journée
    $ ressourceNegociation = ["nourriture", "Eau", "Argent"]    #Liste des ressources pour en choisir aléatoirement pour les négociations
    $ ressourceDemanderNombre = 0   #Nombre de ressources qui sera demander au joueur pour les négociations
    $ ressourceProposerNombre = 0   #Nombre de ressources qui sera proposer au joueur pour les négociations
    $ clanAttaquant = ""    #Portrait du clan attaquant le joueur



screen choix_clan: #À FIX le selected_idle fait n'imp
    imagebutton:
        xpos 140
        idle "image_clan_1"
        hover "image_clan_1_hover"
        selected_idle "image_clan_1_hover"
        action SetVariable ("nourriture", 3), SetVariable ("eau", 100), SetVariable ("argent", 150), SetVariable ("membre", 33), SetVariable("portraitJoueur", "portrait_clan_1"), SetVariable("membreClan1", 40), SetVariable("membreClan2", 27), SetVariable("choixClan", True)


    imagebutton:
        xpos 473
        idle "image_clan_2"
        hover "image_clan_2_hover"
        selected_idle "image_clan_2_hover"
        action SetVariable ("nourriture", 100), SetVariable ("eau", 100), SetVariable ("argent", 250), SetVariable ("membre", 27), SetVariable("portraitJoueur", "portrait_clan_2"), SetVariable("membreClan1", 40), SetVariable("membreClan2", 33), SetVariable("choixClan", True)


    imagebutton:
        xpos 806
        idle "image_clan_3"
        hover "image_clan_3_hover"
        selected_idle "image_clan_3_hover"
        action SetVariable ("nourriture", 75), SetVariable ("eau", 100), SetVariable ("argent", 200), SetVariable ("membre", 40), SetVariable("portraitJoueur", "portrait_clan_3"), SetVariable("membreClan1", 33), SetVariable("membreClan2", 27), SetVariable("choixClan", True)
    frame:
        xalign 0.5
        yalign 0.8

        textbutton "Choisir":
            if choixClan:
                action Jump("test_ecran_dialogue")


screen dialogue: #Ecran lors d'un dialogue
    add "frame_ressource": #Image du cadre des ressources
        xpos 887

    hbox: #Disposition des ressources en haut à droite de l'écran (change la hbox pour ne pas avoir de texte pour éviter que les icones bougent
        xpos 887
        add "icone_ressource"

        text " [nourriture]" :
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

    add portraitJoueur: #Portrait du chat qui parle au milieu à gauche
        yalign 0.3

    add "textbox":  #Boite de dialogue au milieu
        xpos 264
        yalign 0.3

    add "territoire_frame"  #Territoire en haut à gauche

    grid 2 3:   #Grille des logo de clan/pourcentage de territoire

        add "territoire":
            xpos 10
            ypos 10

        text " [membre]%":
            color "000000"
            ypos 15

        add "territoire":
            xpos 10
            ypos 15

        text " [membreClan1]%":
            color "000000"
            ypos 20

        add "territoire":
            xpos 10
            ypos 19

        text " [membreClan2]%":
            color "000000"
            ypos 24

screen negociation: #En plus de l'écran de dialogue lors d'une negociation avec un clan adverse

    add "ressource":    #Ressource a droite
        xpos 264+842
        yalign 0.3

screen combat:
    add portraitJoueur: #Portrait du joueur
        xpos 0
        ypos 100

    add "background_combat":    #Background des ressource du Joueur
        xpos 244
        ypos 100

    add "background_combat":    #Background des ressource du clan adverse
        xpos 244+396
        ypos 100

    add clanAttaquant: #Portrait du chef de clan adverse
        xpos 244+396+396
        ypos 100

    vbox:   #Icone des ressource du Joueur
        xpos 244+25
        ypos 150

        add "icone_ressource"

        add "icone_ressource":
            ypos 50

        add "icone_ressource":
            ypos 100

        add "icone_ressource":
            ypos 150

    vbox:   #Ressource du joueur
        xpos 244+25+75
        ypos 150

        text "[nourriture]":
            ypos 8

        text "[eau]":
            ypos 50+24

        text "[argent]":
            ypos 100+40

        text "[membre]":
            ypos 150+53

    vbox:   #Icone des ressource du clan adverse
        xpos 244+396+321
        ypos 150

        add "icone_ressource"

        add "icone_ressource":
            ypos 50

        add "icone_ressource":
            ypos 100

        add "icone_ressource":
            ypos 150

    vbox:   #Ressource du clan adverse
        xpos 244+396+321-50
        ypos 150

        text "[nourritureAdv]":
            ypos 8

        text "[eauAdv]":
            ypos 74

        text "[argentAdv]":
            ypos 140

        text "[membreClan1]":
            ypos 203

screen boutton_vole_nourriture: #Boutton pour voler de la nourriture après un combat gagné
    frame:
        xpos 244+396+75
        ypos 158
        textbutton "Voler":
            action SetVariable("nourriture", int(nourriture+nourritureAdv*0.33)), Jump("nouveau_jour")

screen boutton_vole_eau:    #Boutton pour voler de l'eau après un combat gagné
    frame:
        xpos 244+396+75
        ypos 224
        textbutton "Voler":
            action SetVariable("eau", int(eau+eauAdv*0.33)), Jump("nouveau_jour")

screen boutton_vole_argent: #Boutton pour voler de l'argent après un combat gagné
    frame:
        xpos 244+396+75
        ypos 290
        textbutton "Voler":
            action SetVariable("argent", int(argent+argentAdv*0.33)), Jump("nouveau_jour")

screen boutton_vole_territoire: #Boutton pour voler des membres/territoires après un combat gagné
    frame:
        xpos 244+396+75
        ypos 353
        textbutton "Voler":
            action SetVariable("membre", membre+(5+int(membreClan1*0.1))), SetVariable("membreClan1",membreClan1-(5+int(membreClan1*0.1))), Jump("nouveau_jour")

#--------------------------------------------------------------------------------------------------------

label start:

    jump test_choix_clan

    return

label test_choix_clan:  #Choix du clan en début de partie
    scene white_background

    show screen choix_clan

    ""

    jump test_choix_clan

label test_ecran_dialogue:  #Placeholder de l'écran de dialogue
    hide screen choix_clan
    scene white_background
    show screen dialogue

    $ dialogue +=1

    if dialogue == 5:
        jump negociation

    $ sceneRandom = renpy.random.randint(0,len(listScene)-1) #Jump dans un label aléatoire présent dans la variable listScene
    jump expression listScene[sceneRandom]

label negociation:  #Scene des negociation

    $ clanAttaquant = portraitJoueur    #Choix aleatoire du clan qui attaque
    while clanAttaquant == portraitJoueur:
        $randomAttaquant = renpy.random.randint(0,2)
        $clanAttaquant = listPortrait[randomAttaquant]

    scene white_background
    show screen negociation #Affiche l'écran des negociations

    $ ressourceProposerRand = renpy.random.randint(0,2) #Choisi quel ressource est proposer aléatoirement
    $ ressourceDemanderRand = ressourceProposerRand
    while ressourceDemanderRand==ressourceProposerRand: #Tant que la ressource demander est la même que celle proposer
        $ ressourceDemanderRand = renpy.random.randint(0,2) #Choisi quel ressource est demander aléatoirement
    $ ressourceDemanderNombre = renpy.random.randint(int(membre*1.1),int(membre*1.4))   #Choisi le nombre de ressource proposer aléatoirement
    $ ressourceProposerNombre = renpy.random.randint(int(membre*0.6),int(membre*0.8))   #Choisi le nombre de ressource demander aléatoirement
    $ ressourceProposer = ressourceNegociation[ressourceProposerRand]
    $ ressourceDemander = ressourceNegociation[ressourceDemanderRand]
    "On echange [ressourceProposerNombre] [ressourceProposer] contre [ressourceDemanderNombre] [ressourceDemander]"

    #Si le joueur n'a pas assez de ressource pour l'échange

    if (ressourceDemanderRand == 0 and ressourceDemanderNombre > nourriture or ressourceDemanderRand == 1 and ressourceDemanderNombre > eau or ressourceDemanderRand == 2 and ressourceDemanderNombre > argent):

        menu:
            "On echange [ressourceProposerNombre] [ressourceProposer] contre [ressourceDemanderNombre] [ressourceDemander]"
            "Non":
                jump nouveau_jour

            "Combattre":
                jump combat

    else :  #Si le joueur a assez de ressource
        menu:
            "On echange [ressourceProposerNombre] [ressourceProposer] contre [ressourceDemanderNombre] [ressourceDemander]"

            "Oui":  #Si le joueur accepte l'échange on retire les ressource demander au joueur et ajoute celle proposer
                if (ressourceDemanderRand == 0):
                    $ nourriture -= ressourceDemanderNombre

                elif (ressourceDemanderRand == 1):
                    $ eau -= ressourceDemanderNombre

                elif (ressourceDemanderRand == 2):
                    $ argent -= ressourceDemanderNombre

                if (ressourceProposerRand == 0):
                    $ nourriture += ressourceProposerNombre

                elif (ressourceProposerRand == 1):
                    $ eau += ressourceProposerNombre

                elif (ressourceProposerRand == 2):
                    $ argent += ressourceProposerNombre


                jump nouveau_jour


            "Non":
                $ combattre = renpy.random.randint(0,1) #Si le joueur refuse l'échange il a une chance sur deux de devoir se battre

                if (combattre == 1):
                    jump nouveau_jour

                else:
                    jump combat

            "Combattre":
                jump combat


label dialog1:
    e "1"
    jump test_ecran_dialogue

label dialog2:
    e "2"
    jump test_ecran_dialogue

label dialog3:
    e "3"
    jump test_ecran_dialogue

label dialog4:
    e "4"
    jump test_ecran_dialogue

label dialog5:
    e "5"
    jump test_ecran_dialogue

label dialog6:
    e "6"
    jump test_ecran_dialogue

label combat:   #Ecran de combat

    #Ressource aléatoire du clan adverse
    $ nourritureAdv = renpy.random.randint(membreClan1*2-10,membreClan1*2+10)
    $ eauAdv = renpy.random.randint(0,100)
    $ argentAdv = renpy.random.randint(int(membreClan1*3*0.7),int(membreClan1*3*1.3))

    scene white_background
    hide screen dialogue
    hide screen negociation
    show screen combat

    ""

    jump combat_gagner

label combat_gagner:    #Afficher les boutons pour voler les ressource si le combat est gagné

    show screen boutton_vole_nourriture
    show screen boutton_vole_eau
    show screen boutton_vole_argent
    show screen boutton_vole_territoire
    ""

    jump combat_gagner


label nouveau_jour: #Changement de jour
    $ dialogue = 0  #Nombre de dialogue par jour reviens à 0
    hide screen boutton_vole_nourriture
    hide screen boutton_vole_eau
    hide screen boutton_vole_argent
    hide screen boutton_vole_territoire
    hide screen dialogue
    hide screen negociation
    hide screen combat
    "{color=#000000}Un nouveau jour commence{/color}"
    $ nourriture -= membre/2    #Les membres du joueur mangent
    if (nourriture < 0):    #Si le joueur n'a pas assez de nourriture
        $ chanceMemberLeave= renpy.random.randint(0,100)    #nombre aléatoire entre 0 et 100
        if (chanceMemberLeave < (nourriture*8)*-1):     #Si le nombre aleatoire est inférieur à la nourriture manquante *8 des membres partent
            $ membreClan1 += int(0.5 *int(5+membre*0.1))
            $ membreClan2 += int(0.5 * int(5+membre*0.1))
            if (int(5+(membre*0.1))%2 > 0):   #Si le nombres de membre qui part est impaire, un membre est perdu dans les arrondis
                $ membreClan1 +=1   #On le rajoute arbitrairement au premier clan adverse
            $ membre -= int(5+membre*0.1) #Le joueur perd les membres qui partent
            $ nourriture = 0    #Nourriture reviens à 0

        else:
            $ nourriture = 0


    jump test_ecran_dialogue
