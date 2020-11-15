                    #- --- --- --- Who killed Jim ? --- --- --- -#

import time

time.sleep(1)

print(" ")
print("   <> Who killed Jim ? <>")
print(" ")
time.sleep(1)

print("Vous êtes Nathan, 17 ans.")
print("Jim, votre petit ami, s'est suicidé. Vous allez donc interroger ses amis via SMS afin de découvrir ce qui l'a poussé à mettre fin à ses jours.")
print(" ")
time.sleep(4)

#Lorsque n=666, le jeu s'arrête et le joueur a perdu.
#Lorsque n=111, le joueur a trouvé une preuve.

clé_emma=0 #débloquée avec Lucie
clé_stéphane=0 #débloquée avec Léonard

a=0
v=0

#- N° fins : 100,101,102,103,104,105,106,107,108,109,110,111,112



#- ---[ MESSAGES LUCIE ]--- - #

messages_Lucie=[]

message0=["Lucie : Hey !","Salut, ça va ?","Cc, cv ?","Hello, ça va ?",1,1,1]
messages_Lucie.append(message0)

message1=["Lucie : Oui et toi ?","Non","Ça peut aller","Oui",2,2,100]
messages_Lucie.append(message1)

message2=["Lucie : Qu'est-ce qui ne va pas ?","C'est depuis la mort de Jim, je me questionne beaucoup.","La mort de Jim me chagrine...","Rien.",3,4,100]
messages_Lucie.append(message2)

message3=["Lucie : Qu'est-ce qui te chiffonne ?","Je me demande ce qui l'a poussé au suicide.","Que lui est-il donc arrivé...","Rien.",5,5,100]
messages_Lucie.append(message3)

message4=["Lucie : C'est vrai, il était si gentil...","Mais il y a quelque chose qui me trouble...","Il me manque...","Je suis perdu sans lui...",3,101,102]
messages_Lucie.append(message4)

message5=["Lucie : Ah...","Tu sais quelque chose ?","Qu'est-ce qu'il y a ?","Y'a quoi ?",6,7,7]
messages_Lucie.append(message5)

message6=["Lucie : Oui...","Explique-moi.","Dis-moi tout.","Dis le moi alors !!!",10,10,8]
messages_Lucie.append(message6)

message7=["Lucie : Rien, je suis juste un peu fatiguée...","N'en fais pas trop !","Ménage-toi !","On l'est tous, repose-toi !",104,104,112]
messages_Lucie.append(message7)

message8=["Lucie : Tu me fais peur...","Bon, pas grave...","Rien à foutre ! Dis !","Osef, fais pêter les infos !",9,103,103]
messages_Lucie.append(message8)

message9=["Lucie : Merci...","Connasse.","Pffff...",":)",666,666,666]
messages_Lucie.append(message9)

message10=["Lucie : C'était il y a plusieurs semaines avant le suicide de Jim... j'avais pris le téléphone d'Emma. Dedans, j'ai vu qu'elle le menaçait de révéler son hommosexualitéà tout le monde  s'il ne te quittait pas...","Ok, merci beaucoup...","D'accord","Merci",999,999,999]
messages_Lucie.append(message10)



#- ---[ MESSAGES LÉONARD ]--- -#

messages_Leonard=[]

message0=["Léonard : Hey ! Tu vas bien ? Je sais que c'est pas facile...","Salut Leo, ça va moyen... et toi ?","Ça va, et toi ?","Yo.",1,2,2]
messages_Leonard.append(message0)

message1=["Léonard : Mieux que toi je pense...","Ne t'inquiète pas pour moi...","C'est pas grave","Je suis toujours sous le choc...",3,3,4]
messages_Leonard.append(message1)

message2=["Léonard : Ma foi, tu m'as l'air bien enjoué, étonnant vu les derniers événements...","Je suis toujours sous le choc...","J'essaie de faire comme je peux.","Détrompe-toi, c'est très dur...",4,4,4]
messages_Leonard.append(message2)

message3=["Léonard : Si je dis que je suis inquiet pour toi, ça change quelque chose ?","Non","Au moins je peux compter sur toi :)","J'aimerais tellement savoir pourquoi il a fait ça...",666,5,6]
messages_Leonard.append(message3)

