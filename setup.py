from setuptools import setup, find_packages

# Read the README.md file with UTF-8 encoding
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyperfcheck',
    version='0.1.1',  # Update with the current version
    description='A high-performance benchmarking library for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Janardhan Medathati',
    author_email='7janardhan7@gmail.com',
    url='https://github.com/Janardhan11/pyperfcheck',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'matplotlib',
        'tabulate',
        'asyncio',  # if async is required
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',  # Explicitly specify the license
)