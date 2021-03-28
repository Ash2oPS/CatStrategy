init -1 python:
    import math

init:
    #Ressource Joueur
    $ nourriture = 0 #Nombre de nourriture
    $ eau = 0        #Nombre d'eau
    $ eauMax = 100   #Nombre maximum d'eau pour le joueur
    $ argent = 0     #Nombre d'argent
    $ membre = 0     #Nombre de membre
    $ imageTerritoire = ""  #Icone de territoire du joueur
    $ joueurEchange = False #Si le joueur peut echanger ou non

    #Boost des bâtiment
    $ membreAttaque = 1 #Multiplicateur pour la force d'armé du clan
    $ boostRecolte = 1  #Multiplicateur pour la recolte de nourriture
    $ boostFiltre = 1   #Multiplicateur pour la récuperation d'eau
    $ boostArgent = 1   #Multiplicateur pour la récolte d'argent (0 avant d'avoir des bâtiments)

    #Portrait Joueur défini dans le label choix_clan
    $ portraitJoueur = ""

    #Ressource Clan adverse
    $ nourritureAdv = 0 #ressource uitlisé lors des combats contre clan
    $ eauAdv = 0
    $ argentAdv = 0

    $ membreClan1 = 0
    $ clan1Vivant = True
    $ imageTerritoire1 = ""

    $ membreClan2 = 0
    $ clan2Vivant = True
    $ imageTerritoire2 = ""

    #list des portraits de chat

    $ listChat = ["chat1a1","chat1a2","chat1a3","chat1a4","chat1a5","chat1a6","chat1a7","chat1a8","chat1a9","chat1a10","chat1a11","chat1a12","chat1a13","chat1a14","chat1a15","chat1a16","chat1a17","chat1a18","chat1a19","chat1a20","chat1a21","chat1a22","chat1b1","chat1b2","chat1b3","chat1b4","chat1b5","chat1b6","chat1b7","chat1b8","chat1b9","chat1b10","chat1b11","chat1b12","chat1b13","chat1b14","chat1b15","chat1b16","chat1b17","chat1b18","chat1b19","chat1b20", "chat1b21","chat1b22", "chat2a1","chat2a2","chat2a3","chat2a4","chat2a5","chat2a6","chat2a7","chat2a8","chat2a9","chat2a10","chat2a11","chat2a12","chat2a13","chat2a14","chat2a15","chat2a16","chat2a17","chat2a18","chat2a19","chat2a20","chat2a21","chat2a22","chat2b1","chat2b2","chat2b3","chat2b4","chat2b5","chat2b6","chat2b7","chat2b8","chat2b9","chat2b10","chat2b11","chat2b12","chat2b13","chat2b14","chat2b15","chat2b16","chat2b17","chat2b18","chat2b19","chat2b20", "chat2b21","chat2b22", "chat2b23"]

    $ chatParlant = listChat[88]    #Portrait du chat en train de parler

    #list des dialogues possible
    $ listScene = ["double_rats_chasse", "mariage_clan_adverse", "fils_bully", "maison_brule", "offre_rat", "proposition_mariage", "etoile_filante", "peur_chien", "fuite_silo", "rat_geant", "legende_humains", "pull_over", "chien_soutterain","dialogueE1", "dialogueE2", "dialogueE3", "dialogueE4", "dialogueE5", "dialogueE6", "dialogueE7", "dialogueE8", "dialogueE9", "dialogueE10", "dialogueE11", "dialogueE12", "dialogueE13", "dialogueE14", "dialogueE15", "dialogueE16", "dialogueE17"]

    $ listSceneUsed = [-1, -1, -1, -1, -1]  #Liste des indices des dialogues déjà utilisé le jour même et la veille

    $ dialogueOk = False    #Sert à vérifier si un dialogue est déjà passer aujourd'hui
    $ listPortrait = ["portrait_clan_1","portrait_clan_2","portrait_clan_3"]    #Liste des portrait de chef de clan
    $ choixClan = False #Deviens True quand le joueur à séléctionner un clan dans l'écran de choix de clan
    $ jour = 0
    $ dialogue = 0  #Nombre de dialogue dans une journée
    $ ressourceNegociation = ["Nourriture", "Eau", "Argent"]    #Liste des ressources pour en choisir aléatoirement pour les négociations
    $ ressourceDemanderNombre = 0   #Nombre de ressources qui sera demander au joueur pour les négociations
    $ ressourceProposerNombre = 0   #Nombre de ressources qui sera proposer au joueur pour les négociations
    $ clanAttaquant = ""    #Portrait du clan attaquant le joueur
    $ test = ""
    $ fondDialogue = "dialogue1"
    $ nombreChoix = "troisChoix.png"


