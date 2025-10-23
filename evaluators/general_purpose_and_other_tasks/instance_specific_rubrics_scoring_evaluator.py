"""
Instance Specific Rubrics Scoring Evaluator

Evaluates each item with its own custom rubric.
Unlike Rubrics Based Scoring (uniform rubric), this allows different rubrics per item.

Useful for heterogeneous datasets where different items need different evaluation criteria.
"""

from typing import Optional, Dict


class InstanceSpecificRubricsScoringEvaluator:
    """
    Instance Specific Rubrics Scoring metric evaluator.
    
    Applies custom rubrics to each item individually,
    enabling personalized evaluation criteria.
    """
    
    def __init__(self, llm=None):
        """
        Initialize Instance Specific Rubrics Scoring Evaluator.
        
        Args:
            llm: Language model for evaluation
        """
        self.llm = llm
    
    async def evaluate(self, sample):
        """
        Evaluate using instance-specific rubrics.
        
        Args:
            sample: Sample with:
                - response: Generated response
                - reference: Reference/ground truth
                - rubrics: Custom rubrics for this specific item
                    Example: {
                        'score0_description': '...',
                        'score1_description': '...'
                    }
        
        Returns:
            int: Score level
        """
        return await self._evaluate_with_instance_rubrics(sample)
    
    async def _evaluate_with_instance_rubrics(self, sample) -> int:
        """
        Evaluate response with instance-specific rubrics.
        
        Process:
        1. Extract item-specific rubrics from sample
        2. Present rubrics to LLM
        3. Request evaluation
        4. Return score
        
        Note: This differs from RubricsScore where all items share one rubric.
        """
        # Implementation using ragas.metrics.InstanceRubrics
        pass


def create_instance_specific_rubrics_scoring_evaluator(llm=None):
    """
    Factory function to create an Instance Specific Rubrics Scoring evaluator.
    
    Args:
        llm: Language model instance
    
    Returns:
        InstanceSpecificRubricsScoringEvaluator: Configured evaluator instance
    """
    return InstanceSpecificRubricsScoringEvaluator(llm=llm)
