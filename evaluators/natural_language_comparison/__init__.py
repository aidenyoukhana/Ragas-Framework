"""
Natural Language Comparison Metrics

Metrics for comparing natural language outputs:
- Factual Correctness: Claim-based accuracy evaluation
- Semantic Similarity: Embedding-based similarity
- Non-LLM String Similarity: Levenshtein distance (no LLM needed)
- BLEU Score: N-gram overlap metric
- ROUGE Score: Recall-oriented evaluation metric
- String Presence: Keyword/entity presence checking
- Exact Match: Binary exact match comparison
"""

from .factual_correctness_evaluator import create_factual_correctness_evaluator
from .semantic_similarity_evaluator import create_semantic_similarity_evaluator
from .nonllm_string_similarity_evaluator import create_nonllm_string_similarity_evaluator
from .bleu_score_evaluator import create_bleu_score_evaluator
from .rouge_score_evaluator import create_rouge_score_evaluator
from .string_presence_evaluator import create_string_presence_evaluator
from .exact_match_evaluator import create_exact_match_evaluator

__all__ = [
    "create_factual_correctness_evaluator",
    "create_semantic_similarity_evaluator",
    "create_nonllm_string_similarity_evaluator",
    "create_bleu_score_evaluator",
    "create_rouge_score_evaluator",
    "create_string_presence_evaluator",
    "create_exact_match_evaluator",
]
