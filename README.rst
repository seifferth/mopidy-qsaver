****************************
Mopidy-Qsaver
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-Qsaver.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Qsaver/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-Qsaver.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Qsaver/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/HeadspringLabs/mopidy-qsaver/master.svg?style=flat
    :target: https://travis-ci.org/HeadspringLabs/mopidy-qsaver
    :alt: Travis-CI build status

.. image:: https://img.shields.io/coveralls/HeadspringLabs/mopidy-qsaver/master.svg?style=flat
   :target: https://coveralls.io/r/HeadspringLabs/mopidy-qsaver?branch=master
   :alt: Test coverage


Mopidy extension that maintains your current queue even when the server restarts (currently the queue dies if you restart the server)


Installation
============

For versions of Mopidy >= 1.0.5, install by running the following (or download-install the master branch)::

    pip install Mopidy-Qsaver==0.1.0
    
For Mopidy version 0.19.5, install by running (or download-install the v0.19.5 branch)::

    pip install Mopidy-Qsaver==0.2.6



Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Qsaver to your Mopidy configuration file::

    [qsaver]
    enabled = true
    backup_file = ./tracklist_backup.json


Project resources
=================

- `Source code <https://github.com/bardoloi/mopidy-qsaver>`_
- `Issue tracker <https://github.com/bardoloi/mopidy-qsaver/issues>`_
- `Development branch tarball <https://github.com/bardoloi/mopidy-qsaver/archive/master.tar.gz#egg=Mopidy-Qsaver-dev>`_


Changelog
=========

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.
