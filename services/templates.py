class Template:
    def __init__(self):
        self.map_linear = (
            f"""
        Écris en français un résumé structuré et détaillé du DOCUMENT délimité par des triples accents graves.
        N'invente rien : si le DOCUMENT est court avec moins de 60 mots, résume le en une seule phrase. 
        """
            + """DOCUMENT : ```{text}```"""
        )

        self.combine_linear = (
            f"""
        Écris en français un résumé structuré en paragraphes détaillés et faciles à retenir du DOCUMENT délimité par des triples accents graves.
        Assure-toi de garder le même ordre que le DOCUMENT, et d'éviter les redondances : ne répéte pas les mêmes idées si elles sont mentionnées plusieurs fois.
        N'ajoute aucune idée qui ne soit pas déjà dans le DOCUMENT.
        Si le DOCUMENT est court avec moins de 100 mots, résume-le en une seule phrase.
        S'il est plus long, assure-toi que ta réponse ait plusieurs paragraphes détaillés, en allant à la ligne entre chaque.
        Assure toi de ne pas répéter les mêmes idées.
        Assure-toi enfin de la cohérence globale et de l'articulation logique de ton résumé.
        """
            + """DOCUMENT : ```{text}```"""
        )

        self.analyse_linear = """
        Recopie le résumé du document entre triple accents graves, en gardant le même format en paragraphes. 
        Ajuste le à la marge, en t'assurant :
        - de la cohérence globale et de la non répétition des messages
        - de préciser les acronymes

        DOCUMENT : ```{text}```
        """

        self.map_key_insights = (
            f"""
        Extrais en français et détaille les idées clefs du DOCUMENT délimité par des triples accents graves, notamment les idées originales ou contre-intuitives, ou avec des statistiques.
        Présente et regroupe ces idées de façon structurée par bullet points et détaillée.
        Chaque bullet point (tiret) de ta réponse doit correspondre à une idée très détaillée.
        Ne répète pas des idées similaires.
        N'ajoute aucune idée qui ne soit pas déjà dans le document. 
        Et si le DOCUMENT est court avec moins de 60 mots, assure-toi de le résumer en une seule idée.
        """
            + """DOCUMENT : ```{text}```"""
        )

        self.collapse_key_insights = (
            f"""
        Le DOCUMENT délimité délimité par des triples accents graves présente des idées clefs.
        Hiérarchise et structure ces idées en quelques messages importants à retenir.
        Ne te répète pas : si des messages ou des idées sont similaires, fusionne-les.
        Si les idées sont illustrées par détails ou des chiffres, garde ces détails ou ces chiffres.
        N'ajoute aucune idée qui ne soit pas déjà dans le DOCUMENT.
        Et si le DOCUMENT est court avec moins de 60 mots, assure-toi de le résumer en une seule idée.
                                     
        Format de la réponse (en français, avec des numéros croissants) : 

        ### 1/ [précise le message à retenir en une phrase simple]
        * idée ou chiffre illustrant le message
        * idée ou chiffre illustrant le message
        ... 

        ...                             

        ### 2/ [précise le message à retenir en une phrase simple]
        * idée ou chiffre illustrant le message
        * idée ou chiffre illustrant le message
        ...                          

        ### n/ [précise le message à retenir en une phrase simple]
        * idée ou chiffre illustrant le message
        * idée ou chiffre illustrant le message
        """
            + """DOCUMENT : ```{text}```"""
        )

        self.combine_key_insights = (
            f"""
        Le DOCUMENT délimité délimité par des triples accents graves présente des idées clefs.
        Hiérarchise et structure ces idées détaillées en quelques messages importants à retenir.
        Ne te répète pas : si des messages ou des idées sont similaires, fusionne-les.
        Si les idées sont illustrées par détails ou des chiffres, garde ces détails ou ces chiffres.
        N'ajoute aucune idée qui ne soit pas déjà dans le DOCUMENT.
        Et si le DOCUMENT est court avec moins de 60 mots, assure-toi de le résumer en une seule idée.
                                     
        Format de la réponse (en français, avec des numéros croissants) : 

        ### 1/ [précise le message à retenir en une phrase simple]
        * idée ou chiffre illustrant le message
        * idée ou chiffre illustrant le message
        ... 

        ...                             

        ### 2/ [précise le message à retenir en une phrase simple]
        * idée ou chiffre illustrant le message
        * idée ou chiffre illustrant le message
        ...                          

        ### n/ [précise le message à retenir en une phrase simple]
        * idée ou chiffre illustrant le message
        * idée ou chiffre illustrant le message
        ...                              

        """
            + """DOCUMENT : ```{text}```"""
        )

        self.analyse_key_insights = """
        Recopie le résumé du document entre triple accents graves, en gardant le même format en markdown. 
        Ajuste le à la marge, en t'assurant :
        - de la cohérence globale et de la non répétition des messages clefs
        - de préciser les acronymes

        DOCUMENT : ```{text}```
        """

        self.HR_report = """Résume le document entre triples accents graves.
                          
        ```{text}```
        
        Formate impérativement ton résumé comme suit (insère le contenu pertinent entre les crochets)
        Si tu ne sais pas quoi mettre entre crochet, mets : Information non disponible.
        Note qu'il n'y a qu'un candidat : n'en propose pas plusieurs.
        
        ### Nom et Prénom du candidat
        [Nom et Prénom du candidat]
        
        ### Informations Générales :
        * Expérience : [Expérience]
        * Parcours et Objectifs de carrière : [Parcours et Objectifs de carrière]
        * Expertise technique : [Expertise technique]
        * Pourquoi changer d'entreprise : [Pourquoi changer d’entreprise]
        * Projection dans sa prochaine entreprise : [Projection dans sa prochaine entreprise]
        * Niveau d'anglais : [Niveau d'anglais]
        
        ### Aspects RH :
        * Disponibilité : [Disponibilité]
        * Prétentions salariales : [Prétentions salariales]
        * Autres process en cours : [Autres processus de recrutement en cours] 
        """

        self.contract = """Résume le contrat entre triples accents graves. Dans ce contrat, onepoint est le prestataire d'un client.
                          
        ```{text}```

        Note qu'il n'y a qu'un contrat : n'en propose pas plusieurs.
        Si certaines phrases disent qu'il n'y a pas d'information, et que d'autres ont une réponse, n'utilise que celles qui ont une réponse.
        Si aucune phrase n'a d'information, dit "Non mentionné dans le contrat". 

        Formate impérativement ton résumé comme suit.
        
        ### Client
        L'entreprise avec laquelle onepoint signe le contrat

        ### Objet du contrat
        Objet du contrat et principaux livrables
        
        ### Clauses clefs
        * <u>Confidentialité</u> : Clauses de confidentialité et éventuelle responsabilité en cas de manquement.
        * <u>Responsabilité</u> Quelle est la responsabilité de onepoint, est-elle plafonnée ? Quel est/sont ce(s) plafond(s) ?
        * <u>Pénalités</u> : Quelles sont les pénalités financières dues par onepoint, dans quel cas sont-elles prévues et avec quel plafond ? (Les pénalités pour retard de paiement ne sont pas dues par onepoint mais par le client et ne doivent pas être mentionnées ici)
        * <u>Non-sollicitation</u> : Les employés de onepoint peuvent-ils être débauchés par le client ? A quelles conditions ?
        * <u>Ogligation de résultat</u> : Onepoint a-t-elle une obligation de résultat ? Ou des 'obligations essentielles' à respecter ?
        * <u>Propriété intellectuelle</u> : À qui appartiennent les livrables ? Quelle propriété intellectuelle et droits d'utiliser les enseignements ou actifs créés lors de la mission conserve onepoint ?
        * <u>Montant</u> : Rémunération en euros ou dollars de la prestation ou coût de la prestation ou prix prévu par onepoint. Révision des prix en cas de contrat pluri-annuel
        * <u>Durée</u> : Durée de la mission. Dure-t-elle plusieurs mois ? Plusieurs années ?
        * <u>Exclusivité</u> : Y a-t-il une clause d'exclusivité empêchant onepoint de travailler avec d'autres clients ? Si oui, de quelle durée et est-elle rémunérée ?
        * <u>Sous-traitance</u> : La sous-traitance par le prestataire est-elle mentionnée ? est-elle encadrée ou interdite ?
        * <u>Données sensibles</u> : Le traitement de données sensibles (confidentiel défense, données médicales, raciales, religieuses, syndicales...), par onepoint est-il mentionné ? Si oui, qu'est-il prévu ?
        * <u>Données personnelles </u> : Le traitement de données personnelles par onepoint est-il mentionné ? Quel traitement est-il prévu ?
        * <u>Délais de paiement</u> : Délais dans lesquels l'entreprise contractant avec onepoint doit payer la rémunération de la prestation
        * <u>Résiliation</u> : Y-a-t-il une clause de résiliation ? Dans quelles conditions le client peut-il résilier ?
        * <u>Législation applicable</u> : Quel est le droit pertinent, français ou celui d'un autre pays ?
        
        """

        self.analyse_contract = """
        Les éléments problématiques sont les éléments du contrat entre triples accents graves pour lesquels les BONNES PRATIQUES entre triples ùùù ne sont pas respectées. 
        Les éléments conformes sont les éléments du contrat pour lesquels les BONNES PRATIQUES sont respectées.
        BONNES PRATIQUES : 
        ùùù
        - Responsabilité : La responsabilité de onepoint est bien plafonnée et ce plafond est inférieur au minimum entre 2 fois le montant total du contrat (c'est à dire de la prestation) et le plafond de garantie couvert par le contrat de responsabilité civile de onepoint. Il n'y a pas de plafond de responsabilité spécifique sur un domaine précis.
        - Pénalités : Il n'y a pas de pénalités spécifique. Le montant cumulé des pénalités est inférieur à 5% du montant du contrat
        - Obligation de résultat : Le contrat ne mentionne pas d'obligation de résultat ou d'"obligation essentielle" (il ne faut pas que ces obligations soient mentionnées car elles sont difficiles à respecter et peuvent mettre onepoint à risque, en particulier une obligation essentielle).
        - Non sollicitation : Le contrat comporte une clause de non sollicitation empêchant le client de débaucher sans indemnité les salariés de onepoint.
        - Propriété intellectuelle : Onepoint conserve la propriété intellectuelle sur ses méthodologies ou actifs préexistants au contrat et le droit d'utiliser les enseignements ou actifs créés lors de la mission.
        - Données sensibles : Le contrat ne mentionne pas le traitement de données sensibles (confidentiel défense, données personnelles médicales, biométriques, raciales ou ethnique, religieuses, appartenance syndicale...). 
        - Données personnelles : Le contrat ne mentionne pas de traitement de données personnelles. Si c'est le cas, il faut s'assurer que la fiche de traitement est détaillée (en cas de doute il faut contacter le Data Protection Officer de onepoint à qsc@groupeonepoint.com).
        - Législation applicable : La législation applicable est le droit français.
        - Exclusivité : Le contrat ne mentionne pas de clause d'exclusivité (il ne faut pas que cette clause soit mentionnée car cela empêcherait onepoint de travailler librement avec d'autres clients). 
        - Sous-traitance : Le contrat ne mentionne pas ou ne restreint pas la sous-traitance par le prestataire (il vaut mieux que cette clause ne soit pas mentionnée, ce qui permet à onepoint de sous traiter librement).
        - Révision des prix : Le contrat ne porte que sur une mission de quelque mois, ou s'il il est pluri-annuel il y a une clause de révision des prix.
        ùùù
                  
        CONTRAT : ```{text}```

        Le format de ta réponse doit être comme suit : 
        ### Points de vigilance
        - <span style="color:red;">élément problématique </span>
        ...

        """
