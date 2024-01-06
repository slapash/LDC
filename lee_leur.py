import random

import time


clubs = {
    "Real Madrid": {"pays": "Espagne", "favori": False, "cote": 1},
    "Bayern": {"pays": "Allemagne", "favori": False, "cote": 1},
    "Arsenal": {"pays": "Angleterre", "favori": False, "cote": 1},
    "Barcelona": {"pays": "Espagne", "favori": False, "cote": 1},
    "Manchester City": {"pays": "Angleterre", "favori": False, "cote": 1},
    "PSG": {"pays": "France", "favori": False, "cote": 1},
    "Napoli": {"pays": "Italie", "favori": False, "cote": 1},
    "AC Milan": {"pays": "Italie", "favori": False, "cote": 1},
    "Athletico Madrid": {"pays": "Espagne", "favori": False, "cote": 1},
    "Dortmund": {"pays": "Allemagne", "favori": False, "cote": 1},
    "Inter Milan": {"pays": "Italie", "favori": False, "cote": 1},
    "Antwerp": {"pays": "Belgique", "favori": False, "cote": 1},
    "Benfica": {"pays": "Portugal", "favori": False, "cote": 1},
    "Braga": {"pays": "Portugal", "favori": False, "cote": 1},
    "Celtic": {"pays": "Ecosse", "favori": False, "cote": 1},
    "Copenhagen": {"pays": "Danemark", "favori": False, "cote": 1},
    "Crvena Zvezda": {"pays": "Serbie", "favori": False, "cote": 1},
    "FC Porto": {"pays": "Portugal", "favori": False, "cote": 1},
    "Feyenoord": {"pays": "Pays Bas", "favori": False, "cote": 1},
    "Galatasaray": {"pays": "Turquie", "favori": False, "cote": 1},
    "Lazio": {"pays": "Italie", "favori": False, "cote": 1},
    "Leipzig": {"pays": "Allemagne", "favori": False, "cote": 1},
    "Lens": {"pays": "France", "favori": False, "cote": 1},
    "Manchester United": {"pays": "Angleterre", "favori": False, "cote": 1},
    "Servette": {"pays": "Suisse", "favori": False, "cote": 1},
    "Newcastle": {"pays": "Angleterre", "favori": False, "cote": 1},
    "PSV": {"pays": "Pays Bas", "favori": False, "cote": 1},
    "Real Sociedad": {"pays": "Espagne", "favori": False, "cote": 1},
    "Salzburg": {"pays": "Autriche", "favori": False, "cote": 1},
    "Sevilla": {"pays": "Espagne", "favori": False, "cote": 1},
    "Shakhtar Donetsk": {"pays": "Ukraine", "favori": False, "cote": 1},
    "Union Berlin": {"pays": "Allemagne", "favori": False, "cote": 1},
}


favoris = [
    "Real Madrid",
    "Bayern",
    "Arsenal",
    "Barcelona",
    "Manchester City",
    "PSG",
    "AC Milan",
    "Athletico Madrid",
    "Inter Milan",
]


def placer_clubs():

    groupes = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
    }  # on crée des groupes vide

    clubs_liste = list(clubs.keys())  # on crée une liste avec tous les clubs du dico

    random.shuffle(clubs_liste)  # on les melange de facon aléatoire

    for club in clubs_liste:

        pays = clubs[club]["pays"]  # pays prend la valeur de pays dans le diccionnaire

        groupe_choisi = None  # on crée groupe_choisi qui est vide pour le moment (None)

        while (
            groupe_choisi is None
        ):  # vérifie si la variable groupe_choisi n'a pas encore été assignée

            for (
                groupe
            ) in (
                groupes
            ):  # on vérifie si le groupe a moins de 4 clubs et que le pays du club n'est pas déjà présent dans le groupe

                if len(groupes[groupe]) < 4 and all(
                    clubs[autre_club]["pays"] != pays for autre_club in groupes[groupe]
                ):  # all() est une foncion qui renvoie true si tout est respecté, sinon false

                    groupe_choisi = groupe  # groupe_choisi= le nombre de groupes

                    groupes[groupe_choisi].append(
                        club
                    )  # on ajoute club a groupes (autant de fois que groupe_choisi)

                    break  # si condition respecter, fin de la boucle

            else:

                random.shuffle(
                    clubs_liste
                )  # sinon on re melange et on recommence la boucle while

    return groupes  # renvoi les groupes


def rajouter_cote(
    equipe, cote, est_favori=False, joue_a_domicile=False
):  # est_favorie et joue_a_domicile sont false par defaut

    if est_favori:

        cote += 0.2  # 1,00 + 0,2 si l'equipe est favori (et pas à domicile)

    if joue_a_domicile:

        cote += 0.1  # 1,00 + 0,1 si l'equipe joue a domicile

    return cote  # renvoi les cotes


