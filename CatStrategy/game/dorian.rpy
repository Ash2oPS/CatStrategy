init:
    #Ressource Joueur
    $ nourriture = 0 #Nombre de nourriture
    $ eau = 0        #Nombre d'eau
    $ argent = 0     #Nombre d'argent
    $ membre = 0     #Nombre de membre

    #Boost des bâtiment
    $ membreAttaque = 1 #Multiplicateur pour la force d'armé du clan
    $ boostRecolte = 1  #Multiplicateur pour la recolte de nourriture
    $ boostFiltre = 1   #Multiplicateur pour la récuperation d'eau
    $ boostArgent = 0   #Multiplicateur pour la récolte d'argent (0 avant d'avoir des bâtiments)

    #Portrait Joueur défini dans le label choix_clan
    $ portraitJoueur = ""

    #Ressource Clan adverse
    $ nourritureAdv = 25
    $ eauAdv = 35
    $ argentAdv = 44
    $ membreClan1 = 0
    $ membreClan2 = 0

    #list des portraits de chat

    $ listChat = ["chat1a1","chat1a2","chat1a3","chat1a4","chat1a5","chat1a6","chat1a7","chat1a8","chat1a9","chat1a10","chat1a11","chat1a12","chat1a13","chat1a14","chat1a15","chat1a16","chat1a17","chat1a18","chat1a19","chat1a20","chat1a21","chat1a22","chat1b1","chat1b2","chat1b3","chat1b4","chat1b5","chat1b6","chat1b7","chat1b8","chat1b9","chat1b10","chat1b11","chat1b12","chat1b13","chat1b14","chat1b15","chat1b16","chat1b17","chat1b18","chat1b19","chat1b20", "chat1b21","chat1b22", "chat2a1","chat2a2","chat2a3","chat2a4","chat2a5","chat2a6","chat2a7","chat2a8","chat2a9","chat2a10","chat2a11","chat2a12","chat2a13","chat2a14","chat2a15","chat2a16","chat2a17","chat2a18","chat2a19","chat2a20","chat2a21","chat2a22","chat2b1","chat2b2","chat2b3","chat2b4","chat2b5","chat2b6","chat2b7","chat2b8","chat2b9","chat2b10","chat2b11","chat2b12","chat2b13","chat2b14","chat2b15","chat2b16","chat2b17","chat2b18","chat2b19","chat2b20", "chat2b21","chat2b22"]
    $ chatParlant = listChat[65]    #Portrait du chat en train de parler

    $ listScene = ["dialog0", "dialog1", "dialog2", "dialog3", "dialog4", "dialog5", "dialog6"] #Liste des différents dialogues
    $ listSceneUsed = [10, 10, 10, 10, 10]
    $ dialogueOk = False    #Sert à vérifier si un dialogue est déjà passer aujourd'hui
    $ listPortrait = ["portrait_clan_1","portrait_clan_2","portrait_clan_3"]    #Liste des portrait de chef de clan
    $ choixClan = False #Deviens True quand le joueur à séléctionner un clan dans l'écran de choix de clan
    $ jour = 0
    $ dialogue = 0  #Nombre de dialogue dans une journée
    $ ressourceNegociation = ["nourriture", "Eau", "Argent"]    #Liste des ressources pour en choisir aléatoirement pour les négociations
    $ ressourceDemanderNombre = 0   #Nombre de ressources qui sera demander au joueur pour les négociations
    $ ressourceProposerNombre = 0   #Nombre de ressources qui sera proposer au joueur pour les négociations
    $ clanAttaquant = ""    #Portrait du clan attaquant le joueur
    $ test = ""
define slowDissolve = Dissolve(1.5)

