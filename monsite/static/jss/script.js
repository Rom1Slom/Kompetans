document.addEventListener('DOMContentLoaded', () => {
    let currentPhraseNumber = 1; // Initialisation

    function changerPhrase(direction) {
        console.log("Direction choisie :", direction);
    
        // Validation de la direction
        if (direction !== "next" && direction !== "previous") {
            console.error("Direction invalide :", direction);
            return;
        }
    
        // Calcul du numéro de la prochaine phrase
        const newPhraseNumber = direction === "next" ? currentPhraseNumber + 1 : currentPhraseNumber - 1;
    
        // Empêcher une navigation hors limites
        if (newPhraseNumber < 1) {
            alert("Vous êtes déjà à la première phrase.");
            return;
        }
    
        console.log("Requête pour la phrase numéro :", newPhraseNumber);
    
        // Requête pour la nouvelle phrase
        fetch(`/traduction/?current_phrase_number=${newPhraseNumber}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP : ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('phrase').innerText = data.phrase;
            document.getElementById('traduction').innerText = data.translation_fr;
            currentPhraseNumber = data.current_phrase_number;
    
            // Désactiver les boutons si nécessaire
            document.getElementById('previous-button').disabled = data.is_first;
            document.getElementById('next-button').disabled = data.is_last;
        })
        .catch(error => {
            console.error(`Erreur lors de la récupération de la phrase (${direction}):`, error);
            alert(`Erreur lors du chargement de la phrase : ${error.message}`);
        });
    }
    
    

    function afficherTraduction() {
        // Utilisation du numéro de phrase actuel
        fetch(`/traduction/${currentPhraseNumber}/`)
            .then(response => {
                if (!response.ok) throw new Error(`Erreur HTTP: ${response.status}`);
                return response.json();
            })
            .then(data => {
                document.getElementById('traduction').innerText = data.traduction;
            })
            .catch(error => {
                console.error("Erreur lors de la récupération de la traduction :", error);
                alert(`Erreur: ${error.message}`);
            });
    }

    // Attach event handlers aux boutons
    window.phraseSuivante = () => {
        document.getElementById('next-button').disabled = true;
        changerPhrase("next").finally(() => {
            document.getElementById('next-button').disabled = false;
        })
    };
    window.phrasePrecedente = () => changerPhrase("previous");
    window.afficherTraduction = afficherTraduction;
});
