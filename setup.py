from setuptools import setup, find_packages


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    """
    Docstring for get_requirements
    
    :param file_path: Path to the requirements file
    :type file_path: str
    :return: List of requirements
    :rtype: list[str]
    """
    requirements = []

    with open(file_path, 'r', encoding="utf-8") as file_obj:
        for req in file_obj:
            req = req.strip()
            if req and req != HYPHEN_E_DOT and not req.startswith("#"):
                requirements.append(req)
    return requirements


setup(
    name='mlproject',
    version='0.1.0',
    author='Zakir',
    author_email='cryptobotnewgls@gmail.com',
    description='End-to-end machine learning project setup',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)