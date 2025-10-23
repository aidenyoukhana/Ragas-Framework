"""
Shared pytest configuration for LLM-generated data tests

This file provides fixtures for generating synthetic test data using Ragas.
"""

import os
import pytest
from dotenv import load_dotenv
from ragas.testset import TestsetGenerator
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_core.documents import Document

load_dotenv()


@pytest.fixture(scope="session")
def ragas_dataset():
    """Generate synthetic test data using Ragas TestsetGenerator with Azure OpenAI."""
    print("\n🚀 Generating synthetic test data for agents and tools...")
    
    try:
        # Sample documents for test data generation (must be substantial for Ragas)
        documents = [
            Document(page_content="""
Python is a high-level, interpreted programming language known for its simplicity and readability.
It was created by Guido van Rossum and first released in 1991. Python supports multiple programming
paradigms, including procedural, object-oriented, and functional programming. It has a comprehensive
standard library that provides tools suited to many tasks. Python is widely used in web development,
data science, artificial intelligence, scientific computing, automation, and many other fields.
The language emphasizes code readability with its notable use of significant indentation. Python's
design philosophy prioritizes code readability and allows programmers to express concepts in fewer
lines of code than would be possible in languages such as C++ or Java. The language provides constructs
intended to enable clear programs on both a small and large scale. Python features a dynamic type
system and automatic memory management and supports multiple programming paradigms, including
object-oriented, imperative, functional programming, and procedural styles. It has a large and
comprehensive standard library. Python interpreters are available for many operating systems, allowing
Python code to run on a wide variety of systems. Python is often described as a "batteries included"
language due to its comprehensive standard library. Many Python programmers report substantial
productivity gains and feel the language encourages the development of higher quality, more maintainable
code. Python is used by many large organizations including Google, NASA, and CERN.
            """)
        ]
        
        # Use AzureChatOpenAI directly for Azure deployments
        llm = AzureChatOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        )
        
        # Initialize Azure OpenAI embeddings
        embeddings = LangchainEmbeddingsWrapper(
            AzureOpenAIEmbeddings(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                model=os.getenv("AZURE_OPENAI_EMBEDDING_MODEL")
            )
        )
        
        # Create generator and generate test data
        generator = TestsetGenerator.from_langchain(llm=llm, embedding_model=embeddings)
        dataset = generator.generate_with_langchain_docs(documents=documents, testset_size=2)
        
        print(f"✅ Generated {len(dataset)} synthetic test samples")
        return dataset
    
    except Exception as e:
        error_msg = f"Dataset generation failed: {str(e)}"
        print(f"❌ {error_msg}")
        print(f"💡 Ensure these environment variables are set:")
        print(f"   - AZURE_OPENAI_API_KEY")
        print(f"   - AZURE_OPENAI_API_VERSION")
        print(f"   - AZURE_OPENAI_ENDPOINT")
        print(f"   - AZURE_OPENAI_DEPLOYMENT_NAME")
        print(f"   - AZURE_OPENAI_EMBEDDING_MODEL")
        pytest.skip(error_msg)

