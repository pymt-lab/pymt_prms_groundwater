=====================
pymt_prms_groundwater
=====================


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_prms_groundwater-green.svg
        :target: https://anaconda.org/conda-forge/pymt_prms_groundwater

.. image:: https://img.shields.io/travis/csdms/pymt_prms_groundwater.svg
        :target: https://travis-ci.org/csdms/pymt_prms_groundwater

.. image:: https://readthedocs.org/projects/pymt_prms-groundwater/badge/?version=latest
        :target: https://pymt_prms-groundwater.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for the PRMS6 Groundwater component


* Free software: MIT license
* Documentation: https://prms-groundwater.readthedocs.io.




=============== =========================================
Component       PyMT
=============== =========================================
PRMSGroundwater `from pymt.models import PRMSGroundwater`
=============== =========================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

--------------------------------
Installing pymt_prms_groundwater
--------------------------------

Once `pymt` is installed, the dependencies of `pymt_prms_groundwater` can
be installed with:

.. code::

  conda install bmi-fortran=2.0 prms

To install `pymt_prms_groundwater`,

.. code::

  conda install pymt_prms_groundwater