def simuler_match(equipe_domicile, equipe_exterieur):

    cote_domicile = rajouter_cote(
        equipe_domicile,
        clubs[equipe_domicile]["cote"],
        equipe_domicile in favoris,
        True,
    )  # calcul les cotes à domicile + favoris

    cote_exterieur = rajouter_cote(
        equipe_exterieur,
        clubs[equipe_exterieur]["cote"],
        equipe_exterieur in favoris,
        False,
    )  # calcul les cotes à l'exterieur + favoris

    score_domicile = min(
        random.randint(0, 4), 4
    )  # simule match, but allant de 1 à 4, max 4, aleatoir mais nb entier (randint)

    score_exterieur = min(
        random.randint(0, 4), 4
    )  # meme chose pour l'exterieur/ la fonction min() garanti que ca ne depasse pas 4

    if score_domicile > score_exterieur:  # si score domicile > score exterieur

        return (
            "Victoire domicile",
            cote_domicile,
            cote_exterieur,
        )  # renvoi "victoire domicile", la cote a dom et la cote à l'ext

    elif score_domicile < score_exterieur:  # meme chose avec l'inverse

        return "Victoire exterieur", cote_domicile, cote_exterieur

    else:

        return "Match nul", cote_domicile, cote_exterieur  # meme chose avec match nul


def enregistrer_resultat(
    resultats, groupe, equipe_dom, equipe_ext, resultat, cote_dom, cote_ext
):

    if resultat == "Victoire domicile":

        resultats[groupe]["classement"][equipe_dom][
            "points"
        ] += 3  # si victoire à dom +3 pts au classement a l'equipe à dom

    elif resultat == "Match nul":

        resultats[groupe]["classement"][equipe_dom][
            "points"
        ] += 1  # si match nul +1 pts au classement à l'equipe dom

        resultats[groupe]["classement"][equipe_ext][
            "points"
        ] += 1  # si match nul +1 pts au classement à l'equipe ext

    else:

        resultats[groupe]["classement"][equipe_ext][
            "points"
        ] += 3  # si victoire à ext +3 pts au classement à l'equipe ext

    # .2f-> veut dire qu'il y a 2 chiffres après la virgule et que c'est un float

    print(
        f"{equipe_dom} (cote: {cote_dom:.2f}) {random.randint(0, 4)} - {random.randint(0, 4)} {equipe_ext} (cote: {cote_ext:.2f})"
    )  # print les infos du match

    time.sleep(0.1)  # les resultats sont affichés avecune interval d'une seconde


def organiser_classement(groupes):

    resultats = {}  # resultat vide pour le moment

    for groupe, equipes in groupes.items():

        resultats[groupe] = {"classement": {}}

        for equipe in equipes:

            resultats[groupe]["classement"][equipe] = {
                "points": 0
            }  # classement se forme avec le nombre de point re inisialiser à 0

        for i in range(len(equipes)):

            for j in range(i + 1, len(equipes)):

                equipe_domicile = equipes[i]

                equipe_exterieur = equipes[j]

                # permet de jouer le match aller

                resultat_aller, cote_aller, cote_retour = simuler_match(
                    equipe_domicile, equipe_exterieur
                )

                enregistrer_resultat(
                    resultats,
                    groupe,
                    equipe_domicile,
                    equipe_exterieur,
                    resultat_aller,
                    cote_aller,
                    cote_retour,
                )

                # permet de jouer le match retour

                resultat_retour, cote_retour, _ = simuler_match(
                    equipe_exterieur, equipe_domicile
                )

                enregistrer_resultat(
                    resultats,
                    groupe,
                    equipe_exterieur,
                    equipe_domicile,
                    resultat_retour,
                    cote_retour,
                    cote_aller,
                )

    return resultats  # renvoi resultats


def afficher_resultats(resultats):

    for groupe, data in resultats.items():

        print(f" \n Groupe {groupe}:")

        classement = sorted(
            data["classement"].items(), key=lambda x: x[1]["points"], reverse=True
        )  # cette ligne permet de faire en sorte que les equipes soient mis dans l'ordre selon les points

        for position, (equipe, stats) in enumerate(
            classement, start=1
        ):  # met la position des equipes allant de 1 à 4

            time.sleep(0.1)

            print(
                f"{position}. {equipe}: {stats['points']} points"
            )  # print le classement


# exécution des groupes/des classements/des matchs

groupes = placer_clubs()

resultats_matchs = organiser_classement(groupes)

afficher_resultats(resultats_matchs)


# on commence par transformer les groupes en listes

liste_equipes_groupes = [
    groupes["A"],
    groupes["B"],
    groupes["C"],
    groupes["D"],
    groupes["E"],
    groupes["F"],
    groupes["G"],
    groupes["H"],
]


# on prend les équipes qualifiées de chaque groupe

equipes_qualifiees = {}