define slowDissolve = Dissolve(1.5)

define fastDissolve = Dissolve(0.5)

define chat = Character("")

screen perdu:
    text "Perdu !":
        xalign 0.5
        yalign 0.5

screen gagne:
    text "Gagné !":
        xalign 0.5
        yalign 0.5

screen choix_clan:
    add "choix_clan"

    imagebutton:
        xpos 15
        ypos 72
        idle "choix_clan1"
        hover "choix_clan1_hover"
        action Jump("choix_clan_1")


    imagebutton:
        xpos 455
        ypos 73
        idle "choix_clan2"
        hover "choix_clan2_hover"
        action Jump("choix_clan_2")


    imagebutton:
        xpos 870
        ypos 66
        idle "choix_clan3"
        hover "choix_clan3_hover"
        action Jump("choix_clan_3")



screen dialogue: #Ecran lors d'un dialogue
    add "dialogue0"
    add chatParlant:
        xpos 120
        ypos 100

    add fondDialogue
    add "ressources"

    text " {color=#000000}[eau]{/color} ":
        size 20
        xanchor 0.5
        yanchor 0.5
        xpos 1124
        ypos 25

    text " {color=#000000}[nourriture]{/color}" :
        size 20
        xanchor 0.5
        yanchor 0.5
        xpos 1164
        ypos 65

    text " {color=#000000}[argent]{/color} ":
        size 20
        xanchor 0.5
        yanchor 0.5
        xpos 1204
        ypos 105


    add "territoire_background"  #Territoire des 3 clans en bas à gauche

    grid 2 3:   #Grille des logo de clan/pourcentage de territoire
        xpos 25
        ypos 540
        add imageTerritoire:
            xpos 10
            ypos 10

        text " [membre]":
            color "000000"
            ypos 10

        add imageTerritoire1:
            xpos 10
            ypos 30

        text " [membreClan1]":
            color "000000"
            ypos 30

        add imageTerritoire2:
            xpos 10
            ypos 50

        text " [membreClan2]":
            color "000000"
            ypos 50

screen combat:
    add "combat0"   #Background de combat

    add portraitJoueur: #Portrait du joueur
        xpos 125
        ypos 120

    add clanAttaquant: #Portrait du chef de clan adverse
        xpos 925
        ypos 120

    add "combat1"   #Frame des clans avec leurs ressources

    vbox:   #Ressource du joueur
        xpos 200
        ypos 390

        text "[eau]":
            ypos 8

        text "[nourriture]":
            ypos 35

        text "[argent]":
            ypos 70

        text "[membre]":
            ypos 110

    vbox:   #Ressource du clan adverse
        xpos 1055
        ypos 390

        text "[eauAdv]":
            ypos 8

        text "[nourritureAdv]":
            ypos 35

        text "[argentAdv]":
            ypos 70

        text "[membreClanAdverse]":
            ypos 110


