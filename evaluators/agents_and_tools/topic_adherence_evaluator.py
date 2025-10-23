"""
Topic Adherence Evaluator

Measures whether the agent/tool stays focused on the given topic during execution.
Evaluates if the agent diverges from the main topic or maintains topical coherence.
"""

from typing import Optional


class TopicAdherenceEvaluator:
    """
    Topic Adherence metric evaluator for Agents.
    
    Measures how well the agent stays focused on the specified topic
    throughout the conversation or task execution.
    """
    
    def __init__(self, llm=None):
        """
        Initialize Topic Adherence Evaluator.
        
        Args:
            llm: Language model for analysis
        """
        self.llm = llm
    
    async def evaluate(self, sample):
        """
        Evaluate topic adherence.
        
        Args:
            sample: Agent sample with:
                - topic: The specified topic
                - response: Agent's response
                - intermediate_steps: Agent's intermediate steps/thoughts
        
        Returns:
            float: Adherence score
        """
        return await self._evaluate_adherence(sample)
    
    async def _evaluate_adherence(self, sample) -> float:
        """
        Evaluate adherence to topic.
        
        Process:
        1. Identify the topic from the input
        2. Analyze response and steps for topic relevance
        3. Measure deviation from topic
        4. Return adherence score
        """
        # Implementation for topic adherence
        pass


def create_topic_adherence_evaluator(llm=None):
    """
    Factory function to create a Topic Adherence evaluator.
    
    Args:
        llm: Language model instance
    
    Returns:
        TopicAdherenceEvaluator: Configured evaluator instance
    """
    return TopicAdherenceEvaluator(llm=llm)
