"""
Exact Match Evaluator

Checks if the generated response exactly matches the reference.
Returns 1 if exact match, 0 otherwise. Can be case-sensitive or insensitive.
"""

from typing import Optional


class ExactMatchEvaluator:
    """
    Exact Match metric evaluator.
    
    Binary metric: returns 1 for exact match, 0 for no match.
    """
    
    def __init__(self, case_sensitive: bool = False):
        """
        Initialize Exact Match Evaluator.
        
        Args:
            case_sensitive: Whether to perform case-sensitive matching
        """
        self.case_sensitive = case_sensitive
    
    async def evaluate(self, sample):
        """
        Evaluate exact match.
        
        Args:
            sample: Sample with:
                - response: Generated response
                - reference: Ground truth reference
        
        Returns:
            float: 1.0 if exact match, 0.0 otherwise
        """
        return await self._evaluate_match(sample)
    
    async def _evaluate_match(self, sample) -> float:
        """
        Evaluate exact match.
        
        Process:
        1. Normalize strings (lowercase if not case_sensitive)
        2. Compare for exact equality
        3. Return 1.0 or 0.0
        """
        pass


def create_exact_match_evaluator(case_sensitive: bool = False):
    """
    Factory function to create an Exact Match evaluator.
    
    Args:
        case_sensitive: Whether to be case-sensitive
    
    Returns:
        ExactMatchEvaluator: Configured evaluator instance
    """
    return ExactMatchEvaluator(case_sensitive=case_sensitive)