message4=["Léonard : J'imagine à peine ce que tu dois vivre...","J'aimerais tellement savoir pourquoi il a fait ça...","Il était tout pour moi...","Oui, c'est dur...",6,105,105]
messages_Leonard.append(message4)

message5=["Léonard : Oui...","Je t'aime" ,"Merci :)","Qu'y a-t-il ? Tu sais quelque chose ?",107,666,7]
messages_Leonard.append(message5)

message6=["Léonard : Moi aussi...","Qu'y a-t-il ? Tu sais quelque chose ?","Que sais-tu ?", "Tu sais quelque chose ? Dis-le moi !",7,7,7]
messages_Leonard.append(message6)

message7=["Léonard : Je... je pense que Stéphane n'est pas étranger à l'affaire... Lorsque Jim lui a dit qu'il était homosexuel, il a paru choqué. Une fois, après la séance de sport, je l'ai vu avec ses copains déchirer ses vêtements...","Vraiment ? Je n'y crois pas... merci en tout cas.","Ah... merci pour ces renseignements, Léo...","Ce salaud va avoir affaire à moi. Merci, Léo.",999,999,999]
messages_Leonard.append(message7)



#- ---[ MESSAGES EMMA ]--- -#

messages_Emma=[]

message0=["Emma : Salut","Coucou !","Salut","Je ne suis pas d'humeur, pardon.",3,1,2]
messages_Emma.append(message0)

message1=["Emma : Ça va ?","Oui, oui","Pas trop, la mort de Jim est... Il me manque.","Ça pourrait aller mieux.",2,3,3]
messages_Emma.append(message1)

message2=["Emma : Tu n'as pas l'air très touché.","Concrètement, je m'en fous.","Bah non.","Détrompe-toi, c'est vraiment douloureux...",110,110,3]
messages_Emma.append(message2)

message3=["Emma : Je comprends, c'est vrai que c'est dur pour moi aussi...","Te fous pas de moi, salope !","Ne me mens pas, je sais toute l'histoire grâce à Lucie.","Je sais que Jim est mort à cause de toi.",5,5,5]
messages_Emma.append(message3)

message4=["Emma : Je comprends, c'est vrai que c'est dur pour moi aussi.","Je te laisse, je dois faire mon deuil.","Oui...","L'inverse serait étonnant.",666,109,666]
messages_Emma.append(message4)

message5=["Emma : Hein ? De quoi ?","Qu'est-ce qui justifie ton meurtre ?","Connasse ! Pourquoi tu as fait ça ?","Tu l'as tué, quelle est ta défense ?",111,111,111]
messages_Emma.append(message5)



#- ---[ MESSAGES STÉPHANE ]--- -#

messages_Stéphane=[]

message0=["Stéphane : Hello, commment tu vas ?", "Mal...","Moyennement bien...","Très bien.",2,2,112]
messages_Stéphane.append(message0)

message1=["Stéphane : La mort de Jim est vun choc pour nous tous, il était vraiment très apprécié...","Savoir que je ne reverrai jamais son doux visage me tord les tripes...","Ça, je ne sais pas... Beaucoup de personnes n'ont pas digéré son homosexualité.","Évidemment ! C'était le garçon le plus gentil et le plus sympa au monde !",113,3,113]
messages_Stéphane.append(message1)

message2=["Stéphane : C'est compréhensible.","Pas vraiment.","Les gens sont des connards.","Sûrement..."]
messages_Stéphane.append(message2)

message3=["Stéphane : Heureusement que tu as de bons amis :)","Oui, je suis content que vous me supportiez.","Je ne sais pas ce que je serais sans vous...","Comme toi :)",114,4,5]
messages_Stéphane.append(message3)

message4=["Stéphane : Rien x)","xD !","Mais quel con :P","lol",115,115,115]
messages_Stéphane.append(message4)

message5=["Stéphane : Je suis ton ami ! Et je pense que j'étais également le meilleur de Jim...","Sûrement...","Il me manque...","Oui :)",116,116,116]
messages_Stéphane.append(message5)

