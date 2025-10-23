"""
Pytest configuration for retrieval augmented generation LLM-generated tests.
Provides fixture to generate synthetic test data using Ragas TestsetGenerator.
"""

import pytest
import os
from ragas.testset import TestsetGenerator
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
            model=os.getenv("AZURE_OPENAI_EMBEDDING_MODEL")
        )
    )
    
    # Create sample documents for test generation
    documents = [
        Document(
            page_content="""
            Retrieval-Augmented Generation (RAG) is an advanced technique in natural language processing that
            combines the strengths of information retrieval and text generation. This approach enhances the
            capabilities of large language models by providing them with relevant context from external knowledge
            sources. The RAG framework consists of two main components: a retriever and a generator. The retriever
            searches through a large corpus of documents to find relevant information based on the input query.
            This component typically uses dense vector representations and similarity search algorithms to identify
            the most pertinent documents. The generator, usually a pre-trained language model, then uses both the
            original query and the retrieved documents to produce a coherent and contextually appropriate response.
            This hybrid approach addresses several limitations of traditional language models, including the ability
            to access up-to-date information, reduce hallucinations, and provide more accurate and verifiable answers.
            RAG systems have been successfully applied in various domains including question answering, conversational
            AI, and knowledge-intensive tasks. The technique allows models to leverage vast amounts of external
            knowledge without requiring this information to be stored in the model parameters themselves, making it
            more efficient and adaptable to changing information landscapes.
            """,
            metadata={"source": "rag_guide"}
        )
    ]
    
    # Create generator and generate synthetic data
    generator = TestsetGenerator.from_langchain(llm=llm, embedding_model=embeddings)
    dataset = generator.generate_with_langchain_docs(documents=documents, testset_size=2)
    
    print(f"✅ Generated {len(dataset)} synthetic test samples")
    
    return dataset
