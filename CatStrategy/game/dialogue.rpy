label double_rats_chasse:
    $ randomChance = renpy.random.randint(1,3)  #Random pour le choix qui a une chance sur trois

    menu:   #"menu:" veux dire qu'on va proposer un choix au joueur

        chat "Chef, nos chasseurs ont trouvé le double des rats habituels aujourd’hui ! Cependant, certains sont d’une couleur inhabituelle..." #Texte du chat qui nous parle (on met chat avant un dialogue quand c'est l'un de nos chat qui nous parle)

        "Garder ces rats":  #un texte avec :  après c'est l'un des choix pour le joueur, le tete entre guillemets c'est ce que verra le joueur
            if randomChance == 1:    #Une chance sur trois que ça se passe bien
                chat "Super, tout s’est bien passé ! Quel festin !"
                $ nourriture += membre*0.7  # le dollar veux dire qu'on écrit en python, c'est surtout utilisé pour modifié ou créer une valeur

            else:   #Si le joueur n'a pas eu le 1 chance sur 3 que ça se passe bien
                chat "Oh oh, certains de nos chats sont tombés malades et sont partis dans un autre clan pour vivre une vie plus… saine."
                $ nourriture += membre*0.7  #membre*0.7 c'est la nourriture récup par les chasseurs(en vrai c'est différent et avec du random, mais on va faire simple pour les dialogue)
                $ membre -= 3   #quand un clan perd un membre, un autre doit le gagné, le faire en random c'est relou donc on va faire simple pour les dialogues

                #On perd des membres donc les autres clans doivent en gagner, mais uniquement si ils sont encore vivant
                if !clan1Vivant:    #si le clan 1 est mort, le clan 2 prend tout
                    $ membreClan2 += 3

                elif !clan2Vivant:
                    $ membreClan1 += 3

                else:   #si les deux sont encore vivant on partage
                    $ membreClan1 +=2
                    $ membreClan2 += 1

        "Jeter les rats en trop.":  #Deuxième choix du joueur
            chat "Bon, tant pis. J’imagine que c’est plus sage de les jeter."

        "Payer 15 brins de Catnabis pour purifier les rats" if argent >= 15:  #Troisième choix du joueur qui ne s'affiche que si la condition est vraie, là c'est que si le joueur a 40 argent ou plus
            chat "Génial, payons-nous ces superbes et délicieux rats !"
            $ argent -= 15
            $ nourriture += membre*0.7

    jump dialogue #a la fin on reviens aux label dialogue qui va choisir un autre dialogue


label mariage_clan_adverse:
    $ randomChance = renpy.random.randint(1,2)

    menu:
        chat "Salut. J’aimerais me marier avec un chat d’un autre clan. J’ai le droit ?"

        "Accepter":
            if randomChance == 1:
                chat "Z’êtes top ! Je pars emménager là-bas !"
                $ membre-=1
                if clan1Vivant:
                    $ membreClan1 += 1
                else:
                    $ membreClan2 += 1
            else:
                chat "Trop bien ! Ca fait un nouveau chat parmi nous !"
                $ membre += 1

                if clan2Vivant:
                    $ membreClan2 -= 1
                else:
                    $ membreClan1 -= 1
                $ membre += 1

        "Financer le mariage avec 25 Catnabis." if argent >= 25:
            chat "Wow, merci ! Vous êtes grave sympa en fait !"
            $ argent -= 25
            $ nourriture += 10
            $ membre += 1

            if clan2Vivant:
                $ membreClan2 -= 1
            else:
                $ membreClan1 -= 1

        "Refuser":
            chat "Sérieux ? Ca s'fait trop pas !"

    jump dialogue


label fils_bully:

    menu:

        chat "Bonsoir. Il y a un péquenaud venu d’un autre clan qui embête mon fils. Vous pouvez y faire quelque chose ?"

        "L'encourager à se défendre":
            chat "Hm, ok. On va essayer ça, j’imagine."

        "Payer 40 brins de Catnabis les aider à déménager." if argent >= 40:
            $ argent -= 40
            $ boostRecolte+= 0.03
            chat "Oh merci bien ! Mon fils travaillera mieux dans ces conditions, il ramenera plus de rats pendant les chasses."

        "Ne rien faire":
            chat "Oh beh super. Merci pour votre aide. Quel chef pathétique !"

    jump dialogue

label maison_brule:

    menu:
        chat "Y a l’feu ! Ma maison est en train d’brûler !"

        "Utiliser 15 d’eau pour éteindre le feu." if eau > 15:
            chat "Vous nous avez sauvés ! Merci, que Dieu vous bénisse !"
            $ eau -= 15

        "Ne rien faire":
            chat "Vous êtes inutile ! Maintenant que notre maison est en cendre, on dégage !"
            $ membre -= 2

            if clan1Vivant:
                $ membreClan1 += 2
            else :
                $ membreClan2 += 2

    jump dialogue


label offre_rat:

    menu:

        chat "Toutes mes plus plates salutations, très cher seigneur. Je vous propose d’acheter 10 de mes rats personnels pour SEULEMENT 30 brins de Catnabis. C’est une affaire à ne pas manquer !"

        " Accepter" if argent >= 30:
            chat "Miahaha, vous ne le regretterez pas !"
            $ argent -= 30
            $ nourriture += 10

        "Refuser":
            chat "Euh… Vous venez de passer à côté de l’affaire du siècle…"

    jump dialogue


label proposition_mariage:

    menu:

        chat "Bonjour chef, enchanté. Voulez-vous m’épouser ?"

        "Accepter":
            chat "Nan mais c’est bon, je plaisantais."

        "Refuser":
            chat "C’est offensant, mais ok."

    jump dialogue


