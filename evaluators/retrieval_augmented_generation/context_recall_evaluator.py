"""
Context Recall Evaluator

Measures how many of the relevant documents (pieces of information) were successfully
retrieved. Context Recall focuses on not missing important results.

Available implementations:
- LLMContextRecall: Uses LLM to break down reference into claims
- NonLLMContextRecall: Uses string comparison metrics for similarity
- IDBasedContextRecall: Direct ID comparison

Formula:
    Context Recall = # of claims in reference supported by retrieved context / Total claims in reference

Or for ID-based:
    Context Recall = # reference context IDs found in retrieved context IDs / Total reference context IDs
"""

from typing import Optional


class ContextRecallEvaluator:
    """
    Context Recall metric evaluator.
    
    Measures how well the retriever captures all relevant information from the
    reference contexts. A high recall means fewer relevant documents were left out.
    """
    
    def __init__(self, llm=None, metric_type: str = "llm"):
        """
        Initialize Context Recall Evaluator.
        
        Args:
            llm: Language model for LLM-based evaluation
            metric_type: Type of metric to use:
                - 'llm': LLM-based claim decomposition
                - 'non_llm': Non-LLM string similarity
                - 'id_based': Direct ID comparison
        """
        self.llm = llm
        self.metric_type = metric_type
    
    async def evaluate(self, sample):
        """
        Evaluate context recall for a given sample.
        
        Args:
            sample: SingleTurnSample with:
                - user_input: The query
                - response: The generated response
                - retrieved_contexts: List of retrieved context chunks
                - reference: Reference answer or ground truth
                - reference_contexts (optional): List of reference contexts
                - retrieved_context_ids (optional): IDs of retrieved contexts
                - reference_context_ids (optional): IDs of reference contexts
        
        Returns:
            float: Recall score between 0 and 1
        """
        if self.metric_type == "llm":
            return await self._evaluate_llm(sample)
        elif self.metric_type == "non_llm":
            return await self._evaluate_non_llm(sample)
        elif self.metric_type == "id_based":
            return await self._evaluate_id_based(sample)
        else:
            raise ValueError(f"Unknown metric type: {self.metric_type}")
    
    async def _evaluate_llm(self, sample) -> float:
        """
        Evaluate using LLM-based claim decomposition.
        
        Process:
        1. Break reference into claims using LLM
        2. For each claim, check if it can be inferred from retrieved contexts
        3. Calculate: supported claims / total claims
        """
        # Implementation would use ragas.metrics.LLMContextRecall
        pass
    
    async def _evaluate_non_llm(self, sample) -> float:
        """
        Evaluate using non-LLM string similarity.
        
        Process:
        1. Use string similarity to compare retrieved contexts with reference contexts
        2. Count how many reference contexts are matched
        3. Calculate: # matched reference contexts / total reference contexts
        """
        # Implementation would use ragas.metrics.NonLLMContextRecall
        pass
    
    async def _evaluate_id_based(self, sample) -> float:
        """
        Evaluate using ID-based comparison.
        
        Process:
        1. Compare retrieved_context_ids with reference_context_ids
        2. Calculate: # of reference IDs found in retrieved IDs / total reference IDs
        """
        # Implementation would use ragas.metrics.IDBasedContextRecall
        pass


def create_context_recall_evaluator(llm=None, metric_type: str = "llm"):
    """
    Factory function to create a Context Recall evaluator.
    
    Args:
        llm: Language model instance
        metric_type: Type of evaluation metric to use
    
    Returns:
        ContextRecallEvaluator: Configured evaluator instance
    """
    return ContextRecallEvaluator(llm=llm, metric_type=metric_type)
