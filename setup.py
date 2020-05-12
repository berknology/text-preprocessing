from setuptools import setup, find_packages


def parse_requirements(fn):
    with open(fn) as f:
        return [req for req in f.read().strip().split('\n') if "==" in req and "#" not in req]


parsed_requirements = parse_requirements(
    'requirements/requirements.txt',
)

parsed_test_requirements = parse_requirements(
    'requirements/requirements.txt',
)

requirements = [str(ir) for ir in parsed_requirements]
test_requirements = [str(tr) for tr in parsed_test_requirements]


with open('README.md') as description_file:
    description = description_file.read()


setup(
    name='text_preprocessing',
    version='0.0.1',
    description="NLP reusable machine learning solution toolkit",
    long_description=description,
    license="BSD license",
    author="He Hao",
    author_email='berknology@gmail.com',
    packages=find_packages(include=['text_preprocessing', 'text_preprocessing.*']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='NLP',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