screen boutton_vole: #Bouttons pour voler des ressources après un combat gagné

    imagebutton:
        xpos 900
        ypos 450
        idle "bouton_voler"
        hover "bouton_voler_hover"
        action SetVariable("nourriture", int(nourriture+nourritureAdv*0.33)), SetVariable("nourriture", int(nourritureAdv-nourritureAdv*0.33)), Jump("post_combat_gagner")

    imagebutton:
        xpos 900
        ypos 390
        idle "bouton_voler"
        hover "bouton_voler_hover"
        action SetVariable("eau", int(eau+eauAdv*0.33)), SetVariable("eau", int(eauAdv-eauAdv*0.33)), Jump("post_combat_gagner")

    imagebutton:
        xpos 900
        ypos 510
        idle "bouton_voler"
        hover "bouton_voler_hover"
        action SetVariable("argent", int(argent+argentAdv*0.33)), SetVariable("argentAdv", int(argentAdv-argentAdv*0.33)), Jump("post_combat_gagner")

    imagebutton:
        xpos 900
        ypos 570
        idle "bouton_voler"
        hover "bouton_voler_hover"
        action SetVariable("membre", (membre+int((5+float(membreClanAdverse*0.1))))), SetVariable("membreClanAdverse",membreClanAdverse-int((5+float(membreClanAdverse*0.1)))), Jump("post_combat_gagner")


#--------------------------------------------------------------------------------------------------------

label start:
    scene intro
    ""


label choix_clan:  #Choix du clan en début de partie
    scene fond
    with slowDissolve

    show screen choix_clan
    with slowDissolve

    ""

    jump choix_clan

label choix_clan_1:
    hide screen choix_clan
    with slowDissolve

    $ nourriture = 125
    $ eau = 80
    $ argent = 150
    $ membre = 33
    $ portraitJoueur = "portrait_clan_1"
    $ membreClan1 = 27
    $ membreClan2 = 40
    $ imageTerritoire = "clanb"
    $ imageTerritoire1 = "clanv"
    $ imageTerritoire2 = "clanr"
    $ listPortrait.pop(0)

    jump dialogue


label choix_clan_2:
    hide screen choix_clan
    with slowDissolve

    $ nourriture = 100
    $ eau = 80
    $ argent = 250
    $ membre = 27
    $ portraitJoueur = "portrait_clan_2"
    $ membreClan1 = 33
    $ membreClan2 = 40
    $ imageTerritoire = "clanv"
    $ imageTerritoire1 = "clanb"
    $ imageTerritoire2 = "clanr"
    $ listPortrait.pop(1)

    jump dialogue


label choix_clan_3:
    hide screen choix_clan
    with slowDissolve

    $ nourriture = 75
    $ eau = 80
    $ argent = 200
    $ membre = 40
    $ portraitJoueur = "portrait_clan_3"
    $ membreClan1 = 33
    $ membreClan2 = 27
    $ imageTerritoire = "clanr"
    $ imageTerritoire1 = "clanb"
    $ imageTerritoire2 = "clanv"
    $ listPortrait.pop(2)

    jump dialogue


label dialogue:
    $ fondDialogue = "dialogue1"
    $ chatParlant = "chat2b23"  #image du chat vide
    scene fond
    with slowDissolve

    show screen dialogue
    with dissolve

    $ jour += 1
    $ dialogue += 1 #Nombre de dialogue de la journée +1
    $ dialogueOk = False    #Dialogue aléatoire n'est pas déjà passé aujourd'hui

    if dialogue == 2:   #le deuxième dialogue
        jump explorateur

    if dialogue == 4:   #le quatrième dialogue
        jump chasseur

    if dialogue == 5:   #Après 4 dialogues aléatoire
        jump negociation    #Negociation aléatoire avec un clan adverse

    #image de chat aléatoire
    $ randomChat = renpy.random.randint(0, len(listChat)-2)
    $ chatParlant = listChat[randomChat]

    python:
        while not dialogueOk:
            dialogueOk = True
            sceneRandom = renpy.random.randint(0,len(listScene)-1) #Choix aléatoire du dialogue
            for i in listSceneUsed:
                if sceneRandom == i:    #On vérifie que le dialogue n'est pas déjà passé aujourd'hui
                    dialogueOk = False  #si c'est le cas on reste dans la boucle

    if jour == 0 and dialogue == 1: #Premier dialogue du premier jour
        $ listSceneUsed[0] = sceneRandom    #On met l'indice du dialogue dans la liste

    elif jour == 0 and dialogue == 3:   #Troisième dialogue du premier jour
        $ listSceneUsed[1] = sceneRandom


    elif jour > 0 and dialogue == 1:   #Différent pour les autres jour car on met a l'indice 2 et 3 du tableau et pas 0 et 1
        $ listSceneUsed[2] = sceneRandom

    else:
        $ listSceneUsed[3] = sceneRandom


    jump expression listScene[sceneRandom]