for groupe, equipes in zip(
    "ABCDEFGH", liste_equipes_groupes
):  # la fonction "zip" forme des tuples entre le groupe et les equipes

    classement_groupe = sorted(
        resultats_matchs[groupe]["classement"].items(),
        key=lambda x: x[1]["points"],
        reverse=True,
    )  # resultats_matchs[groupe]['classement'] accede au classement/.items  transforme le dictionnaire des classements en une séquence de paires clé-valeur (items)/lambda x: x[1]['points'] prend un tuple x (une équipe+ son classement) et retourne la valeur du nombre de points de cette équipe.(x[1 est le deuxieme element)/sorted indique comment trier les éléments de la séquence (les équipes) en fonction du nombre de points de manière décroissante.

    equipes_qualifiees[groupe] = [
        equipe for equipe, _ in classement_groupe[:2]
    ]  # crée une liste contenant les deux premiers du groupe


# maintenant on forme "les paires" des matchs pour les huitièmes de finale

huitiemes_de_finale = []

for i in range(0, 4):  # 4 fois

    # les clubs des groupes A,B,C,D jouent toujours contre un du groupe E,F,G,H (pour eviter confusions)

    match_1 = (
        equipes_qualifiees[chr(65 + i)][0],
        equipes_qualifiees[chr(65 + i + 4)][1],
    )  # le premier du groupe A,B,C,D joue contre un deuxieme du E,F,G,H

    match_2 = (
        equipes_qualifiees[chr(65 + i + 4)][0],
        equipes_qualifiees[chr(65 + i)][1],
    )  # le premier du groupe E,F,G,H joue contre un deuxieme du groupe A,B,C,D

    huitiemes_de_finale.extend([match_1, match_2])  # ajoute tous les pairs de matchs


# si on veut affiche les paires de matchs des huitièmes de finale mais pas besoin

"""print("\n------------ Huitièmes de finale -------------- \n")

for match in huitiemes_de_finale:

    print(match)"""


def simuler_match(equipe_domicile, equipe_exterieur):

    # Calcule les cotes des équipes

    cote_domicile = rajouter_cote(
        equipe_domicile,
        clubs[equipe_domicile]["cote"],
        equipe_domicile in favoris,
        True,
    )

    cote_exterieur = rajouter_cote(
        equipe_exterieur,
        clubs[equipe_exterieur]["cote"],
        equipe_exterieur in favoris,
        False,
    )

    # Limite le score à un maximum de 4 buts

    score_domicile = min(random.randint(0, 4), 4)

    score_exterieur = min(random.randint(0, 4), 4)

    # Détermine le résultat du match

    if score_domicile > score_exterieur:

        resultat = "Victoire domicile"

    elif score_domicile < score_exterieur:

        resultat = "Victoire exterieur"

    else:

        resultat = "Match nul"

    return resultat, cote_domicile, cote_exterieur, score_domicile, score_exterieur


def simuler_huitiemes_de_finale(matchs_huitiemes):

    resultats_huitiemes = []

    for equipe_dom, equipe_ext in matchs_huitiemes:

        # Simule le match aller

        (
            resultat_aller,
            cote_aller_dom,
            cote_aller_ext,
            score_aller_dom,
            score_aller_ext,
        ) = simuler_match(equipe_dom, equipe_ext)

        # Simule le match retour

        (
            resultat_retour,
            cote_retour_dom,
            cote_retour_ext,
            score_retour_dom,
            score_retour_ext,
        ) = simuler_match(equipe_ext, equipe_dom)

        # Calcule le score cumulé

        score_cumule_dom = score_aller_dom + score_retour_dom

        score_cumule_ext = score_aller_ext + score_retour_ext

        # Ajoute les résultats à la liste

        resultats_huitiemes.append(
            (
                equipe_dom,
                equipe_ext,
                ("Aller", score_aller_dom, score_aller_ext),
                ("Retour", score_retour_dom, score_retour_ext),
                ("Cumul", score_cumule_dom, score_cumule_ext),
            )
        )

    return resultats_huitiemes


# Exécution des huitièmes de finale

resultats_huitiemes = simuler_huitiemes_de_finale(huitiemes_de_finale)


# Affiche les résultats des huitièmes de finale

print("\n------------ Résultats Huitièmes de finale -------------- \n")

for resultat in resultats_huitiemes:

    print(f"     {resultat[0]} vs {resultat[1]}:")

    for type_match, score_dom, score_ext in resultat[2:]:

        cote_dom = rajouter_cote(
            resultat[0], clubs[resultat[0]]["cote"], resultat[0] in favoris, True
        )

        cote_ext = rajouter_cote(
            resultat[1], clubs[resultat[1]]["cote"], resultat[1] in favoris, False
        )

        print(
            f"{type_match}: {resultat[0]} (cote: {cote_dom:.2f}) {score_dom} - {score_ext} {resultat[1]} (cote: {cote_ext:.2f}) \n ",
            end="",
        )

        time.sleep(0.1)

    print("\n")
