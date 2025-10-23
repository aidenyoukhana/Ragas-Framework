"""
Non-LLM String Similarity Evaluator

Measures string similarity using traditional NLP metrics like Levenshtein distance,
without requiring an LLM. Fast and efficient for simple string comparisons.

Requires: rapidfuzz package
"""

from typing import Optional


class NonLLMStringSimilarityEvaluator:
    """
    Non-LLM String Similarity metric evaluator.
    
    Uses string matching algorithms (Levenshtein distance, etc.)
    for similarity calculation without LLM calls.
    """
    
    def __init__(self):
        """
        Initialize Non-LLM String Similarity Evaluator.
        Requires: pip install rapidfuzz
        """
        pass
    
    async def evaluate(self, sample):
        """
        Evaluate string similarity.
        
        Args:
            sample: Sample with:
                - response: Generated response
                - reference: Ground truth reference
        
        Returns:
            float: Similarity score (0 to 1)
        """
        return await self._evaluate_similarity(sample)
    
    async def _evaluate_similarity(self, sample) -> float:
        """
        Evaluate string similarity using non-LLM methods.
        
        Process:
        1. Use Levenshtein distance or similar metric
        2. Normalize to 0-1 range
        3. Return similarity score
        """
        # Implementation using rapidfuzz
        pass


def create_nonllm_string_similarity_evaluator():
    """
    Factory function to create a Non-LLM String Similarity evaluator.
    
    Returns:
        NonLLMStringSimilarityEvaluator: Configured evaluator instance
    """
    return NonLLMStringSimilarityEvaluator()
