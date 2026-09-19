"""
Deep Learning Embedding & Semantic Analysis Engine using Sentence-Transformers.
Provides contextual dense vector embeddings (all-MiniLM-L6-v2) for resumes,
job descriptions, and career roles. Automatically falls back to Scikit-Learn TF-IDF
if PyTorch/SentenceTransformers is not available.
"""

import os
from typing import Optional, List, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

_MODEL = None
_MODEL_NAME = "all-MiniLM-L6-v2"
_TRIED_LOADING = False

def get_sentence_transformer_model():
    """
    Lazy loader for SentenceTransformer model singleton.
    Loads the lightweight all-MiniLM-L6-v2 model on first demand.
    """
    global _MODEL, _TRIED_LOADING
    if _MODEL is not None:
        return _MODEL
    if _TRIED_LOADING:
        return None

    _TRIED_LOADING = True
    try:
        from sentence_transformers import SentenceTransformer
        _MODEL = SentenceTransformer(_MODEL_NAME)
        print(f"[ML ENGINE] SentenceTransformer loaded successfully: {_MODEL_NAME}")
        return _MODEL
    except Exception as e:
        print(f"[ML ENGINE] Notice: SentenceTransformer unavailable ({e}). Using Scikit-Learn TF-IDF.")
        return None

def is_deep_learning_active() -> bool:
    """Returns True if the SentenceTransformer deep learning model is loaded."""
    model = get_sentence_transformer_model()
    return model is not None

def calculate_deep_semantic_similarity(text1: str, text2: str) -> Tuple[float, str]:
    """
    Computes contextual cosine similarity between two texts.
    Returns:
        (similarity_score: float [0.0 - 1.0], engine_name: str)
    """
    if not text1.strip() or not text2.strip():
        return 0.0, "None"

    model = get_sentence_transformer_model()
    if model is not None:
        try:
            # Generate 384-dimensional dense contextual embeddings
            embeddings = model.encode(
                [text1[:4000], text2[:4000]],
                convert_to_numpy=True,
                normalize_embeddings=True
            )
            # Dot product of normalized vectors = Cosine Similarity
            sim = float(np.dot(embeddings[0], embeddings[1]))
            return float(np.clip(sim, 0.0, 1.0)), f"Sentence-Transformers ({_MODEL_NAME})"
        except Exception as err:
            print(f"[ML ENGINE] SentenceTransformer inference failed: {err}. Falling back to TF-IDF.")

    # Fallback to Scikit-Learn TF-IDF Cosine Similarity
    try:
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1500)
        tfidf = vectorizer.fit_transform([text1, text2])
        sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return float(np.clip(sim, 0.0, 1.0)), "Scikit-Learn TF-IDF"
    except Exception:
        return 0.35, "Fallback Baseline"
