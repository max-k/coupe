#!/bin/bash

function _exit() {
    local status="$1"
    rm -f grammar.*
    rm -r test1.*
    exit "$status"
}

function _error() {
    local program="$1"
    echo "Please install $program to use this script"
    _exit 1
}

# Exit if textx is not available
if ! textx >/dev/null; then
    _error "TextX"
fi

# Exit if graphviz is not available
if ! dot -? >/dev/null; then
    _error "GraphViz"
fi

# Exit if PlantUML is not available
if ! plantuml -h >/dev/null; then
    _error "PlantUML"
fi

# Prepare temporary grammar file
cp -f coupe/grammar.py grammar.tx
sed -i '/"""$/d' grammar.tx
sed -i '/^#/d' grammar.tx

# Copy temporary example model file
cp -f examples/test1.cue test1.cue

# Generate GraphViz representation of metamodel
textx generate grammar.tx --target dot
dot -Tpng -O grammar.dot
cp grammar.dot.png images/metamodel-graphviz.png

# Generate PlantUML representation of metamodel
textx generate grammar.tx --target PlantUML
plantuml grammar.pu
cp grammar.png images/metamodel-plantuml.png

# Generate GraphViz representation of example model
textx generate test1.cue --grammar grammar.tx --target dot
dot -Tpng -O test1.dot
cp test1.dot.png images/test1-graphviz.png

_exit 0