screen choix_clan: #A FIX le selected_idle fait n'imp
    imagebutton:
        xpos 140
        idle "image_clan_1"
        hover "image_clan_1_hover"
        selected_idle "image_clan_1_hover"
        action SetVariable ("nourriture", 125), SetVariable ("eau", 80), SetVariable ("argent", 150), SetVariable ("membre", 33), SetVariable("portraitJoueur", "portrait_clan_1"), SetVariable("membreClan1", 40), SetVariable("membreClan2", 27), SetVariable("choixClan", True)


    imagebutton:
        xpos 473
        idle "image_clan_2"
        hover "image_clan_2_hover"
        selected_idle "image_clan_2_hover"
        action SetVariable ("nourriture", 100), SetVariable ("eau", 80), SetVariable ("argent", 250), SetVariable ("membre", 27), SetVariable("portraitJoueur", "portrait_clan_2"), SetVariable("membreClan1", 40), SetVariable("membreClan2", 33), SetVariable("choixClan", True)


    imagebutton:
        xpos 806
        idle "image_clan_3"
        hover "image_clan_3_hover"
        selected_idle "image_clan_3_hover"
        action SetVariable ("nourriture", 75), SetVariable ("eau", 80), SetVariable ("argent", 200), SetVariable ("membre", 40), SetVariable("portraitJoueur", "portrait_clan_3"), SetVariable("membreClan1", 33), SetVariable("membreClan2", 27), SetVariable("choixClan", True)
    frame:
        xalign 0.5
        yalign 0.8

        textbutton "Choisir":
            if choixClan:
                action Jump("delete_player_portrait_list")


screen dialogue: #Ecran lors d'un dialogue
    add "dialogue0"
    add chatParlant:
        xpos 120
        ypos 100

    add "dialogue1"
    add "dialogue2"
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

        text "[membreClanAdverse]":
            ypos 203

screen boutton_vole_nourriture: #Boutton pour voler de la nourriture après un combat gagné
    frame:
        xpos 244+396+75
        ypos 150
        textbutton "Voler":
            action SetVariable("nourriture", int(nourriture+nourritureAdv*0.33)), Jump("post_combat_gagner")

screen boutton_vole_eau:    #Boutton pour voler de l'eau après un combat gagné
    frame:
        xpos 244+396+75
        ypos 242
        textbutton "Voler":
            action SetVariable("eau", int(eau+eauAdv*0.33)), Jump("post_combat_gagner")

screen boutton_vole_argent: #Boutton pour voler de l'argent après un combat gagné
    frame:
        xpos 244+396+75
        ypos 334
        textbutton "Voler":
            action SetVariable("argent", int(argent+argentAdv*0.33)), Jump("post_combat_gagner")

screen boutton_vole_territoire: #Boutton pour voler des membres/territoires après un combat gagné
    frame:
        xpos 244+396+75
        ypos 426
        textbutton "Voler":
            action SetVariable("membre", (membre+(5+float(membreClanAdverse*0.1)))), SetVariable("membreClanAdverse",membreClanAdverse-(5+float(membreClanAdverse*0.1))), Jump("post_combat_gagner")

#--------------------------------------------------------------------------------------------------------

label start:

    jump choix_clan

    return

label choix_clan:  #Choix du clan en début de partie
    scene fond

    show screen choix_clan

    ""

    jump choix_clan

label delete_player_portrait_list:
    if (portraitJoueur == 'portrait_clan_1'):
        $ listPortrait.pop(0)
    elif (portraitJoueur == 'portrait_clan_2'):
        $ listPortrait.pop(1)
    else:
        $ listPortrait.pop(2)


