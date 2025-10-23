"""
Response Relevancy Evaluator (formerly Answer Relevance)

Measures how relevant a response is to the user input. This metric assesses whether
the generated response actually addresses the user's question.

Formula:
    Response Relevancy = (1/N) × Σ(i=1 to N) cosine_similarity(E_gi, E_o)

Where:
    E_gi = Embedding of i-th generated question from response
    E_o = Embedding of user input
    N = Number of generated questions (default is 3)

Process:
    1. Generate N artificial questions from the response content
    2. Compute cosine similarity between each generated question and user input
    3. Average these similarity scores
"""

from typing import Optional


class ResponseRelevancyEvaluator:
    """
    Response Relevancy metric evaluator.
    
    Measures how well the response addresses the user's question by generating
    artificial questions from the response and comparing their similarity with
    the original user input.
    """
    
    def __init__(self, llm=None, embeddings=None, num_questions: int = 3):
        """
        Initialize Response Relevancy Evaluator.
        
        Args:
            llm: Language model for question generation
            embeddings: Embeddings model for similarity calculation
            num_questions: Number of artificial questions to generate (default: 3)
        """
        self.llm = llm
        self.embeddings = embeddings
        self.num_questions = num_questions
    
    async def evaluate(self, sample):
        """
        Evaluate response relevancy for a given sample.
        
        Args:
            sample: SingleTurnSample with:
                - user_input: The original user question
                - response: The generated response
        
        Returns:
            float: Relevancy score. Note: may fall outside [0, 1] due to cosine similarity range [-1, 1]
        """
        return await self._evaluate_relevancy(sample)
    
    async def _evaluate_relevancy(self, sample) -> float:
        """
        Evaluate response relevancy.
        
        Process:
        1. Generate N artificial questions from the response using LLM
        2. Embed user input and each generated question
        3. Calculate cosine similarity between each pair
        4. Return average similarity score
        """
        # Implementation would use ragas.metrics.ResponseRelevancy
        pass


def create_response_relevancy_evaluator(llm=None, embeddings=None, num_questions: int = 3):
    """
    Factory function to create a Response Relevancy evaluator.
    
    Args:
        llm: Language model instance
        embeddings: Embeddings model instance
        num_questions: Number of generated questions to use
    
    Returns:
        ResponseRelevancyEvaluator: Configured evaluator instance
    """
    return ResponseRelevancyEvaluator(llm=llm, embeddings=embeddings, num_questions=num_questions)