label explorateur:
    $ chatParlant = "chat1a8"
    $ filtre = renpy.random.randint(int((membre*0.7)*boostFiltre),int((membre*0.9)*boostFiltre)) #Avant le 2ème dialogue dialogues des chats reviennent avec de l'eau
    chat "Vos explorateurs sont revenu avec [filtre] d'eau. "
    $ eau += filtre
    if eau > eauMax:
        $ eau = eauMax
    jump dialogue

label chasseur:
    $ chatParlant = "chat1b8"
    $ chasse = renpy.random.randint(int((membre*0.6)*boostRecolte),int((membre*0.8)*boostRecolte))  #Avant le 4ème dialogue dialogues des chats reviennent avec de l'eau
    chat "Vos chasseurs sont revenu avec [chasse] de nourritures."
    $ nourriture += chasse

    jump dialogue

label negociation:  #Scene des negociation
    $ fondDialogue = "negociation"
    #Choix aleatoire du clan qui attaque
    if (clan1Vivant and clan2Vivant):
        $ randomAttaquant = renpy.random.randint(0,len(listPortrait)-1)
    else:
        $ randomAttaquant = 0

    $ clanAttaquant = listPortrait[randomAttaquant] #Portrait du chef de clan qui négocie/attaque
    $ chatParlant = listPortrait[randomAttaquant]

    $ ressourceProposerRand = renpy.random.randint(0,2) #Choisi aléatoirement quel ressource est proposer
    $ ressourceDemanderRand = ressourceProposerRand
    while ressourceDemanderRand==ressourceProposerRand: #Tant que la ressource demander est la même que celle proposer
        $ ressourceDemanderRand = renpy.random.randint(0,2) #Choisi quel ressource est demander aléatoirement
    $ ressourceDemanderNombre = renpy.random.randint(int(membre*1.1),int(membre*1.4))   #Choisi le nombre de ressource proposer aléatoirement
    $ ressourceProposerNombre = renpy.random.randint(int(membre*0.6),int(membre*0.8))   #Choisi le nombre de ressource demander aléatoirement
    $ ressourceProposer = ressourceNegociation[ressourceProposerRand]
    $ ressourceDemander = ressourceNegociation[ressourceDemanderRand]

    #Faire en sorte que le clan adverse ait plus de ressources que ce qu'il offrait au joueur
    if (ressourceProposerRand == 0):
        $ nourritureAdv = int(ressourceProposerNombre*1.25+50)

    elif (ressourceProposerRand == 1):
        $ eauAdv = int(ressourceProposerNombre+30)
        if eauAdv > 100:
            $ eauAdv = 100

    else:
        $ argentADv = int(ressourceProposerNombre*1.5+163)

    #Si le joueur n'a pas assez de ressource pour l'échange
    if (ressourceDemanderRand == 0 and ressourceDemanderNombre > nourriture or ressourceDemanderRand == 1 and ressourceDemanderNombre > eau or ressourceDemanderRand == 2 and ressourceDemanderNombre > argent):
        $ joueurEchange = False
    else:
        $ joueurEchange = True



        #Si c'est le clan "Bouffe"
        if listPortrait[randomAttaquant] == "portrait_clan_1":
            menu:
                chat "Bonsoir, monsieur le rival ! J’aimerais beaucoup que vous me donniez [ressourceDemanderNombre] [ressourceDemander] contre [ressourceProposerNombre] [ressourceProposer]. Qu’en dites-vous ?"

                "Accepter" if joueurEchange:

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
                        if eauMax > eau:
                            $ eau = eauMax

                    elif (ressourceProposerRand == 2):
                        $ argent += ressourceProposerNombre

                    chat "Ça c'est une bien belle affaire, merci collègue !"
                    jump nouveau_jour

                "Refuser":
                    $ combattre = renpy.random.randint(0,1) #Si le joueur refuse l'échange il a une chance sur deux de devoir se battre
                    if (combattre == 1):
                        chat "Bah, okay tant pis, peut-être la prochaine fois."
                        jump nouveau_jour

                    else:
                        chat "Meh, c’est pas la réponse que j’attendais, et je veux vous prendre ce que j’étais venu chercher !"
                        jump combat

                "Attaquer":
                    chat "Oh ? C’est hyper méchant ça ! Mais ok, battons-nous !"
                    jump combat

        #Si c'est clan "Riche"
        elif listPortrait[randomAttaquant] == "portrait_clan_2":
            menu:
                chat "Salutations, être inférieur. J’exige que nous procédions à un échange. Je veux [ressourceDemanderNombre] de votre [ressourceDemander] contre [ressourceProposerNombre] de mon [ressourceProposer]."

                "Accepter" if joueurEchange:

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
                        if eauMax > eau:
                            $ eau = eauMax

                    elif (ressourceProposerRand == 2):
                        $ argent += ressourceProposerNombre

                    chat "Bien sûr que vous acceptez !"
                    jump nouveau_jour

                "Refuser":
                    $ combattre = renpy.random.randint(0,1) #Si le joueur refuse l'échange il a une chance sur deux de devoir se battre
                    if (combattre == 1):
                        chat "Pardon ? Hm, je n’en avais pas spécialement besoin de toute façon."
                        jump nouveau_jour

                    else:
                        chat "Vous me faites bien rire, comme si vous aviez le choix !"
                        jump combat

                "Attaquer":
                    chat "Comme vous êtes rude ! Je vais vous enseigner la politesse, moi !"
                    jump combat

        #Si c'est le clan "Combat"
        else:
            menu:
                chat "Hé, vermine ! Donne-moi [ressourceDemanderNombre] [ressourceDemander] et je te donne [ressourceProposerNombre] [ressourceProposer]."

                "Accepter" if joueurEchange:

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
                        if eauMax > eau:
                            $ eau = eauMax

                    elif (ressourceProposerRand == 2):
                        $ argent += ressourceProposerNombre

                    chat "..."
                    jump nouveau_jour

                "Refuser":
                    $ combattre = renpy.random.randint(0,1) #Si le joueur refuse l'échange il a une chance sur deux de devoir se battre
                    if (combattre == 1):
                        chat "Pff. On se reverra."
                        jump nouveau_jour

                    else:
                        chat "Tu vas le regretter !"
                        jump combat

                "Attaquer":
                    chat "Je vais te réduire en bouillie, minable !"
                    jump combat


