from setuptools import setup, find_packages

setup(
    name="cer_pex1_lib",
    version="1.0.1",
    description="Library for the first programming exercise of the CER lecture.",
    author="Christoph Zelch",
    author_email="zelch@sim.informatik.tu-darmstadt.de",
    packages=find_packages(),
    python_requires=">=3.6.0",
    setup_requires=['wheel'],
    install_requires=[
        "numpy",
        "matplotlib",
        "jupyter"
    ]
)
