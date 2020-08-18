=====
Coupe
=====

-----------------------------------------------------------------
Simple but accurate multi-purpose Cue-Sheet parser based on textX
-----------------------------------------------------------------

.. contents:: Table of Contents

Description
===========

`coupe`_ is a parser for `cue-sheet`_ files, as described in `Appendix A of CDRWIN
user manual`_.

It makes use of `textX`_, a meta-language for building Domain-Specific Languages
or specific file format parsers in `Python`_.

It's free as in `free beer` and distributed under `GNU General Public License v3+`_.

Installation
============

.. code:: bash

  $ pip install coupe


Graphical representation
========================

Meta-model
----------

Export grammar to a file

.. code:: bash

    $ cp coupe/grammar.py grammar.tx
    $ sed -i '/"""$/d' grammar.tx
    $ sed -i '/^#/' grammar.tx

Generate graphical visualization of coupe_ meta-model in `GraphViz`_'s dot format

.. note:: ``dot -> png`` conversion requires `GraphViz`_

.. code:: bash

    $ textx generate grammar.tx --target dot
    $ dot -Tpng -O grammar.dot

.. image:: images/metamodel-graphviz.png
    :width: 600px
    :alt: Meta-model in GraphViz format

Generate graphical visualization of coupe_ meta-model in `PlantUML`_'s pu format

.. note:: ``pu -> png`` conversion requires `PlantUML`_

.. code:: bash

    $ textx generate grammar.tx --target PlantUML
    $ plantuml grammar.pu

.. image:: images/metamodel-plantuml.png
    :width: 600px
    :alt: Meta-model in PlantUML format

Cleanup

.. code:: bash

    $ rm grammar.*

Model
-----

Simple example from `Cue sheet page`_ on the `Hydrogenaudio Knowledgebase web site`_:

.. code:: bash

    $ cat examples/test1.cue

.. code::

    REM GENRE Alternative
    REM DATE 1991
    REM DISCID 860B640B
    REM COMMENT "ExactAudioCopy v0.95b4"
    PERFORMER "My Bloody Valentine"
    TITLE "Loveless"
    FILE "My Bloody Valentine - Loveless.wav" WAVE
        TRACK 01 AUDIO
            TITLE "Only Shallow"
            PERFORMER "My Bloody Valentine"
            INDEX 01 00:00:00
            TRACK 02 AUDIO
            TITLE "Loomer"
            PERFORMER "My Bloody Valentine"
            INDEX 01 04:17:52

Copy example file to current directory

.. code:: bash

    $ cp examples/test1.cue .

Generate graphical visualization of test1.cue in `GraphViz`_'s dot format

.. note:: ``dot -> png`` conversion requires `GraphViz`_

.. code:: bash

    $ textx generate test1.cue --grammar grammar.tx --target dot
    $ dot -Tpng -O test1.dot

.. image:: images/test1-graphviz.png
    :width: 600px
    :alt: Meta-model in GraphViz format

Cleanup

.. code:: bash

    $ rm test1.*

Usage
=====

Let's re-use our previous example.

First, we use coupe demonstration script

.. code:: bash

    $ python -m coupe examples/test1.cue
    GENRE Alternative
    DISCID 860B640B
    COMMENT ExactAudioCopy v0.95b4
    PERFORMER My Bloody Valentine
    CATALOG 6578765325689
    TITLE Loveless
    DATE 1991
    FILE My Bloody Valentine - Loveless.wav WAVE
     * TRACK 01 AUDIO
      - TITLE Only Shallow
      - PERFORMER My Bloody Valentine
      - ISRC ABCDE1234567
      - FLAGS 4CH PRE
     * TRACK 02 AUDIO
      - TITLE Loomer
      - PERFORMER My Bloody Valentine
      - ISRC FRZ119220350
      - FLAGS 4CH PRE


Then we can use coupe as a library and browse parsed data

.. code:: python

    >>> from coupe import model_from_file
    >>> model = model_from_file("examples/test1.cue")
    >>> model.infos
    {'GENRE': <REMIdOrString:GENRE>, 'DISCID': <REMDiscId:DISCID>, 'COMMENT': <REMIdOrString:COMMENT>, 'PERFORMER': <MetaTag:PERFORMER>, 'CATALOG': <Catalog:CATALOG>, 'TITLE': <MetaTag:TITLE>, 'DATE': <REMDate:DATE>}
    >>> model.infos['DATE']
    <REMDate:DATE>
    >>> model.infos['DATE'].value
    '1991'
    >>> model.infos['GENRE'].value
    'Alternative'
    >>> model.files
    {'My Bloody Valentine - Loveless.wav': <File:My Bloody Valentine - Loveless.wav>}
    >>> model.files['My Bloody Valentine - Loveless.wav'].tracks
    [<textx:Track instance at 0x6aa0ed115670>, <textx:Track instance at 0x6aa0ed1156a0>]
    >>> [f"{t.number} {t.datatype}" for t in model.files["My Bloody Valentine - Loveless.wav"].tracks]
    ['01 AUDIO', '02 AUDIO']

.. _cue-sheet: https://en.wikipedia.org/wiki/Cue_sheet_(computing)
.. _Appendix A of CDRWIN user manual: https://web.archive.org/web/20070614044112/http://www.goldenhawk.com/download/cdrwin.pdf
.. _textX: https://github.com/textX/textX
.. _Python: https://www.python.org/
.. _GNU General Public License v3+: https://www.gnu.org/licenses/gpl-3.0.en.html
.. _GraphViz: https://www.graphviz.org/
.. _PlantUML: https://plantuml.com/
.. _Cue sheet page: http://wiki.hydrogenaud.io/index.php?title=Cue_sheet
.. _Hydrogenaudio Knowledgebase web site: http://wiki.hydrogenaud.io/index.php