label dialogue:  #Placeholder de l'écran de dialogue
    hide screen choix_clan

    show screen dialogue
    $ jour += 1
    $ dialogue +=1
    $ dialogueOk = False

    if dialogue == 2:
        $ filtre = renpy.random.randint(int((membre*0.25)*boostFiltre),int((membre*0.4)*boostFiltre)) #Avant le 2ème dialogue dialogues des chats reviennent avec de l'eau
        "Vos explorateurs sont revenu avec [filtre] d'eau."
        $ eau += filtre
    if dialogue == 4:
        $ chasse = renpy.random.randint(int((membre*0.20)*boostRecolte),int((membre*0.35)*boostRecolte))  #Avant le 4ème dialogue dialogues des chats reviennent avec de l'eau
        "Vos chasseurs sont revenu avec [chasse] de nourritures."
        $ nourriture += chasse

    if dialogue == 5:   #Après 4 dialogues aléatoire
        jump negociation    #Negociation aléatoire avec un clan adverse

    python:
        while not dialogueOk:
            dialogueOk = True
            sceneRandom = renpy.random.randint(0,len(listScene)-1) #Choix aléatoire du dialogue
            for i in listSceneUsed:
                if sceneRandom == i:    #On vérifie que le dialogue n'est pas déjà passé aujourd'hui
                    dialogueOk = False  #si c'est le cas on reste dans la boucle

    $ listSceneUsed[dialogue-1] = sceneRandom   #On met l'indice du dialogue dans une autre liste
    "[listSceneUsed[0]] | [listSceneUsed[1]] | [listSceneUsed[2]] | [listSceneUsed[3]] | [listSceneUsed[4]] "
    jump expression listScene[sceneRandom]

label negociation:  #Scene des negociation
    #Choix aleatoire du clan qui attaque
    $ randomAttaquant = renpy.random.randint(0,1)
    $ clanAttaquant = listPortrait[randomAttaquant] #Portrait du chef de clan qui attaque
    $ chatParlant = listPortrait[randomAttaquant]

    $ ressourceProposerRand = renpy.random.randint(0,2) #Choisi quel ressource est proposer aléatoirement
    $ ressourceDemanderRand = ressourceProposerRand
    while ressourceDemanderRand==ressourceProposerRand: #Tant que la ressource demander est la même que celle proposer
        $ ressourceDemanderRand = renpy.random.randint(0,2) #Choisi quel ressource est demander aléatoirement
    $ ressourceDemanderNombre = renpy.random.randint(int(membre*1.1),int(membre*1.4))   #Choisi le nombre de ressource proposer aléatoirement
    $ ressourceProposerNombre = renpy.random.randint(int(membre*0.6),int(membre*0.8))   #Choisi le nombre de ressource demander aléatoirement
    $ ressourceProposer = ressourceNegociation[ressourceProposerRand]
    $ ressourceDemander = ressourceNegociation[ressourceDemanderRand]

    #Ressource aléatoire du clan adverse
    $ nourritureAdv = renpy.random.randint(int(membreClan1*2-10),int(membreClan1*2+10))
    $ eauAdv = renpy.random.randint(25,100)
    $ argentAdv = renpy.random.randint(int(membreClan1*3*0.7),int(membreClan1*3*1.3))

    #Faire en sorte que le clan adverse à plus de ressources que ce qu'il offrait au joueur
    if (ressourceProposerRand == 0):
        $ nourritureAdv = int(ressourceProposerNombre*1.25+93)

    elif (ressourceProposerRand == 1):
        $ eauAdv = int(ressourceProposerNombre+75)
        if eauAdv > 100:
            $ eauAdv = 100

    else:
        $ argentADv = int(ressourceProposerNombre*1.5+163)



    "On vous donne [ressourceProposerNombre] [ressourceProposer] contre [ressourceDemanderNombre] [ressourceDemander]"

    #Si le joueur n'a pas assez de ressource pour l'échange

    if (ressourceDemanderRand == 0 and ressourceDemanderNombre > nourriture or ressourceDemanderRand == 1 and ressourceDemanderNombre > eau or ressourceDemanderRand == 2 and ressourceDemanderNombre > argent):

        menu:
            "On vous donne [ressourceProposerNombre] [ressourceProposer] contre [ressourceDemanderNombre] [ressourceDemander]"
            "Refuser":
                $ combattre = renpy.random.randint(0,1) #Si le joueur refuse l'échange il a une chance sur deux de devoir se battre
                if (combattre == 1):
                    jump nouveau_jour

                else:
                    jump combat

            "Attaquer":
                jump combat

    else :  #Si le joueur a assez de ressource
        menu:
            "On vous donne [ressourceProposerNombre] [ressourceProposer] contre [ressourceDemanderNombre] [ressourceDemander]"

            "Accepter":  #Si le joueur accepte l'échange on retire les ressource demander au joueur et ajoute celle proposer
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


            "Refuser":
                $ combattre = renpy.random.randint(0,1) #Si le joueur refuse l'échange il a une chance sur deux de devoir se battre

                if (combattre == 1):
                    jump nouveau_jour

                else:
                    jump combat

            "Attaquer":
                jump combat

