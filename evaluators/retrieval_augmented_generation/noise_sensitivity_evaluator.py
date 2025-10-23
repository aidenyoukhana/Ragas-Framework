"""
Noise Sensitivity Evaluator

Measures how often a system makes errors by providing incorrect responses when
utilizing either relevant or irrelevant retrieved documents. This helps identify
how sensitive the system is to noise in the retrieved contexts.

Formula:
    Noise Sensitivity = # of incorrect claims in response / Total # of claims in response

Modes:
    - 'relevant': Measures sensitivity to irrelevant but relevant-looking contexts
    - 'irrelevant': Measures sensitivity to clearly irrelevant contexts
"""

from typing import Optional, Literal


class NoiseSensitivityEvaluator:
    """
    Noise Sensitivity metric evaluator.
    
    Measures how the system's response quality is affected by noisy or irrelevant
    retrieved contexts. Lower scores indicate better robustness to noise.
    """
    
    def __init__(self, llm=None, mode: Literal["relevant", "irrelevant"] = "relevant"):
        """
        Initialize Noise Sensitivity Evaluator.
        
        Args:
            llm: Language model for analysis
            mode: Type of noise to evaluate:
                - 'relevant': Noisy relevant contexts (mix of relevant and irrelevant)
                - 'irrelevant': Clearly irrelevant contexts
        """
        self.llm = llm
        self.mode = mode
    
    async def evaluate(self, sample):
        """
        Evaluate noise sensitivity for a given sample.
        
        Args:
            sample: SingleTurnSample with:
                - user_input: The query
                - response: The generated response
                - reference: Ground truth answer
                - retrieved_contexts: Mix of relevant and irrelevant contexts
        
        Returns:
            float: Noise sensitivity score between 0 and 1 (lower is better)
        """
        return await self._evaluate_noise_sensitivity(sample)
    
    async def _evaluate_noise_sensitivity(self, sample) -> float:
        """
        Evaluate noise sensitivity.
        
        Process:
        1. Identify claims in the response
        2. Identify claims that are NOT supported by ground truth
        3. Calculate: # incorrect claims / total claims
        
        The score indicates how many claims in the response are incorrect,
        potentially due to noise in the retrieved contexts.
        """
        # Implementation would use ragas.metrics.NoiseSensitivity
        pass


def create_noise_sensitivity_evaluator(llm=None, mode: Literal["relevant", "irrelevant"] = "relevant"):
    """
    Factory function to create a Noise Sensitivity evaluator.
    
    Args:
        llm: Language model instance
        mode: Type of noise to evaluate ('relevant' or 'irrelevant')
    
    Returns:
        NoiseSensitivityEvaluator: Configured evaluator instance
    """
    return NoiseSensitivityEvaluator(llm=llm, mode=mode)