label combat:   #Ecran de combat

    if (randomAttaquant == 0 and clan1Vivant):
        $ membreClanAdverse = membreClan1

    else:
        $ membreClanAdverse = membreClan2


    #Ressource aléatoire du clan adverse
    $ nourritureAdv = renpy.random.randint(int(membreClanAdverse*1.8),int(membreClanAdverse*2.2))
    $ eauAdv = renpy.random.randint(25,100)
    $ argentAdv = renpy.random.randint(int(membreClanAdverse*3*0.7),int(membreClanAdverse*3*1.3))

    hide screen dialogue
    with dissolve
    show screen combat
    with fastDissolve

    ""

    $ randomOutcome = renpy.random.randint(0,100)   #Variable qui décidera qui gagne dans le combat
    if ((float(membre*membreAttaque)/(membre*membreAttaque+membreClanAdverse))*100 > randomOutcome):
        show screen gagne
        pause 1
        jump combat_gagner

    else:
        if (ressourceDemanderRand == 0):
            if nourriture < ressourceDemanderNombre:
                $ nourriture -= 0
            else:
                $ nourriture -= ressourceDemanderNombre
                $ nourritureAdv += ressourceDemanderNombre

        elif (ressourceDemanderRand == 1):
            if eau < ressourceDemanderNombre:
                $ eau = 0
            else:
                $ eau -= ressourceDemanderNombre
                $ eauAdv += ressourceDemanderNombre

        elif (ressourceDemanderRand == 2):
            if argent < ressourceDemanderNombre:
                $ argent = 0
            else:
                $ argent -= ressourceDemanderNombre
                $ argentAdv += ressourceDemanderNombre

        $ membreClan1 += int(math.ceil(0.5 *int(5+membre*0.1)))   #Les deux clans adverses se partage les membres qui partent
        $ membreClan2 += int(math.floor(0.5 *int(5+membre*0.1)))
        $ membre -= int(5+membre*0.1) #Le joueur perd les membres


        if membre < 0:  #Si le joueur n'a plus de membre il a perdu
            $ membreClan1 += membre
            $ membre = 0
            jump perdu


        show screen perdu
        pause 1
        jump nouveau_jour

