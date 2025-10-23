"""
Pytest configuration for NVIDIA metrics LLM-generated tests.
Provides fixture to generate synthetic test data using Ragas TestsetGenerator.
"""

import pytest
import os
from ragas.testset import TestsetGenerator
from ragas.testset.synthesizers import default_query_distribution
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_core.documents import Document


@pytest.fixture(scope="session")
def ragas_dataset():
    """
    Generate a synthetic test dataset using Ragas TestsetGenerator.
    This fixture is scoped to session to avoid regenerating data for each test.
    """
    print("\n🚀 Generating synthetic test data...")
    
    # Initialize Azure OpenAI LLM
    llm = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0
    )
    
    # Initialize Azure OpenAI Embeddings
    embeddings = LangchainEmbeddingsWrapper(
        AzureOpenAIEmbeddings(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"),
        )
    )
    
    # Create sample documents for test generation
    documents = [
        Document(
            page_content="""
            Python is a high-level, interpreted programming language known for its simplicity and readability.
            Created by Guido van Rossum and first released in 1991, Python has become one of the most popular
            programming languages in the world. Its design philosophy emphasizes code readability with the use
            of significant indentation. Python supports multiple programming paradigms, including structured,
            object-oriented, and functional programming. The language provides constructs that enable clear
            programming on both small and large scales. Python features a dynamic type system and automatic
            memory management. It has a large and comprehensive standard library, often described as having
            batteries included. Python interpreters are available for many operating systems, making Python
            a truly cross-platform language. The language is used in various domains including web development,
            data science, artificial intelligence, scientific computing, and automation. Popular frameworks
            like Django and Flask have made Python a preferred choice for web development. In data science,
            libraries such as NumPy, Pandas, and Matplotlib provide powerful tools for data analysis and
            visualization. Machine learning frameworks like TensorFlow and PyTorch have further cemented
            Python's position in the AI and ML community.
            """,
            metadata={"source": "programming_guide"}
        )
    ]
    
    # Create generator and generate synthetic data
    generator = TestsetGenerator.from_langchain(llm=llm, embedding_model=embeddings)
    dataset = generator.generate_with_langchain_docs(documents=documents, testset_size=2)
    
    print(f"✅ Generated {len(dataset)} synthetic test samples")
    
    return dataset
