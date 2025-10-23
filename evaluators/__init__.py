"""
Ragas Evaluators Package

A comprehensive evaluation framework for Retrieval-Augmented Generation (RAG)
and other AI applications, based on the Ragas documentation.

Categories:
- retrieval_augmented_generation: RAG-specific metrics (8 evaluators)
- nvidia_metrics: NVIDIA-specific metrics (3 evaluators)
- agents_and_tools: Agent and tool use metrics (4 evaluators)
- natural_language_comparison: NLP comparison metrics (7 evaluators)
- sql_metrics: SQL query quality metrics (2 evaluators)
- general_purpose_and_other_tasks: General purpose metrics (5 evaluators)

Total: 29 evaluators across 6 categories
"""

from . import (
    retrieval_augmented_generation,
    nvidia_metrics,
    agents_and_tools,
    natural_language_comparison,
    sql_metrics,
    general_purpose_and_other_tasks,
)

__all__ = [
    "retrieval_augmented_generation",
    "nvidia_metrics",
    "agents_and_tools",
    "natural_language_comparison",
    "sql_metrics",
    "general_purpose_and_other_tasks",
]
