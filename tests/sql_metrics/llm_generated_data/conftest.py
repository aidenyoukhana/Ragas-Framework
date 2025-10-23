"""
Pytest configuration for SQL metrics LLM-generated tests.
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
            SQL (Structured Query Language) is a domain-specific language used for managing and manipulating
            relational databases. It was initially developed in the 1970s by IBM and has become the standard
            language for relational database management systems. SQL provides commands for defining database
            schemas, inserting and updating data, querying data, and controlling access to databases. The
            language consists of several key components including Data Definition Language (DDL) for creating
            and modifying database structures, Data Manipulation Language (DML) for inserting, updating, and
            deleting data, and Data Query Language (DQL) for retrieving data from databases. SQL uses a
            declarative syntax where users specify what data they want rather than how to retrieve it, making
            it accessible to both technical and non-technical users. Common operations include SELECT statements
            for querying data, JOIN operations for combining data from multiple tables, and aggregate functions
            like COUNT, SUM, and AVG for data analysis. Modern SQL databases support advanced features such as
            stored procedures, triggers, views, and transactions that ensure data integrity and consistency.
            Popular SQL database systems include MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server, and
            SQLite, each with their own extensions and optimizations while maintaining SQL standard compliance.
            """,
            metadata={"source": "sql_guide"}
        )
    ]
    
    # Create generator and generate synthetic data
    generator = TestsetGenerator.from_langchain(llm=llm, embedding_model=embeddings)
    dataset = generator.generate_with_langchain_docs(documents=documents, testset_size=2)
    
    print(f"✅ Generated {len(dataset)} synthetic test samples")
    
    return dataset
