from setuptools import setup, find_packages

setup(
    name='mandelbrot',
    version='1.0.0',
    author='Your Name',
    author_email='your@email.com',
    description='A project for generating Mandelbrot fractals',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'numpy',
        'jupyter',
        'ipympl',

    ],
)
