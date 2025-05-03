from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Facture</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Facture</h1>
    <p><strong>Client :</strong> watt</p>
    <p><strong>Prestation :</strong> gfdg</p>
    <p><strong>Coût unitaire :</strong> 350.00 €</p>


    <p><strong>Date :</strong> April 24, 2025, 8:27 p.m.</p>
    <h2>Total : 350.00 €</h2>
</body>
</html>
"""

try:
    HTML(string=html_content).write_pdf("test.pdf")
    print("PDF généré avec succès.")
except Exception as e:
    print(f"Erreur lors de la génération du PDF : {e}")