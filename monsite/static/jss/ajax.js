document.addEventListener('DOMContentLoaded', function() 
// La ligne ci-dessus attend le chargement de la page HTML pour exécuter la fonction à l'intérieur
{
    document.getElementById('myButton').addEventListener('click', function() {
        fetch('ajax/')
        // la ligne ci-dessus envoie une requête HTTP à l'URL ajax/
            .then(response => response.json())
            // Une fois la réponse reçue, on convertit en json. 
            .then(data => {
                document.getElementById('message').innerText = data.message;
            });
    });
});
 