label combat_gagner:    #Afficher les boutons pour voler les ressource si le combat est gagné

    show screen boutton_vole

    ""

    jump combat_gagner

label post_combat_gagner:
    if eau > eauMax:
        $ eau = eauMax

    $ membre = int(membre)  #les membre du joueur sont convertie en integ pour ne pas avoir de chiffre a virgule dans l'interface

    if randomAttaquant == 0 and clan1Vivant:    #Si le clan qui nous a attaqué est le clanAdverse 1
        $ membreClan1 = int(membreClanAdverse)  #Son nombre de membre deviens celui du clan qui nous a attaquer

    else:                       #Si le clan qui nous a attaqué est le clanAdverse 2
        $ membreClan2 = int(membreClanAdverse)

    if (membreClan1 <= 0 and clan1Vivant):    #Si le clan adverse 1 est en vie mais avec 0 membre
        $ clan1Vivant = False
        $ membre += membreClan1
        $ membreClan1 = 0
        $ listPortrait.pop(0)

    if (membreClan2 <= 0 and clan2Vivant):    #Si le clan adverse 2 est en vie mais avec 0 membre
        $ clan2Vivant = False
        $ membre += membreClan2
        $ membreClan2 = 0
        $ listPortrait.pop(len(listPortrait)-1)

    jump nouveau_jour

