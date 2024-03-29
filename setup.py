from setuptools import setup


def read_files(files):
    data = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            data.append(f.read())
    return "\n".join(data)


long_description = read_files(['README.md'])

meta = {}
with open('./src/dpn_py_package/version.py', encoding='utf-8') as f:
    exec(f.read(), meta)

setup(
    name="dpn_py_package",
    description="A small example package, Designed for testing and learning, aimed at enhancing our workflow for increased efficiency.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=meta['__version__'],
    author="Dipen Parmar",
    author_email="dipensavji+pypi@gmail.com",
    url="https://github.com/dipenparmar12/dpn_py_package",
    keywords=['testing', 'python'],
    packages=['dpn_py_package'],
    package_dir={'': 'src'},
    python_requires=">=3.7",
    # entry_points={
    #     "console_scripts": [
    #         "dpn_py_package=dpn_py_package.__main__:cli",
    #     ],
    # },
    # license='BSD-3-Clause',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)