message6=["Stéphane : C'est compréhensible.","Sutout par toi.","Homophobe.","Tu n'es qu'une sombre merde.",7,7,8]
messages_Stéphane.append(message6)

message7=["Stéphane : Pardon ?","Je sais que tu as harcelé Jim.","C'est de ta faute s'il est mort.","Tu l'as tué.",117,117,117]
messages_Stéphane.append(message7)

message8=["Stéphane : Hey, pourquoi tant de violence ?","Je sais que tu as harcelé Jim.","C'est de ta faute s'il est mort.","Tu l'as tué.",117,117,117]
messages_Stéphane.append(message8)




#- ---[ MESSAGES ]--- -#

n=0
while n!=99 :




    #- MENU PERSOS 1

    if v==0 :
        n=0
        print(" ----- ")
        print(" ")

        print("Choisissez un contact :")
        print("  1 : Lucie")
        print("  2 : Léonard")
        print("  3 : Emma")
        print("  4 : Stéphane")

        print(" ")
        print(" ----- ")
        print(" ")

        x=input()
        if int(x)==1:
            a=1
        if int(x)==2:
            a=2
        if int(x)==3:
            a=3
        if int(x)==4:
            a=4
        print(" ")

        time.sleep(2)




    #- MENU PERSOS 2

        #- Lucie
    if a==1 :
        print("1 : Parler")
        print("2 : Voir le profil")
        x=input()
        print(" ")

        if int(x)==1:
            v=1
            a=0

        if int(x)==2:
            print("Lucie Peinte, 15 ans")
            print("N° Mobile : 06-92-23-18-62")
            print("Email : lucie.peinte@penlium.com")
            print(" ")
            time.sleep(1)
            a=1


        #- Léonard
    if a==2 :
        print("1 : Parler")
        print("2 : Voir le profil")
        x=input()
        print(" ")

        if int(x)==1:
            v=2
            a=0

        if int(x)==2:
            print("Léonard Bare, 16 ans")
            print("N° Mobile : 06-73-38-19-45")
            print("Email : lbare@exacempta.fr")
            print(" ")
            time.sleep(1)
            a=2


        #- Emma
    if a==3 :
        print("1 : Parler")
        print("2 : Voir le profil")
        x=input()
        print(" ")

        if int(x)==1:
            v=3
            a=0

        if int(x)==2:
            print("Emma Reinchter, 17 ans")
            print("N° Mobile : 07-23-42-92-30")
            print("Email : emmadu36@espaki.com")
            print(" ")
            time.sleep(1)
            a=3


        #-Stéphane
    if a==4 :
        print("1 : Parler")
        print("2 : Voir le profil")
        x=input()
        print(" ")

        if int(x)==1:
            v=4
            a=0

        if int(x)==2:
            print("Stéphane Ganach, 16 ans")
            print("N° Mobile : 06-12-48-22-83")
            print("Email : stephaneganach@stab.com")
            print(" ")
            time.sleep(1)
            a=4




    #- CONVERSATIONS

        #- Lucie
    if v==1 :
        if n==10 :
            clé_emma=1
        time.sleep(1)

        print(messages_Lucie[n][0])
        print("  Réponse 1: "+messages_Lucie[n][1])
        print("  Réponse 2: "+messages_Lucie[n][2])
        print("  Réponse 3: "+messages_Lucie[n][3])

        x=input()
        if int(x)==1:
            n=messages_Lucie[n][4]
        if int(x)==2:
            n=messages_Lucie[n][5]
        if int(x)==3:
            n=messages_Lucie[n][6]
        print(" ")


        #-Léonard
    if v==2 :
        time.sleep(1)
        if n==7 :
            clé_stephane=1

        print(messages_Leonard[n][0])
        print("  Réponse 1: "+messages_Leonard[n][1])
        print("  Réponse 2: "+messages_Leonard[n][2])
        print("  Réponse 3: "+messages_Leonard[n][3])

        x=input()
        if int(x)==1:
            n=messages_Leonard[n][4]
        if int(x)==2:
            n=messages_Leonard[n][5]
        if int(x)==3:
            n=messages_Leonard[n][6]
        print(" ")


        #- Emma
    if v==3 :
        time.sleep(1)

        if n==3 :
            if clé_emma==0 :
                n=4

        print(messages_Emma[n][0])
        print("  Réponse 1: "+messages_Emma[n][1])
        print("  Réponse 2: "+messages_Emma[n][2])
        print("  Réponse 3: "+messages_Emma[n][3])

        x=input()
        if int(x)==1:
            n=messages_Emma[n][4]
        if int(x)==2:
            n=messages_Emma[n][5]
        if int(x)==3:
            n=messages_Emma[n][6]
        print(" ")


        #- Stéphane
    if v==4 :
        time.sleep(1)

        if n==3 :
            if clé_stéphane==1 :
                n=6

        print(messages_Leonard[n][0])
        print("  Réponse 1: "+messages_Stéphane[n][1])
        print("  Réponse 2: "+messages_Stéphane[n][2])
        print("  Réponse 3: "+messages_Stéphane[n][3])

        x=input()
        if int(x)==1:
            n=messages_Stéphane[n][4]
        if int(x)==2:
            n=messages_Stéphane[n][5]
        if int(x)==3:
            n=messages_Stéphane[n][6]
        print(" ")



