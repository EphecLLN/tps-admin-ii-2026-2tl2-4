import requests
import json
import datetime

# Configuration
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:1.5b"
MAX_ITERATIONS = 3  # Garde-fou pour éviter les boucles infinies

# System Prompt structuré pour le mode Agent
messages = [
    {
        "role": "system", 
        "content": """Tu es un agent CRM autonome. Pour CHAQUE message, réponds UNIQUEMENT en JSON.
Actions disponibles :
- {"action": "GET_TIME"} : Pour obtenir l'heure actuelle.
- {"action": "SEARCH_CLIENT", "nom": "nom"} : Pour chercher un client dans la base.
- {"action": "RESPOND", "message": "texte"} : Pour donner ta réponse finale à l'utilisateur.

Procédure : Réfléchis étape par étape. Si tu as besoin d'une info, utilise l'action appropriée."""
    }
]

print("=== Agent ReAct CRM Démarré (HITL Activé) ===")

while True:
    user_input = input("\n[VOUS]: ")
    if user_input.lower() in ['quit', 'exit']:
        break

    messages.append({"role": "user", "content": user_input})
    
    # --- DÉBUT DE LA BOUCLE REACT ---
    it_count = 0
    final_answer_reached = False

    while it_count < MAX_ITERATIONS and not final_answer_reached:
        it_count += 1
        
        # Appel au LLM
        payload = {"model": MODEL, "messages": messages, "stream": False, "format": "json"}
        try:
            response = requests.post(OLLAMA_URL, json=payload).json()
            raw_reply = response["message"]["content"]
            data = json.loads(raw_reply)
            
            # 1. Cas : Demande d'outil (Action)
            if data["action"] in ["GET_TIME", "SEARCH_CLIENT"]:
                print(f"  [RÉFLEXION] L'agent veut exécuter : {data['action']}")
                
                # Validation Humaine (HITL)
                confirm = input(f"  [HITL] Autoriser l'action {data['action']} ? (y/n): ")
                if confirm.lower() != 'y':
                    print("  [STOP] Action refusée par l'utilisateur.")
                    break

                # Exécution de l'action
                resultat_outil = ""
                if data["action"] == "GET_TIME":
                    resultat_outil = datetime.datetime.now().strftime("%H:%M:%S")
                
                elif data["action"] == "SEARCH_CLIENT":
                    nom = data.get("nom", "")
                    with open("clients.csv", "r") as f:
                        found = [l.strip() for l in f if nom.lower() in l.lower()]
                        resultat_outil = " | ".join(found) if found else "Client introuvable."

                print(f"  [OBSERVATION] Résultat : {resultat_outil}")
                
                # On ajoute le résultat à l'historique et on reboucle
                messages.append({"role": "assistant", "content": raw_reply})
                messages.append({"role": "user", "content": f"[SYSTÈME] Résultat de l'action : {resultat_outil}. Continue."})

            # 2. Cas : Réponse Finale (Sortie de boucle)
            elif data["action"] == "RESPOND":
                print(f"\n[AGENT]: {data['message']}")
                messages.append({"role": "assistant", "content": raw_reply})
                final_answer_reached = True

        except Exception as e:
            print(f"  [ERREUR] : {e}")
            break
    
    if it_count >= MAX_ITERATIONS:
        print("  [LOG] Limite d'itérations atteinte pour cette question.")

# Fin du programme
