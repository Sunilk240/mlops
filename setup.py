from setuptools import setup, find_packages

setup(
    name="mlops",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.26.0',
        'pandas>=2.1.0',
        'flask==2.3.3',
        'pytest==7.4.0',
        'python-dotenv==1.0.0',
        'scikit-learn>=1.3.0'
    ],
) 