# Ragas LLM Evaluation Framework

A comprehensive testing framework for evaluating Large Language Models using the Ragas library. This framework includes categorized evaluators with both LLM-generated and manual test datasets.

<img width="1245" height="878" alt="image" src="https://github.com/user-attachments/assets/8a9b035d-6a3d-488d-9943-53ef2585e1c7" />
<img width="557" height="832" alt="image" src="https://github.com/user-attachments/assets/46fec4ab-8866-403c-8ced-fc5ba1a680b5" />


## Features

- **29+ Ragas Evaluators**: Organized into 6 categories covering RAG, agents, SQL, NLP, and more
- **Dual Testing Approach**: 
  - LLM-generated test data using Ragas TestsetGenerator
  - Manual test data for precise validation
- **Azure OpenAI Integration**: Built-in support for Azure OpenAI (gpt-4o) with embeddings
- **Interactive Reporting**: Allure test reports with visualizations and detailed results
- **Automated Test Suite**: All evaluators have corresponding test files

## Prerequisites

- Python 3.8+ (tested with Python 3.13.7)
- Virtual environment (recommended)
- Azure OpenAI access with:
  - GPT-4o deployment
  - text-embedding-3-large deployment
- Allure CLI (for reports): `brew install allure` (macOS) or see [Allure docs](https://docs.qameta.io/allure/)

## Setup

### 1. Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with your Azure OpenAI and Azure AI Foundry credentials:

```bash
# Environment Variables for LLM Evaluation Framework

# OpenAI Platform Configuration (Optional)
# Get your API key from: https://platform.openai.com/api-keys
# OPENAI_API_KEY=sk-dummy-key-for-testing
# OPENAI_MODEL=gpt-4o-mini

# Azure AI Foundry Hosted LLM Configuration
# Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=text-embedding-3-small
AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-3-small
 
# Azure AI Foundry Project (following Microsoft documentation standard)
AZURE_SUBSCRIPTION_ID=your_azure_subscription_id_here
AZURE_RESOURCE_GROUP=your_resource_group_name_here
AZURE_PROJECT_NAME=your_project_name_here
```

Get these values from:
- **Azure OpenAI values**: Azure Portal → Your OpenAI resource → "Keys and Endpoint"
- **Azure AI Foundry values**: Azure AI Foundry portal → Your project → "Project settings"

## Usage

### Run Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run with verbose output and print statements
pytest tests/ -v -s

# Run only LLM-generated data tests
pytest tests/**/llm_generated_data/ -v -s

# Run only manual data tests
pytest tests/**/manual_data/ -v -s

# Run with Allure
pytest tests/ -v --alluredir=allure-results

# Serve the Allure Results
allure serve allure-results
```

### View Results

#### Console Output
Test results will be displayed in the console with detailed output when using `-v -s` flags.

#### Allure Reports (Interactive HTML)
Generate and view detailed test reports with charts, timelines, and visualizations:

```bash
# Run all tests and generate Allure results
pytest tests/ --alluredir=allure-results -v -s

# Generate HTML report from results
allure generate allure-results --clean -o allure-report

# Open report in browser
allure open allure-report
```

The Allure report provides:
- Test execution timeline
- Pass/fail statistics with charts
- Detailed test output and console logs
- **Evaluation metrics and scores** (when tests run actual evaluations)
- Test organization by category
- Historical trends (when running multiple times)

### Test Data Organization

Each evaluator category has two types of tests:

1. **`llm_generated_data/`**: Tests using Ragas TestsetGenerator to create synthetic test data
   - **Data Generation Tests**: Verify that test data can be generated (e.g., `test_faithfulness_generated.py`)
   - **Evaluation Tests**: Actually run the metric and show scores (e.g., `test_faithfulness_evaluation_with_metrics.py`)
   - Automatically generates diverse test questions and contexts
   - Uses Azure OpenAI (gpt-4o) for generation
   - Creates 2 test samples per run (configurable in `tests/conftest.py`)

2. **`manual_data/`**: Tests using hand-crafted test cases
   - Precise control over test inputs
   - Deterministic results
   - Good for regression testing

### Viewing Evaluation Metrics

To see actual metric scores (faithfulness, relevance, etc.) in your tests:

1. **Use the evaluation test files** (e.g., `test_faithfulness_evaluation_with_metrics.py`)
2. These tests will:
   - Generate or use test data
   - Run the actual Ragas metric evaluation
   - Display scores in console output
   - Attach detailed metrics to Allure reports

Example metrics you'll see:
- **Individual Sample Scores**: Faithfulness score for each test sample (0.0 to 1.0)
- **Summary Statistics**: Average, min, max scores across all samples
- **Evaluation DataFrame**: Complete results table with all metrics

Check the Allure report attachments for:
- `📊 Summary Statistics` - Overall performance metrics
- `Sample N Score` - Individual sample evaluation results
- `Evaluation Results DataFrame` - Full metrics table

> **💡 Want to see actual metric scores?** See [`HOW_TO_ADD_METRIC_EVALUATION.md`](./HOW_TO_ADD_METRIC_EVALUATION.md) for a complete guide on adding metric evaluation to your tests.

### Adding New Evaluators

1. Create the evaluator class in the appropriate category folder under `evaluators/`
2. Create test files in both `tests/<category>/llm_generated_data/` and `tests/<category>/manual_data/`
3. For LLM-generated tests, use the `ragas_dataset` fixture from `tests/conftest.py`
4. **Important**: Import `allure` and use `allure.attach()` to add test data to reports
5. **For metric evaluation**: See [`HOW_TO_ADD_METRIC_EVALUATION.md`](./HOW_TO_ADD_METRIC_EVALUATION.md) for adding actual score calculations
6. Run tests to validate: `pytest tests/<category>/ -v -s`

Example LLM-generated test structure:
```python
import pytest
import allure
from evaluators.your_category.your_evaluator import YourEvaluator

def test_your_evaluator_generated(ragas_dataset):
    """Test YourEvaluator with LLM-generated data"""
    evaluator = YourEvaluator()
    assert len(ragas_dataset) > 0
    
    # Attach dataset info to Allure report
    allure.attach(
        f"Total samples generated: {len(ragas_dataset)}", 
        name="Dataset Info", 
        attachment_type=allure.attachment_type.TEXT
    )
    
    # Print and attach each sample
    for idx, sample in enumerate(ragas_dataset):
        print(f"\nSample {idx + 1}: {sample}")
        
        # Attach to Allure report
        allure.attach(
            f"Sample data: {sample}",
            name=f"Sample {idx + 1}",
            attachment_type=allure.attachment_type.TEXT
        )
```

> **Note**: The `allure.attach()` calls are what make your test data visible in the Allure HTML report. Without them, only console output is captured.

## Project Structure

```
.
├── evaluators/                      # Ragas evaluators organized by category
│   ├── agents_and_tools/           # Agent-specific metrics (4 evaluators)
│   │   ├── agent_goal_accuracy_evaluator.py
│   │   ├── tool_call_accuracy_evaluator.py
│   │   ├── tool_call_f1_evaluator.py
│   │   └── topic_adherence_evaluator.py
│   ├── general_purpose_and_other_tasks/  # General metrics (5 evaluators)
│   │   ├── aspect_critic_evaluator.py
│   │   ├── instance_specific_rubrics_scoring_evaluator.py
│   │   ├── rubrics_based_scoring_evaluator.py
│   │   ├── simple_criteria_scoring_evaluator.py
│   │   └── summarization_evaluator.py
│   ├── natural_language_comparison/  # NLP comparison metrics (6 evaluators)
│   │   ├── bleu_score_evaluator.py
│   │   ├── exact_match_evaluator.py
│   │   ├── factual_correctness_evaluator.py
│   │   ├── nonllm_string_similarity_evaluator.py
│   │   ├── rouge_score_evaluator.py
│   │   └── semantic_similarity_evaluator.py
│   ├── nvidia_metrics/             # NVIDIA-specific metrics (3 evaluators)
│   │   ├── answer_accuracy_evaluator.py
│   │   ├── context_relevance_evaluator.py
│   │   └── response_groundedness_evaluator.py
│   ├── retrieval_augmented_generation/  # RAG metrics (8 evaluators)
│   │   ├── context_entities_recall_evaluator.py
│   │   ├── context_precision_evaluator.py
│   │   ├── context_recall_evaluator.py
│   │   ├── faithfulness_evaluator.py
│   │   ├── multimodal_faithfulness_evaluator.py
│   │   ├── multimodal_relevance_evaluator.py
│   │   ├── noise_sensitivity_evaluator.py
│   │   └── response_relevancy_evaluator.py
│   └── sql_metrics/                # SQL-specific metrics (2 evaluators)
│       ├── datacompy_score_evaluator.py
│       └── sql_query_equivalence_evaluator.py
│
├── tests/                          # Test files mirroring evaluator structure
│   ├── <category>/
│   │   ├── llm_generated_data/     # Tests using Ragas TestsetGenerator
│   │   └── manual_data/            # Tests using hand-crafted data
│   └── conftest.py                 # Pytest configuration and fixtures
│
├── conftest.py                     # Project-level pytest configuration
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (not in git)
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## Evaluator Categories

### Agents and Tools (4 evaluators)
- **Agent Goal Accuracy**: Measures if agent achieves intended goals
- **Tool Call Accuracy**: Validates correct tool selection and usage
- **Tool Call F1**: F1 score for tool call precision and recall
- **Topic Adherence**: Checks if agent stays on topic

### General Purpose and Other Tasks (5 evaluators)
- **Aspect Critic**: Evaluates specific aspects of responses
- **Instance Specific Rubrics Scoring**: Scoring based on custom rubrics per instance
- **Rubrics Based Scoring**: General rubric-based evaluation
- **Simple Criteria Scoring**: Pass/fail criteria evaluation
- **Summarization**: Evaluates summary quality

### Natural Language Comparison (6 evaluators)
- **BLEU Score**: Machine translation quality metric
- **Exact Match**: Binary exact string matching
- **Factual Correctness**: Validates factual accuracy
- **Non-LLM String Similarity**: Traditional string similarity metrics
- **ROUGE Score**: Recall-oriented summarization metric
- **Semantic Similarity**: Embedding-based semantic comparison

### NVIDIA Metrics (3 evaluators)
- **Answer Accuracy**: NVIDIA-specific answer validation
- **Context Relevance**: Measures context relevance
- **Response Groundedness**: Checks grounding in provided context

### Retrieval Augmented Generation (8 evaluators)
- **Context Entities Recall**: Entity coverage in retrieved context
- **Context Precision**: Precision of retrieved contexts
- **Context Recall**: Recall of relevant contexts
- **Faithfulness**: Answer faithfulness to context
- **Multimodal Faithfulness**: Faithfulness for multimodal data
- **Multimodal Relevance**: Relevance for multimodal responses
- **Noise Sensitivity**: Robustness to noisy contexts
- **Response Relevancy**: Response relevance to query

### SQL Metrics (2 evaluators)
- **DataComPy Score**: DataFrame comparison scoring
- **SQL Query Equivalence**: Validates SQL query semantic equivalence

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your evaluator in the appropriate category folder
4. Create tests in both `llm_generated_data/` and `manual_data/` folders
5. Run tests to validate: `pytest tests/ -v -s`
6. Update this README if adding new categories
7. Submit a pull request

## License

This project is licensed under the MIT License.
