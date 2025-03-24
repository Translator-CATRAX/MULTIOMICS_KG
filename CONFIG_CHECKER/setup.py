from setuptools import setup, find_packages

setup(
    name="TABLASSERT_CONFIG_CHECKER",
    version="3.0.0",
    packages=find_packages(),
    install_requires=[
        "requests", "pyyaml"],
    entry_points={
        "console_scripts": [
            "kg_config=src.main:kg_config_main",
            "table_config=src.main:table_config_main",
            "config_checker_test=src.test:main"]},
    description="""
        Check your Tablassert KG and Table Configs for syntax with this
        simple and easy to use tool. Tablassert itself preforms a more
        comprehensive check but this is a great start and doesn't require
        a hundered database connections.""",
    author="Skye Goetz (ISB)",
    author_email="sgoetz@systemsbiology.org",
    url="https://github.com/Translator-CATRAX/MULTIOMICS_KG",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    python_requires=">=3.12.6")
