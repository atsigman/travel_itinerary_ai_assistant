from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ai_travel_agent",
    version="0.1",
    author="atsigman",
    packages=find_packages(),
    install_requires=requirements,
)