label nouveau_jour: #Changement de jour
    $ dialogue = 0  #Nombre de dialogue par jour reviens à 0
    hide screen perdu
    with slowDissolve
    hide screen gagne
    with slowDissolve
    hide screen boutton_vole
    hide screen dialogue
    with slowDissolve
    hide screen negociation
    with slowDissolve
    hide screen combat
    with slowDissolve
    scene nouveau_jour
    with slowDissolve

    if (not clan1Vivant and not clan2Vivant):
        jump gagner

    $ eau = int(eau)
    $ nourriture = int(nourriture)
    $ argent = int(argent)

    python:
        for i in range(2):
            listSceneUsed[i] = listSceneUsed[i+2]
            listSceneUsed[i+2] = 0

    $ nourriture -= membre/2    #Les membres du joueur mangent
    $ nourriturePerdu = membre/2

    if nourriture >= 0:  #Si le joueur a assez de nourriture
        "Vos membres se nourrissent et vous perdez [nourriturePerdu] nourriture."

    else:    #Si le joueur n'a pas assez de nourriture
        $ chanceMemberLeave= renpy.random.randint(0,100)    #Nombre aléatoire entre 0 et 100
        if (chanceMemberLeave < 33+(nourriture*6)*-1):     #Si le joueur perd des membre (33% + 3% par membre qui n'a pas mangé de provoqué la perte de membre pour le joueur si il n'a pas assez de nourriture)
            $ membreClan1 += int(math.ceil(0.5 *int(5+membre*0.1)))    #Les deux clans adverses se partage les membres qui partent
            $ membreClan2 += int(math.floor(0.5 * int(5+membre*0.1)))
            $ membrePerdu = int(5+membre*0.1)
            $ membre -= int(5+membre*0.1) #Le joueur perd les membres
            $ nourriture = 0    #Nourriture reviens à 0
            "[membrePerdu] de vos membres ont décidé de quitter votre clan car vous n'aviez plus de quoi les nourrirent."
        else:
            "Vous n'avez plus de nourritures, vos membres ne vont pas rester longtemps si ça continue comme ça."
            $ nourriture = 0


    if membre < 0:  #Si le joueur n'a plus de membre il a perdu
        $ membreClan1 += membre
        $ membre = 0
        jump perdu


    $ eau -= membre/2    #Les membres du joueur boivent

    if eau >= 0:  #Si le joueur a assez d'eau
        "Vos membres se désaltèrent et vous perdez [nourriturePerdu] eau."

    else:    #Si le joueur n'a pas assez de nourriture
        $ chanceMemberLeave = renpy.random.randint(0,100)    #Nombre aléatoire entre 0 et 100
        if (chanceMemberLeave < 33+(eau*6)*-1):     #Si le joueur perd des membre (33% + 3% par membre qui n'a pas mangé de provoqué la perte de membre pour le joueur si il n'a pas assez de nourriture)
            $ membreClan1 += int(math.ceil(0.5 *int(5+membre*0.1)))    #Les deux clans adverses se partage les membres qui partent
            $ membreClan2 += int(math.floor(0.5 * int(5+membre*0.1)))
            $ membrePerdu = int(5+membre*0.1)
            $ membre -= int(5+membre*0.1) #Le joueur perd les membres
            $ eau = 0    #Eau reviens à 0
            "[membrePerdu] de vos membres ont quitter votre clan en étant assoifés et sont parti dans les clans adverse."
        else:
            "Vous n'avez plus d'eau, si ça continue vous aller perdre des membres."
            $ eau = 0

    #Si le joueur a crée la ferme a argent
    if boostArgent > 0:
        $ argentRecup = membre/2*boostArgent
        $ argent += argentRecup
        "Votre ferme à Catnabis a été productive, vous récupérer [argentRecup]"


    if membre < 0:  #Si le joueur n'a plus de membre il a perdu
        jump perdu

    #Combat entre les deux clans adverses si ils sont tout les deux encore là
    if (clan1Vivant and clan2Vivant):
        $ randomOutcome = renpy.random.randint(0,100)
        if ((float(membreClan1)/(membreClan1+membreClan2))*100 <= randomOutcome):   #Clan1 gagne
            $ membreClan1 += int(math.floor(2+membreClan2*0.05))
            $ membreClan2 -= int(math.floor(2+membreClan2*0.05))

        else:   #Clan2 gagne
            $ membreClan1 -= int(math.floor(2+membreClan1*0.05))
            $ membreClan2 += int(math.floor(2+membreClan1*0.05))


    if (membreClan1 <= 0 and clan1Vivant):    #Si le clan adverse 1 est en vie mais avec 0 membre
        $ clan1Vivant = False
        $ membre += membreClan1
        $ membreClan1 = 0
        $ listPortrait.pop(0)

    if (membreClan2 <= 0 and clan2Vivant):    #Si le clan adverse 2 est en vie mais avec 0 membre
        $ clan2Vivant = False
        $ membre += membreClan2
        $ membreClan2 = 0
        $ listPortrait.pop(len(listPortrait)-1)

    if (membre+membreClan1+membreClan2 != 100):
        $ membre += 100 - (membre+membreClan1+membreClan2)
    jump dialogue

label perdu:

    "Vous n'avez plus de membre voulant se battre pour vous, vous finissez par rester seul dans une pièce vide, sombre et sans aucun bruit..."

    return

label gagner:

    "Tout les chats sont a vos ordres et plus personne ne questionne votre autorité"

    return
