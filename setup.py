from setuptools import setup, find_packages


def read_requirements(filename='requirements.txt'):
    with open(filename) as req:
        content = req.read()
        requirements = content.split('\n')
    return [r for r in requirements if r and not r.startswith('#')]


setup(name='pythia', version='0.1.0', packages=find_packages(),
    install_requires=read_requirements(), entry_points={'console_scripts':
    ['pythia=src.main:main']}, author='Matteo Notaro', author_email=
    'matteoatnotaro@gmail.com', description=
    'Pythia Suggest is a tool designed to automatically generate docstrings for Python files using the power of large language models (LLMs)'
    , long_description=open('README.md').read(),
    long_description_content_type='text/markdown', url=
    'https://github.com/MattNot/Pythia-Suggest', classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'], python_requires='>=3.6')
