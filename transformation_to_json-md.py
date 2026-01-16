from grobid_client.grobid_client import GrobidClient
import os

# --- CONFIGURATION ---
INPUT_DIR = "./input_pdf"
OUTPUT_DIR = "./output_results"
SERVER_URL = "https://sciencialab-grobid-onnx.hf.space"

# Créer les dossiers si nécessaire
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def main():
    print("🚀 Démarrage du client Grobid...")

    # 1. Initialisation du client avec l'URL du serveur
    # On configure aussi un timeout généreux (60s) car le serveur public peut être lent
    client = GrobidClient(
        grobid_server=SERVER_URL, 
        batch_size=1000, 
        sleep_time=5, 
        timeout=60
    )

# 2. Lancement du traitement
# 2. Lancement du traitement
    client.process(
        service="processFulltextDocument", 
        input_path=INPUT_DIR,              
        output=OUTPUT_DIR,                 
        n=2,                               
        force=True,                        
        consolidate_header=True,           
        json_output=True,                  
        markdown_output=True               
    )

    print(f"\n✅ Traitement terminé ! Vérifie le dossier : {OUTPUT_DIR}")

if __name__ == "__main__":
    main()