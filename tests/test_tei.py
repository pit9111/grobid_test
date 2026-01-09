import pytest
from lxml import etree
import os

dossier_du_test = os.path.dirname(os.path.abspath(__file__))
fichier_xml = os.path.join(dossier_du_test, "..", "xml-tei", "test.pdf.tei.xml")

def test_verifier_si_texte_vide():
    # J'essaie de charger le fichier, si ça marche pas je fais échouer le test
    try:
        tree = etree.parse(fichier_xml)
        root = tree.getroot()
    except Exception as e:
        pytest.fail("Impossible de lire le fichier : " + str(e))
    
    # Il faut le namespace pour que lxml trouve les balises
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    node_text = root.find('.//tei:text', ns)
    
    # Je récupère tout le texte d'un coup
    contenu_complet = ""
    if node_text is not None:
        contenu_complet = "".join(node_text.itertext())

    print("Taille du texte récupéré : " + str(len(contenu_complet)))

    # Si c'est vide une fois les espaces enlevés, c'est une erreur
    assert contenu_complet.strip() != ""
