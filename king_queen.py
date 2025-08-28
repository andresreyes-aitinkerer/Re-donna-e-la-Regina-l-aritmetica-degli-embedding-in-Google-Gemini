from google import genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from definitions import king_defs, man_defs, woman_defs, def_candidates

# Inizializza il client
client = genai.Client(api_key="<API KEY>")

def emb(txt: str) -> np.ndarray:
    r = client.models.embed_content(model="gemini-embedding-001", contents=txt)
    return np.array(r.embeddings[0].values, dtype=np.float64)

def emb_mean(texts: list[str]) -> np.ndarray:
    V = np.stack([emb(t) for t in texts], axis=0)
    return V.mean(axis=0)

def cos(a, b) -> float:
    return float(cosine_similarity([a],[b])[0][0])


# Vettori medi
v_king    = emb_mean(king_defs)
v_man  = emb_mean(man_defs)
v_woman = emb_mean(woman_defs)

# Analogia
v_result = v_king - v_man + v_woman


# Scoring e ranking
scores = []
for w, defs in def_candidates.items():
    v = emb_mean(defs)
    scores.append((w, cos(v_result, v)))

scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)

print("Ranking (re - uomo + donna):")
for w, s in scores_sorted:
    print(f"{w:12s} {s:.4f}")