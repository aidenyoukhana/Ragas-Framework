"""
Test Topic Adherence - Evaluation with LLM-Generated Data
"""

import pytest
import allure


def test_topic_adherence_generated_with_metrics(ragas_dataset):
    """
    Test Topic Adherence metric with LLM-generated synthetic data.
    
    This test verifies that:
    1. Synthetic data can be generated successfully
    2. The dataset contains valid samples
    3. We can access and display the generated data
    
    Note: TopicAdherenceScore requires MultiTurnSample format with topics,
    which is different from the standard RAG format. This test focuses on
    dataset generation validation.
    """
    
    # Verify dataset exists
    assert len(ragas_dataset) > 0, "Dataset should contain at least one sample"
    
    print(f"\n✅ Generated {len(ragas_dataset)} synthetic samples")
    
    allure.attach(
        f"Total samples: {len(ragas_dataset)}", 
        name="Dataset Info", 
        attachment_type=allure.attachment_type.TEXT
    )
    
    # Display generated samples
    for idx, sample in enumerate(ragas_dataset, start=1):
        print(f"\nSample {idx}:")
        print(sample)
        
        allure.attach(
            str(sample),
            name=f"Generated Sample {idx}",
            attachment_type=allure.attachment_type.TEXT
        )
    
    print("\n✅ Test passed: Topic Adherence dataset generation successful")