label dialog0:
    "0"
    jump dialogue

label dialog1:
    "1"
    jump dialogue

label dialog2:
    "2"
    jump dialogue

label dialog3:
    "3"
    jump dialogue

label dialog4:
    "4"
    jump dialogue

label dialog5:
    "5"
    jump dialogue

label dialog6:
    "6"
    jump dialogue

label combat:   #Ecran de combat

    if randomAttaquant == 0:
        $ membreClanAdverse = membreClan1

    else:
        $ membreClanAdverse = membreClan2


    hide screen dialogue
    show screen combat

    ""

    $ randomOutcome = renpy.random.randint(0,100)   #Variable qui décidera qui gagne dans le combat
    if ((float(membre*membreAttaque)/(membre*membreAttaque+membreClanAdverse))*100 > randomOutcome):
        "Vous avez gagné !"
        jump combat_gagner

    else:
        if (ressourceDemanderRand == 0):
            $ nourriture -= int(20+nourriture*0.25)

        elif (ressourceDemanderRand == 1):
            $ eau -= int(15+eau*0.25)

        elif (ressourceDemanderRand == 2):
            $ argent -= int(30+argent*0.25)


        $ membreClan1 += int(0.5 *int(5+membre*0.1))    #Les deux clans adverses se partage les membres qui partent
        $ membreClan2 += int(0.5 * int(5+membre*0.1))
        $ membre -= int(5+membre*0.1) #Le joueur perd les membres

        if (membre + membreClan1 + membreClan2)%2 == 1: #Si le total des membre est impaire (un membre s'est perdu dans les pourcentage) on le donne arbitrairement au clan adverse 1
            $ membreClan1 +=1

        if membre < 0:  #Si le joueur n'a plus de membre il a perdu
            $ membreClan1 += membre
            $ membre = 0
            jump perdu


        "Vous avez perdu !"
        jump nouveau_jour

label combat_gagner:    #Afficher les boutons pour voler les ressource si le combat est gagné

    show screen boutton_vole_nourriture
    show screen boutton_vole_eau
    show screen boutton_vole_argent
    show screen boutton_vole_territoire
    ""

    jump combat_gagner

label post_combat_gagner:
    $ membre = int(membre)  #les membre du joueur sont convertie en integer pour ne pas avoir de chiffre a virgule dans l'interface


    if randomAttaquant == 0:    #Si le clan qui nous a attaqué est le clanAdverse 1
        $ membreClan1 = int(membreClanAdverse)  #Son nombre de membre deviens celui du clan qui nous a attaquer

    else:                       #Si le clan qui nous a attaqué est le clanAdverse 2
        $ membreClan2 = int(membreClanAdverse)

    if (membre + membreClan1 + membreClan2)%2 ==1:
        $ membre +=1    #Si le total des membre est impaire (un membre s'est perdu dans les pourcentage) on le donne arbitrairement au joueur

    jump nouveau_jour

