"""
Test Simple Criteria Scoring - LLM Generated Data Validation
"""

import pytest
import allure


def test_simple_criteria_scoring_generated_with_metrics(ragas_dataset):
    """Validate that LLM-generated dataset is created successfully for simple criteria scoring."""
    
    # Verify dataset was generated
    assert ragas_dataset is not None, "Dataset should be generated"
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
            name=f"Sample {idx}",
            attachment_type=allure.attachment_type.TEXT
        )
    
    print(f"\n✅ Dataset generation test passed - {len(ragas_dataset)} samples created")
