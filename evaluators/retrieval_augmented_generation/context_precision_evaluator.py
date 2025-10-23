"""
Context Precision Evaluator

Evaluates the retriever's ability to rank relevant chunks higher than irrelevant ones.
Context Precision assesses the degree to which relevant chunks in the retrieved context
are placed at the top of the ranking.

Available implementations:
- LLMContextPrecisionWithoutReference: Uses LLM to compare each chunk with response
- LLMContextPrecisionWithReference: Uses LLM to compare each chunk with reference
- NonLLMContextPrecisionWithReference: Uses non-LLM similarity measures (requires rapidfuzz)
- IDBasedContextPrecision: Compares context IDs directly

Formula:
    Context Precision@K = ∑(k=1 to K) [Precision@k × v_k] / Total number of relevant items in top K

Where:
    K = total number of chunks in retrieved_contexts
    v_k ∈ {0,1} = relevance indicator at rank k
    Precision@k = true positives@k / (true positives@k + false positives@k)
"""

from typing import Optional


class ContextPrecisionEvaluator:
    """
    Context Precision metric evaluator.
    
    Measures how precisely the retriever ranks relevant documents, focusing on
    whether relevant chunks appear at the top of the ranking rather than being
    mixed with irrelevant results.
    """
    
    def __init__(self, llm=None, embeddings=None, metric_type: str = "llm_without_reference"):
        """
        Initialize Context Precision Evaluator.
        
        Args:
            llm: Language model for LLM-based evaluation
            embeddings: Embeddings model for similarity calculations
            metric_type: Type of metric to use:
                - 'llm_without_reference': LLM comparison with response only
                - 'llm_with_reference': LLM comparison with reference
                - 'non_llm': Non-LLM string similarity (requires rapidfuzz)
                - 'id_based': Direct ID comparison
        """
        self.llm = llm
        self.embeddings = embeddings
        self.metric_type = metric_type
    
    async def evaluate(self, sample):
        """
        Evaluate context precision for a given sample.
        
        Args:
            sample: SingleTurnSample with:
                - user_input: The query
                - response: The generated response
                - retrieved_contexts: List of retrieved context chunks
                - reference (optional): Reference answer
                - reference_contexts (optional): List of reference contexts
                - retrieved_context_ids (optional): IDs of retrieved contexts
                - reference_context_ids (optional): IDs of reference contexts
        
        Returns:
            float: Precision score between 0 and 1
        """
        if self.metric_type == "llm_without_reference":
            return await self._evaluate_llm_without_reference(sample)
        elif self.metric_type == "llm_with_reference":
            return await self._evaluate_llm_with_reference(sample)
        elif self.metric_type == "non_llm":
            return await self._evaluate_non_llm(sample)
        elif self.metric_type == "id_based":
            return await self._evaluate_id_based(sample)
        else:
            raise ValueError(f"Unknown metric type: {self.metric_type}")
    
    async def _evaluate_llm_without_reference(self, sample) -> float:
        """Evaluate using LLM comparison with response."""
        # Implementation would use ragas.metrics.LLMContextPrecisionWithoutReference
        pass
    
    async def _evaluate_llm_with_reference(self, sample) -> float:
        """Evaluate using LLM comparison with reference."""
        # Implementation would use ragas.metrics.LLMContextPrecisionWithReference
        pass
    
    async def _evaluate_non_llm(self, sample) -> float:
        """Evaluate using non-LLM similarity measures."""
        # Implementation would use ragas.metrics.NonLLMContextPrecisionWithReference
        pass
    
    async def _evaluate_id_based(self, sample) -> float:
        """Evaluate using ID-based comparison."""
        # Implementation would use ragas.metrics.IDBasedContextPrecision
        # Formula: # of retrieved IDs found in reference / total retrieved IDs
        pass


def create_context_precision_evaluator(llm=None, embeddings=None, metric_type: str = "llm_without_reference"):
    """
    Factory function to create a Context Precision evaluator.
    
    Args:
        llm: Language model instance
        embeddings: Embeddings model instance
        metric_type: Type of evaluation metric to use
    
    Returns:
        ContextPrecisionEvaluator: Configured evaluator instance
    """
    return ContextPrecisionEvaluator(llm=llm, embeddings=embeddings, metric_type=metric_type)
