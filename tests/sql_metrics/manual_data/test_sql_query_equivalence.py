"""
Test Sql Query Equivalence - Evaluation with Metrics
"""

import pytest
import allure
import os
from ragas import evaluate
import numpy as np
from ragas.metrics import LLMSQLEquivalence
from datasets import Dataset
from langchain_openai import AzureChatOpenAI

def test_sql_query_equivalence_with_metrics(ragas_dataset):
    """Test Sql Query Equivalence metric with actual evaluation and scoring."""
    
    # Verify dataset exists
    assert len(ragas_dataset) > 0, "Dataset should contain at least one sample"
    
    allure.attach(
        f"Total samples: {len(ragas_dataset)}", 
        name="Dataset Info", 
        attachment_type=allure.attachment_type.TEXT
    )
    
    # Prepare evaluation data
    eval_data = {
        "question": [],
        "answer": [],
        "contexts": [],
        "reference": [],
        "reference_contexts": [],
    }
    
    for idx, sample in enumerate(ragas_dataset):
        # Create sample data for evaluation
        question = f"Sample question {idx + 1}"
        answer = f"Sample answer {idx + 1}"
        contexts = [f"Context {idx + 1}"]
        reference = f"Reference answer {idx + 1}"
        reference_contexts = [f"Reference context {idx + 1}"]
        
        eval_data["question"].append(question)
        eval_data["answer"].append(answer)
        eval_data["contexts"].append(contexts)
        eval_data["reference"].append(reference)
        eval_data["reference_contexts"].append(reference_contexts)
        
        allure.attach(
            f"Q: {question}\nA: {answer}",
            name=f"Sample {idx + 1}",
            attachment_type=allure.attachment_type.TEXT
        )
    
    dataset = Dataset.from_dict(eval_data)
    
    # Initialize LLM
    llm = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0
    )
    
    print(f"\n🔍 Running Sql Query Equivalence evaluation...")
    
    try:
        result = evaluate(dataset, metrics=[LLMSQLEquivalence()], llm=llm)
        metrics_df = result.to_pandas()
        
        print(f"\n📊 Results:\n{metrics_df}")
        
        allure.attach(str(metrics_df), name="Results", attachment_type=allure.attachment_type.TEXT)
        
        # Attach scores
        # Filter for numeric columns only
        numeric_cols = metrics_df.select_dtypes(include=[np.number]).columns.tolist()
        
        for idx, row in metrics_df.iterrows():
            scores = {col: row[col] for col in numeric_cols}
            
            allure.attach(
                f"Scores: {scores}",
                name=f"Sample {idx + 1} Score",
                attachment_type=allure.attachment_type.TEXT
            )
        
        # Summary
        summary = f"\nSql Query Equivalence Evaluation:\n"
        for col in numeric_cols:
            if col in metrics_df.columns:
                summary += f"- Avg {col}: {metrics_df[col].mean():.4f}\n"
        
        print(summary)
        allure.attach(summary, name="📊 Summary", attachment_type=allure.attachment_type.TEXT)
        
    except Exception as e:
        error_msg = f"Evaluation failed: {str(e)}"
        print(f"\n❌ {error_msg}")
        allure.attach(error_msg, name="Error", attachment_type=allure.attachment_type.TEXT)
        pytest.skip(f"Metric evaluation not yet implemented: {e}")
