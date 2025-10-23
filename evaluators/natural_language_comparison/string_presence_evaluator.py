"""
String Presence Evaluator

Checks if specific strings or keywords from the reference
are present in the generated response.

This is a simple but effective metric for verifying presence
of important terms or phrases.
"""

from typing import Optional, List


class StringPresenceEvaluator:
    """
    String Presence metric evaluator.
    
    Evaluates whether important strings/keywords from reference
    are present in the response.
    """
    
    def __init__(self):
        """
        Initialize String Presence Evaluator.
        """
        pass
    
    async def evaluate(self, sample):
        """
        Evaluate string presence.
        
        Args:
            sample: Sample with:
                - response: Generated response
                - reference: Reference text/keywords
        
        Returns:
            float: Score (0 to 1) based on string coverage
        """
        return await self._evaluate_presence(sample)
    
    async def _evaluate_presence(self, sample) -> float:
        """
        Evaluate presence of reference strings in response.
        
        Process:
        1. Extract important strings/entities from reference
        2. Check presence in response
        3. Calculate: # present strings / total strings
        """
        pass


def create_string_presence_evaluator():
    """
    Factory function to create a String Presence evaluator.
    
    Returns:
        StringPresenceEvaluator: Configured evaluator instance
    """
    return StringPresenceEvaluator()