label etoile_filante:
    $ randomChance = renpy.random.randint(1,2)
    menu:
        chat "Bonjour, monsieur ! J’ai vu une étoile filante cette nuit et j’ai fait le vœu que vous me donniez un rat supplémentaire aujourd’hui. Dites, vous acceptez ?"

        "Révelez ton voeu le rend irréalisable.":
            chat "Ah… Oui vous avez raison. Pardonnez-moi..."

        "Accepter" if nourriture >= 1:
            chat "Oh merci beaucoup ! Je savais que j’avais bien fait de ne pas dormir de la nuit !"
            $ nourriture -= 1

        "Lui demander de payer 2 brin de Catnabis en échange." if nourriture >= 1:
            if randomChance == 1:
                chat "Je… Non. Je ne peux pas me le permettre…"

            else:
                chat "Oh eh bien, oui. J’imagine que c’est plus juste ainsi..."
                $ nourriture -= 1
                $ argent += 2

    jump dialogue


label peur_chien:
    $ randomChance = renpy.random.randint(1,2)

    menu:
        chat "J’entends les chiens de la surface aboyer de chez moi. J’ai peur..."

        "Nous sommes tous en sécurité.":
            chat "J’espère que vous avez raison..."

        "Lui faire comprendre qu’il est temps de se ressaisir.":
            if randomChance == 1 and nourriture >= 1:
                chat "Je vous ai chouré de la bouffe ! Ca vous apprendra à me parler comme ça !"
                $ nourriture -= 1

            else:
                chat "Ok, oui, je dois prendre sur moi et ne plus y penser ! Tenez, pour vous remercier je vous donne un peu de mes Catnabis."
                $ argent += 8

    jump dialogue


label fuite_silo:
    $ randomChance = renpy.random.randint(1,2)

    menu:
        chat "Chef ! Notre silo a une fuite, nous sommes en train de perdre une grosse quantité d’eau !"

        "Payer 30 brins de Catnabis pour le réparer rapidement." if argent >= 30:
            chat "Super, mission accomplie, nous n’avons rien perdu !"
            $ argent -= 30

        "Leur dire de gérer le problème comme il peuvent":
            chat "Nous avons pu le réparer, mais nous avons perdu pas mal d’eau..."
            if eau < 15:
                $ eau = 0
            else:
                $ eau -= 15

    jump dialogue

label rat_geant:
    $ randomChance = renpy.random.randint(1,2)

    menu:
        chat "Wow, chef ! Un rat VRAIMENT gigantesque a été vu pas loin du village ! Que voulez-vous faire ?"

        "Envoyer des chasseurs à sa poursuite.":

            if randomChance == 1:
                chat "Nous avons pu le récupérer ! On va se régaler, chef !"
                $ nourriture += 15

            else:
                chat "Hum... nous n’avons pas pu le récupérer… A vrai dire, il a même effrayé un chat qui a décidé de partir pour un autre clan..."
                $ membre -= 1
                if clan1Vivant:
                    $ membreClan1 += 1
                else:
                    $ membreClan2 += 1

        "Ne rien faire.":
            if randomChance == 1:
                chat "Sacrebleu ! Le rat géant a effrayé deux de nos chats qui ont décidé de partir…"
                $ membre -= 2
                if clan1Vivant:
                    $ membreClan1 += 2
                else:
                    $ membreClan2 += 2

            else:
                chat "Ok, chef, dans ce cas nous ne faisons rien."

    jump dialogue


label legende_humains:

    menu:

        chat "Dites, je me pose une question. Mes parents m’ont souvent parlé des humains. Mais ce n’est qu’une légende. Ils n’ont jamais existé… Si ?"

        "Lui dire que ce n’est qu’une légende.":
            chat "Haha, bien sûr ! Désolé de vous avoir posé une question aussi bête !"

        "Lui dire la vérité.":
            chat "Oh… Je vois. Eh bien, je vous avouerais que j’aurais aimé connaître la belle époque où nous étions chouchoutés par ces dieux… Enfin, merci de votre sincérité."

    jump dialogue


label pull_over:

    menu:
        chat "Eh, regardez ! Ma fille m’a offert un pull à votre effigie."

        "Lui dire que c’est magnifique.":
            chat "Haha, moi aussi j’aime beaucoup !"

        "Faire semblant de vomir pour exprimer votre dégoût.":
            chat "Ah… euh… Oui, je le trouve hideux moi aussi..."

    jump dialogue

label chien_soutterain:
    $ randomChance = renpy.random.randint(1,4)

    menu:
        chat "Chef, il y a urgence ! Un chien est entré dans le souterrain ! Que devons-nous faire ?"

        "L’attaquer.":
            if randomChance >= 2:
                chat "Mission accomplie, le chien est remonté à la surface, complètement effrayé !"

            else:
                chat "On a réussi à le faire remonté à la surface, mais 3 de nos chats ont décidé de quitter le clan à cause des risques que vous leur avez fait prendre…"
                $ membre -= 3
                if !clan1Vivant:
                    $ membreClan2 += 3

                elif !clan2Vivant:
                    $ membreClan1 += 3

                else:
                    $ membreClan1 += 1
                    $ membreClan2 += 2

        "Se cacher.":
            if randomChance == 1:
                chat "Aucun chat n’a été blessé chef mais il semblerait que le chien nous ait fait perdre une partie de notre nourriture et de notre eau..."
                if nourriture >= 35:
                    $ nourriture -= 35
                else:
                    $ nourriture = 0

                if eau >= 30:
                    $ eau -= 30
                else:
                    $ eau = 0
            else:
                chat "Aucun chat n’a été blessé chef ! Le chien est reparti à la surface sans avoir causé le moindre dégât !"

    jump dialogue


#renpy.random.randint(1,2)