#- PREUVES / GAME OVER -#

    if n==999 :
        time.sleep(1)
        print("<> Félicitations, vous avez découvert une preuve ! <>")
        print(" ")
        print(" ")
        time.sleep(1)
        v=0

    if n==666 :
        time.sleep(1)
        print("<> Votre interlocuteur a quitté la conversation. <>")
        print(" ")
        print(" ")
        time.sleep(1)
        v=0


#- RÉPONSES -#

    if n==100 :
        time.sleep(1)
        print("Lucie : D'accord.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==101 :
        time.sleep(1)
        print("Lucie : À nous aussi.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==102 :
        time.sleep(1)
        print("Lucie : Nous aussi.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==103 :
        time.sleep(1)
        print("Lucie : Non.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==104 :
        time.sleep(1)
        print("Lucie : Oui, merci.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==112 :
        time.sleep(1)
        print("Lucie : Merci :)")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==105 :
        time.sleep(1)
        print("Léonard : Courage !")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==106 :
        time.sleep(1)
        print("Léonard : D'accord... Je suis là si besoin.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==107 :
        time.sleep(1)
        print("Léonard : Je ne suis pas là-dedans...")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==108 :
        time.sleep(1)
        print("Emma : Ah... pardon.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==109 :
        time.sleep(1)
        print("Emma : Bon bah j'te laisse. ")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==110 :
        time.sleep(1)
        print("Emma : Tu n'es qu'un connard.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==111 :
        time.sleep(1)
        print("Emma : Je l'aimais... je l'ai toujours aimé...")
        print("Mais quand il a avoué qu'il était PD, ça m'a dégouté. Alors j'ai juste voulu qu'il te quitte, mais je ne savais pas que ça irait jusque là...")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==112 :
        time.sleep(1)
        print("Stéphane : Tu n'es qu'un sombre connard.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==113 :
        time.sleep(1)
        print("Stéphane : Oui.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==114 :
        time.sleep(1)
        print("Stéphane : Tkt :)")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==115 :
        time.sleep(1)
        print("Stéphane : Bon je te laisse à ton deuiul. Toutes mes plus profondes condoléances.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==116 :
        time.sleep(1)
        print("Stéphane : Je pense qu'il est temps que je te laisse te reposer. Sache que tu as tout mon soutient dans cette terrible épreuve.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n==117 :
        time.sleep(1)
        print("Stéphane : C'est sa faute... Tu t'imagines, toi ?")
        print("Ton meilleur ami te dit qu'il est gay ?!")
        print("J'ai réagi comme n'importe quelle personne sensée.")
        time.sleep(1)
        print("Et puis s'il est mort c'est aussi à cause de toi, tu l'as perverti, j'en suis sûr. Avant de te rencontrer il était normal. S'il est mort c'est parce qu'il était faible, et aussi à cause de toi.")
        print(" ")
        print(" ")
        time.sleep(1)

    if n!=666 :
        print("<> Votre interlocuteur a quitté la conversation. <>")
        print(" ")
        print(" ")
        time.sleep(1)
        v=0

#