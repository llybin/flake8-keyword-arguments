from setuptools import find_packages, setup

package_name = 'flake8_keyword_arguments'


def get_long_description():
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    version='0.1.0',
    description=(
        'A flake8 extension that is looking for function calls and '
        'forces to use keyword arguments if there are more than X arguments'
    ),
    classifiers=[
        'Environment :: Console',
        'Framework :: Flake8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=2.7',
    include_package_data=True,
    keywords='flake8',
    author='Viktor Chaptsev',
    author_email='viktor@chaptsev.ru',
    install_requires=['flake8', 'setuptools'],
    entry_points={
        'flake8.extension': [
            'FKA = flake8_keyword_arguments.checker:KeywordArgumentsChecker',
        ],
    },
    url='https://github.com/llybin/flake8-keyword-arguments',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
