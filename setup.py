from setuptools import setup, find_packages

setup(
    name='rag_package',  # Replace with your package name
    version='0.1.0',  # Initial version
    description='A package for RAG pipeline implementation',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/rag_package',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        'faiss-cpu',
        'sentence-transformers',
        'datasets',
        'transformers',
        'openai'
    ],
    python_requires='>=3.6',  # Specify your Python version
)
