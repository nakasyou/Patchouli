from setuptools import setup

with open("README.md",encoding="utf-8") as f:
    long_description=f.read()

setup(
    name="pyPatchouli",
    version="0.1.0",
    install_requires=[],
    description="Patchouli is LINE app's history text parser.",
    long_description=long_description,
    license="MIT",
    keywords='line patchouliv history parser',
    author="nakasyou",
    url="https://github.com/nakasyou/Patchouli",
    long_description_content_type="text/markdown"
)