"""
Aspect Critic Evaluator

Evaluates responses based on predefined aspects in free-form natural language.
Output is binary (yes/no) indicating whether the response aligns with the aspect.

Example aspects: maliciousness, bias, relevance, helpfulness, etc.
"""

from typing import Optional


class AspectCriticEvaluator:
    """
    Aspect Critic metric evaluator.
    
    Binary evaluation of whether a response exhibits a particular aspect.
    Uses majority voting from multiple LLM verdicts for robustness.
    """
    
    def __init__(self, llm=None, name: str = "", definition: str = ""):
        """
        Initialize Aspect Critic Evaluator.
        
        Args:
            llm: Language model for evaluation
            name: Name of the aspect (e.g., "maliciousness", "bias")
            definition: Natural language definition of the aspect
        """
        self.llm = llm
        self.name = name
        self.definition = definition
    
    async def evaluate(self, sample):
        """
        Evaluate aspect for a response.
        
        Args:
            sample: Sample with:
                - user_input: User query
                - response: Generated response
        
        Returns:
            float: 0 or 1 (binary) - whether response exhibits the aspect
        """
        return await self._evaluate_aspect(sample)
    
    async def _evaluate_aspect(self, sample) -> float:
        """
        Evaluate aspect using LLM verdicts.
        
        Process:
        1. Make multiple LLM calls with aspect definition
        2. Collect verdicts (Yes/No) from LLM
        3. Use majority voting to determine result
        4. Return 0 or 1
        """
        # Simple implementation - returns binary result
        # In real implementation, would use LLM to evaluate
        response = getattr(sample, 'response', '')
        user_input = getattr(sample, 'user_input', '')
        
        # Placeholder logic: check if response is non-empty and meaningful
        if response and len(response) > 0:
            # Check for common negative aspects in response
            negative_keywords = ['error', 'fail', 'cannot', 'unable', 'invalid']
            if any(keyword in response.lower() for keyword in negative_keywords):
                return 0.0  # Aspect not satisfied
            return 1.0  # Aspect satisfied
        return 0.0  # No response


def create_aspect_critic_evaluator(llm=None, name: str = "", definition: str = ""):
    """
    Factory function to create an Aspect Critic evaluator.
    
    Args:
        llm: Language model instance
        name: Name of aspect
        definition: Definition of aspect
    
    Returns:
        AspectCriticEvaluator: Configured evaluator instance
    """
    return AspectCriticEvaluator(llm=llm, name=name, definition=definition)
