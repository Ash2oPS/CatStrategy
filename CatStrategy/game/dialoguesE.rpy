label dialogueE1:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Chef ! Un énorme bruit venant de la surface et un séisme se sont fait ressentir dans tout le souterrain. Nos chats ont peur." #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        " Payer 40 brins de Catnabis pour prendre parole devant les chats et les rassurer.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            if randomChance == 1:    #Une chance sur trois que ça se passe bien
                chat "Vous avez été fantastique chef ! Quatre chats d’autres clans nous ont rejoints quand ils ont vu à quel point vous étiez attentif à nos besoins !"
                $ argent -= 40  # le dollar veux dire qu'on écrit en python, c'est surtout utilisé pour modifié ou créer une valeur
                $ membre += 4

                #On perd des membres donc les autres clans doivent en gagner, mais uniquement si ils sont encore vivant
                if !clan1Vivant:    #si le clan 1 est mort, le clan 2 prend tout
                    $ membreClan2 -= 4

                elif !clan2Vivant
                    $ membreClan1 -= 4

                else:   #si les deux sont encore vivant on partage
                    $ membreClan1 -= 2
                    $ membreClan2 -= 2


            else:   #Si le joueur n'a pas eu le 1 chance sur 3 que ça se passe bien
                chat "Vous vous êtes plutôt bien débrouillé, chef. Les chats se sont calmés."
                $ argent -= 40


        "Ne rien faire.":  #Deuxième choix du joueur
            if randomChance == 1:
                chat "La plupart des chats se sont calmés d’eux-mêmes. Cependant, deux chats ont décidé de partir pour un autre clan dont le chef a su tenir un discours des plus rassurants."
                $ membre -= 2

                if !clan1Vivant:
                    $ membreClan2 += 2

                elif !clan2Vivant
                    $ membreClan1 += 2

                else:
                    $ membreClan1 += 2

            else:
                chat "La plupart des chats se sont calmés d’eux-mêmes. En espérant qu’ils soient tous aussi conciliants la prochaine fois."

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE2:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Bonsoir. Dites, je me demandais si vous pouviez me donner un coup de patte. Nous vivons très mal avec ma famille. Pourriez-vous nous donner une petite avance s’il vous plaît." #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Leur donner 40 brins de Catnabis.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            if randomChance == 1:    #Une chance sur trois que ça se passe bien
                chat "Merci beaucoup, vous êtes le meilleur !"
                $ argent -= 40


        "Refuser":  #Deuxième choix du joueur
            if randomChance == 1:
                chat "Vous n’avez aucun coeur ! Nous partons pour un clan plus conciliant !"
                $ membre -= 2

                if !clan1Vivant:
                    $ membreClan2 += 2

                elif !clan2Vivant
                    $ membreClan1 += 2

                else:
                    $ membreClan1 += 2

            else:
                chat "Arfh, très bien, je peux comprendre…"

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE3:

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Chef ! Il nous faut une plus grosse puissance militaire ! Améliorons notre Chaserne d’Entraînement ! Il faut pouvoir se défendre en cas d’attaque ennemie." #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Améliorer la Chaserne pour 40 brins de Catnabis.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "C’est une sage décision, chef !"
            $ argent -= 40
            $ membreAttaque += .1


        "Refuser.":  #Deuxième choix du joueur
            chat "Très bien, c’est vous qui voyez."


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE4:

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Monsieur, nous sommes motivés pour construire un nouveau silo pour contenir notre eau ! Nous ne serons plus obligés de nous limiter à nos petits silos actuels. Vous en pensez quoi ?" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Construire un nouveau silo d’eau pour 40 brins de Catnabis.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "C’est une sage décision, chef !"
            $ argent -= 40
            $ eauMax += 50


        "Refuser.":  #Deuxième choix du joueur
            chat "Meh, tant pis. On était pas si motivés, de toute façon."


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE5:

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Wesh frère, ça t’dirait qu’on améliore nos fermes à Catnabis ? Avec ça, tu pourras te faireplus d’oseille !" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Améliorer les fermes à Catnabis pour 40 brins de Catnabis.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Meheh, c’est un plaisir de faire affaire avec vous."
            $ argent -= 40
            $ boostArgent += 1


        "Refuser.":  #Deuxième choix du joueur
            chat "‘Kay, salut."


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE6:
    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Bonjour, chef. J’ai trouvé le moyen d’améliorer les filtres à eau ! Nous pourrons récolter davantage d’eau quotidiennement !" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Améliorer les filtres à eau pour 40 brins de Catnabis.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Très bien, je me mets au travail !"
            $ argent -= 40
            $ boostFiltre += 0.1


        "Refuser.":  #Deuxième choix du joueur
            chat "Bien, ça sera pour une prochaine fois."

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE7:
    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Nous avons besoin de plus de nourriture, chef ! Améliorons notre camp de Chats-seurs pour récupérer plus de rats !" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Améliorer le camp de Chats-seurs pour 40 brins de Catnabis":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Très bien, je me mets au travail !"
            $ argent -= 40
            $ boostRecolte += 0.1


        "Refuser.":  #Deuxième choix du joueur
            chat "J’imagine que nous avons assez de nourriture alors..."

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE8:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Chef, nous entendons de plus en plus de gros bruits venant de la surface. Que se passe-t-il ?" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Lui dire que tout va bien.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Hm très bien, si vous le dites..."

        "Lui dire que les humains sont des êtres très bruyants.":  #Deuxième choix du joueur
            chat "Oui, j’ai cru constater ça ! J’espère qu’ils vont bien, quand même."

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE9:

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Chef, il n’y a que trois films de disponibles dans notre vidéo-club. Vous voulez pas financer la production de nouveaux ?" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Payer 20 brins de Catnabis pour que de nouveaux films voient le jour.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Génial ! Je suis sûr que de nouveaux chats vont venir pour découvrir ces nouveautés !"
            $ argent -= 20  # le dollar veux dire qu'on écrit en python, c'est surtout utilisé pour modifié ou créer une valeur
            $ membre += 2

            #On perd des membres donc les autres clans doivent en gagner, mais uniquement si ils sont encore vivant
            if !clan1Vivant:    #si le clan 1 est mort, le clan 2 prend tout
                $ membreClan2 -= 2

            elif !clan2Vivant
                $ membreClan1 -= 2

            else:   #si les deux sont encore vivant on partage
                $ membreClan1 -= 1
                $ membreClan2 -= 1


        "Refuser.":  #Deuxième choix du joueur
                chat "Moui, je m’en doutais un peu. Bon eh bien, continuons de nous ennuyer alors..."

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE10:

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Regardez ! Vous avez reçu une lettre de menace ! Elle dit que si vous ne me donnez pas 5 rats, vous serez bientôt assassiné !" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Lui donner les 5 rats":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Vous acceptez ? Vraiment ? Enfin, je veux dire, oui ! C’est une sage décision !"
            $ nourriture -= 5

        "Ne rien faire.":  #Deuxième choix du joueur
                chat "Moui bon, c’était pas vraiment crédible, hein ? J’aurais essayé..."

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE11:
    $ randomChance = renpy.random.randint(1,3)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Quelle horreur ! Les fermes à Catnabis se sont fait dévaliser ! Qu’allons-nous faire ?" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        " Payer 10 rats pour retrouver les voleurs":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Les voleurs ont été appréhendés ! Le Catnabis volé a été récupéré !"
            $ nourrite -= 10


        "Partir vous-même à la poursuite des voleurs.":  #Deuxième choix du joueur
            if randomChance == 1:
                chat "Wow, vous avez réussi, bravo chef, vous avez tout récupéré. J’espère que vous leur avez fait payer !"

            else:
                chat "Rah, bien essayé, mais vous ne les avez pas rattrapés…"
                $ argent = int((argent/3)*2)

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE12:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Nous avons besoin de plus de membres dans notre clan ! Que souhaitez-vous faire ?" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        " Payer 40 brins de Catnabis pour créer une campagne publicitaire.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            if randomChance == 1:    #Une chance sur trois que ça se passe bien
                chat "“Wow, elle a vraiment fait fureur ! Elle nous a ramené quatre nouveaux chats !"
                $ argent -= 40  # le dollar veux dire qu'on écrit en python, c'est surtout utilisé pour modifié ou créer une valeur
                $ membre += 4

                #On perd des membres donc les autres clans doivent en gagner, mais uniquement si ils sont encore vivant
                if !clan1Vivant:    #si le clan 1 est mort, le clan 2 prend tout
                    $ membreClan2 -= 4

                elif !clan2Vivant
                    $ membreClan1 -= 4

                else:   #si les deux sont encore vivant on partage
                    $ membreClan1 -= 2
                    $ membreClan2 -= 2


            else:   #Si le joueur n'a pas eu le 1 chance sur 3 que ça se passe bien
                chat "Elle nous a ramené 1 nouveau chat, c’est déjà pas mal, non ?"
                $ argent -= 40
                $ membre += 1

                #On perd des membres donc les autres clans doivent en gagner, mais uniquement si ils sont encore vivant
                if !clan1Vivant:    #si le clan 1 est mort, le clan 2 prend tout
                    $ membreClan2 -= 1

                elif !clan2Vivant
                    $ membreClan1 -= 1

                else:   #si les deux sont encore vivant on partage
                    $ membreClan1 -= 1


        "Payer 5 rats pour que vos chats fassent un spectacle inter-clan.":  #Deuxième choix du joueur
            if randomChance == 1:
                chat "Haha, le spectacle a cartonné ! 3 chats se sont joints à nous !"
                $ membre += 3
                $ nourriture -= 5

                if !clan1Vivant:
                    $ membreClan2 -= 3

                elif !clan2Vivant
                    $ membreClan1 -= 3

                else:
                    $ membreClan1 -= 2
                    $ membreClan2 -= 1

            else:
                chat "Aïe, c’était… pitoyable. L’un de nos chats s’est tellement senti mal à l’aise qu’il a préféré partir."
                $ membre -= 1
                $ nourriture -= 5

                if !clan1Vivant:
                    $ membreClan2 += 1

                elif !clan2Vivant
                    $ membreClan1 += 1

                else:
                    $ membreClan1 -= 1

        "Ne rien faire":
            chat "Ne faisons rien alors..."


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE13:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Ma femme a réalisé ces super cookies ! Vous voulez en acheter ?" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Acheter les cookies pour 10 brins de Catnabis.":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            chat "Vous êtes si généreux, merci !"
            $ argent -= 10

        "Refuser":  #Deuxième choix du joueur
            if randomChance == 1:
                chat "C’est vraiment dommage, ils sont si délicieux !"

            else:
                chat "Hm, nous allons en faire pour un autre chef de clan. Lui peut-être saura apprécier nos efforts !"
                $ membre -= 2

                #On perd des membres donc les autres clans doivent en gagner, mais uniquement si ils sont encore vivant
                if !clan1Vivant:    #si le clan 1 est mort, le clan 2 prend tout
                    $ membreClan2 += 2

                elif !clan2Vivant
                    $ membreClan1 += 2

                else:   #si les deux sont encore vivant on partage
                    $ membreClan2 += 2


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE14:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:
        chat "Pierre, feuille, ciseaux !"

        "Pierre.":
            if randomChance == 1:
                chat "Feuille ! Ha vous avez perdu ! Vous me devez 2 rats !"
                $ nourriture -= 2

            else:
                chat "Ciseaux ! Rah, bien joué… Tenez, 20 brins de Catnabis..."
                $ argent += 20

        "Feuille.":
            if randomChance == 1:
                chat "Ciseaux ! Ha vous avez perdu ! Vous me devez 2 rats !"
                $ nourriture -= 2

            else:
                chat "Pierre ! Rah, bien joué… Tenez, 20 brins de Catnabis..."
                $ argent += 20

        "Ciseaux":
            if randomChance == 1:
                chat "Pierre ! Ha vous avez perdu ! Vous me devez 2 rats !"
                $ nourriture -= 2

            else:
                chat "Feuille ! Rah, bien joué… Tenez, 20 brins de Catnabis..."
                $ argent += 20

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE15:

    menu:
        chat "Les chiens sont des être diaboliques, n’est-ce pas ? Pourquoi est-ce que les humains les préfèrent à nous ?"

        "Lui dire que les humains sont stupides.":
            chat "Moui, ça m’en a tout l’air ! Mais bon, ils avaient l’air si gentils avec nous autrefois..."

        "Lui dire que les chiens ne sont pas si ignobles.":
            chat "C’est vrai ? C’est… inattendu..."


    jump dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE16:

    menu:
        chat "Chef, regardez, j’ai trouvé de quoi remplir 50% d’un silo d’eau. Je vous propose ça contre 8 rats. Entendu ?"

        "Accepter.":
            chat "Ah génial, j’espère que vous ne boirez pas tout d’un coup !"
            $ eau += 50
            if eau > eauMax:
                eau = eauMax

        "Refuser.":
            chat "Dans ce cas, je garde toute cette eau pour moi !"


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE17:
    $ randomChance = renpy.random.randint(1,2)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Monsieur le chef, j’ai, genre, ultra méga faim là ! Soit vous me donnez 3 rats, soit je vais voir ailleurs !" #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Lui donner 3 rats":
            chat "Je vais m'éclater la panse ! Ce soir, c'est plateau-télé !"
            $ nourriture -= 3

        "Refuser.":
            chat "Dans ce cas, adieu !"
            $ membre -= 1

            if !clan1Vivant:
                $ membreClan2 += 1

            elif !clan2Vivant
                $ membreClan1 += 1

            else:
                $ membreClan2 += 1

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue
