import requests
import json
import datetime

# Configuration
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:1.5b"

# Initialisation avec le System Prompt mis à jour pour le CRM
messages = [
    {
        "role": "system", 
        "content": """Tu es un assistant CRM. Pour CHAQUE message, réponds UNIQUEMENT en JSON valide.
Format si l'utilisateur veut l'heure              : {"action": "GET_TIME"}
Format si l'utilisateur parle d'un client         : {"action": "SEARCH_CLIENT", "nom": "nom ou mot-clé"}
Format pour toute autre réponse                   : {"action": "RESPOND", "message": "ta réponse"}"""
    }
]

print("=== Agent IA CRM (RAG par grep) Démarré ===")

while True:
    user_input = input("\nVous: ")
    if user_input.lower() in ['quit', 'exit']:
        break

    messages.append({"role": "user", "content": user_input})

    payload = {"model": MODEL, "messages": messages, "stream": False, "format": "json"}
    
    try:
        response = requests.post(OLLAMA_URL, json=payload).json()
        raw_reply = response["message"]["content"]
        messages.append({"role": "assistant", "content": raw_reply})

        data = json.loads(raw_reply)

        # CAS 1 : L'HEURE
        if data["action"] == "GET_TIME":
            heure = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"  [OUTIL] Heure → {heure}")
            messages.append({"role": "user", "content": f"[SYSTÈME] Heure : {heure}. Formule ta réponse en JSON."})
            
            res_heure = requests.post(OLLAMA_URL, json={"model": MODEL, "messages": messages, "stream": False, "format": "json"}).json()
            final_heure = json.loads(res_heure["message"]["content"])
            messages.append({"role": "assistant", "content": res_heure["message"]["content"]})
            print(f"\nAgent: {final_heure.get('message', final_heure)}")

        # CAS 2 : RECHERCHE CLIENT (RAG)
        elif data["action"] == "SEARCH_CLIENT":
            nom_recherche = data.get("nom", "")
            print(f"  [OUTIL] Recherche de '{nom_recherche}' dans clients.csv...")

            # Simulation d'un grep en Python
            resultat = "Client non trouvé."
            with open("clients.csv", "r") as f:
                lignes_trouvees = []
                for ligne in f:
                    if nom_recherche.lower() in ligne.lower():
                        lignes_trouvees.append(ligne.strip())
                
                if lignes_trouvees:
                    resultat = " | ".join(lignes_trouvees)

            # 🎯 COMPLÉTÉ (5) : Injection du contexte (Augmentation)
            # L'objectif est de donner la donnée brute au LLM pour qu'il l'interprète.
            messages.append({
                "role": "user",
                "content": f"[SYSTÈME - Résultat RAG] Infos trouvées : {resultat}. Formule ta réponse finale en JSON."
            })

            res_rag = requests.post(OLLAMA_URL, json={"model": MODEL, "messages": messages, "stream": False, "format": "json"}).json()
            final_rag = json.loads(res_rag["message"]["content"])
            messages.append({"role": "assistant", "content": res_rag["message"]["content"]})
            print(f"\nAgent: {final_rag.get('message', final_rag)}")

        # CAS 3 : RÉPONSE SIMPLE
        elif data["action"] == "RESPOND":
            print(f"\nAgent: {data['message']}")

    except Exception as e:
        print(f"  [⚠️ ERREUR] : {e} | Réponse brute : {raw_reply}")
