###
# \file setup.py
#
# Install with symlink: 'pip install -e .'
# Changes to the source file will be immediately available to other users
# of the package
#
# \author     Michael Ebner (michael.ebner.14@ucl.ac.uk)
# \date       July 2017
#

import os

from setuptools import setup, find_packages

#with open("README.md", "r") as fh:
#    long_description = fh.read()
long_description = "Removed - meant to be README.md"

about = {}
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "nsol", "__about__.py")) as fp:
    exec(fp.read(), about)


def install_requires(fname="requirements.txt"):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    url=about["__uri__"],
    author=about["__author__"],
    author_email=about["__email__"],
    license=about["__license__"],
    packages=find_packages(),
    install_requires=install_requires(),
    zip_safe=False,
    keywords='development numericalsolver convexoptimisation',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: BSD License',

        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'nsol_corrupt_data = nsol.application.corrupt_data:main',
            'nsol_run_deconvolution = nsol.application.run_deconvolution:main',
            'nsol_run_deconvolution_study = nsol.application.run_deconvolution_study:main',
            'nsol_run_denoising = nsol.application.run_denoising:main',
            'nsol_run_denoising_study = nsol.application.run_denoising_study:main',
            'nsol_show_parameter_study = nsol.application.show_parameter_study:main',
        ],
    },

)
