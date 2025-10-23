"""
Context Entities Recall Evaluator

Measures the recall of entities (named entities, facts, etc.) retrieved from the
reference contexts. This metric is useful for fact-based use cases like tourism QA,
historical QA, etc.

Formula:
    Context Entity Recall = # of common entities (RCE ∩ RE) / Total # of entities in reference (RE)

Where:
    RE = Set of entities in reference
    RCE = Set of entities in retrieved contexts
"""

from typing import Optional


class ContextEntitiesRecallEvaluator:
    """
    Context Entities Recall metric evaluator.
    
    Measures what fraction of entities from the reference are successfully recalled
    in the retrieved contexts. Useful for fact-based evaluation where entities matter.
    """
    
    def __init__(self, llm=None):
        """
        Initialize Context Entities Recall Evaluator.
        
        Args:
            llm: Language model for entity extraction
        """
        self.llm = llm
    
    async def evaluate(self, sample):
        """
        Evaluate context entities recall for a given sample.
        
        Args:
            sample: SingleTurnSample with:
                - reference: Reference text containing entities
                - retrieved_contexts: List of retrieved context chunks
        
        Returns:
            float: Entity recall score between 0 and 1
        """
        return await self._evaluate_entities(sample)
    
    async def _evaluate_entities(self, sample) -> float:
        """
        Evaluate entity recall.
        
        Process:
        1. Extract entities from reference using LLM/NER
        2. Extract entities from retrieved contexts
        3. Find common entities
        4. Calculate: # common entities / # reference entities
        """
        # Implementation would use ragas.metrics.ContextEntityRecall
        pass


def create_context_entities_recall_evaluator(llm=None):
    """
    Factory function to create a Context Entities Recall evaluator.
    
    Args:
        llm: Language model instance for entity extraction
    
    Returns:
        ContextEntitiesRecallEvaluator: Configured evaluator instance
    """
    return ContextEntitiesRecallEvaluator(llm=llm)
