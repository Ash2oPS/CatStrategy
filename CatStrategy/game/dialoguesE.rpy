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



            else:   #Si le joueur n'a pas eu le 1 chance sur 3 que ça se passe bien
                chat "C’est une sage décision, chef !"
                $ argent -= 40
                $ membreAttaque += .1


        "Refuser.":  #Deuxième choix du joueur
                chat "Très bien, c’est vous qui voyez."


    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


#----------------------------------------------------------------------------------------------------------------------

label dialogueE4:
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

label dialogueE5:
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

label dialogueE6:
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

label dialogueE7:
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

label dialogueE8:
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

label dialogueE9:
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

label dialogueE10:
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

label dialogueE11:
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

label dialogueE12:
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

label dialogueE13:
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

label dialogueE14:
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

label dialogueE15:
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

label dialogueE16:
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

label dialogueE17:
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

label dialogueE18:
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