label nouveau_jour: #Changement de jour
    $ dialogue = 0  #Nombre de dialogue par jour reviens à 0
    hide screen boutton_vole_nourriture #cache tous les autres screen
    hide screen boutton_vole_eau
    hide screen boutton_vole_argent
    hide screen boutton_vole_territoire
    hide screen dialogue
    hide screen negociation
    hide screen combat
    scene nouveau_jour
    with slowDissolve
    "{color=#000000}Un nouveau jour commence{/color}"

    $ nourriture -= membre/2    #Les membres du joueur mangent
    $ nourriturePerdu = membre/2

    if nourriture >= 0:  #Si le joueur a assez de nourriture
        "Vos membres se nourrissent et vous perdez [nourriturePerdu] nourriture."

    else:    #Si le joueur n'a pas assez de nourriture
        $ chanceMemberLeave= renpy.random.randint(0,100)    #Nombre aléatoire entre 0 et 100
        if (chanceMemberLeave < 33+(nourriture*6)*-1):     #Si le joueur perd des membre (33% + 3% par membre qui n'a pas mangé de provoqué la perte de membre pour le joueur si il n'a pas assez de nourriture)
            $ membreClan1 += int(0.5 *int(5+membre*0.1))    #Les deux clans adverses se partage les membres qui partent
            $ membreClan2 += int(0.5 * int(5+membre*0.1))
            $ membrePerdu = int(5+membre*0.1)
            $ membre -= int(5+membre*0.1) #Le joueur perd les membres
            $ nourriture = 0    #Nourriture reviens à 0
            "[membrePerdu] de vos membres ont décidé de quitter votre clan car vous n'aviez plus de quoi les nourrirent."
        else:
            "Vous n'avez plus de nourritures, vos membres ne vont pas rester longtemps si ça continue comme ça."
            $ nourriture = 0

    if (membre + membreClan1 + membreClan2)%2 == 1: #Si le total des membre est impaire (un membre s'est perdu dans les pourcentage) on le donne arbitrairement au clan adverse 1
        $ membreClan1 +=1

    if membre < 0:  #Si le joueur n'a plus de membre il a perdu
        $ membreClan1 += membre
        $ membre = 0
        jump perdu


    $ eau -= membre/2    #Les membres du joueur boivent

    if eau >= 0:  #Si le joueur a assez d'eau
        "Vos membres se désaltèrent et vous perdez [nourriturePerdu] eau."

    else:    #Si le joueur n'a pas assez de nourriture
        $ chanceMemberLeave= renpy.random.randint(0,100)    #Nombre aléatoire entre 0 et 100
        if (chanceMemberLeave < 33+(eau*6)*-1):     #Si le joueur perd des membre (33% + 3% par membre qui n'a pas mangé de provoqué la perte de membre pour le joueur si il n'a pas assez de nourriture)
            $ membreClan1 += int(0.5 *int(5+membre*0.1))    #Les deux clans adverses se partage les membres qui partent
            $ membreClan2 += int(0.5 * int(5+membre*0.1))
            $ membrePerdu = int(5+membre*0.1)
            $ membre -= int(5+membre*0.1) #Le joueur perd les membres
            $ eau = 0    #Eau reviens à 0
            "[membrePerdu] de vos membres ont quitter votre clan en étant assoifés et sont parti dans les clans adverse."
        else:
            "Vous n'avez plus d'eau, si ça continue vous aller perdre des membres."
            $ eau = 0

    if membre < 0:  #Si le joueur n'a plus de membre il a perdu
        $ membreClan1 += membre
        $ membre = 0
        jump perdu

    if (membre + membreClan1 + membreClan2)%2 == 1: #Si le total des membre est impaire (un membre s'est perdu dans les pourcentage) on le donne arbitrairement au clan adverse 1
        $ membreClan1 +=1

    #Combat entre les deux clans adverses
    $ randomOutcome = renpy.random.randint(0,100)
    if ((float(membreClan1)/(membreClan1+membreClan2))*100 <= randomOutcome):   #Clan1 gagne
        $ membreClan1 += int(2+membreClan2*0.05)
        $ membreClan2 -= int(2+membreClan2*0.05)
        if (membre + membreClan1 + membreClan2)%2 == 1:
            $ membreClan1+=1

    else:   #Clan2 gagne
        $ membreClan1 -= int(2+membreClan1*0.05)
        $ membreClan2 += int(2+membreClan1*0.05)
        if (membre + membreClan1 + membreClan2)%2 == 1:
            $ membreClan2+=1


    jump dialogue

label perdu:

    "Vous n'avez plus de membre voulant se battre pour vous, vous finissez par rester seul dans une pièce vide, sombre et sans aucun bruit..."

    return
