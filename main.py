#!/usr/bin/env python

from os import path
import Bio.SeqRecord

import enamlx
enamlx.install()

from atom.api import Atom, Str, Range, Bool, Value, Int, Tuple, observe, ContainerList
import enaml
from enaml.qt.qt_application import QtApplication

class Partition(Atom):
    """ A simple class representing a partition in a phylogenetic analysis.

    """
    # FIXME: what about number of sites?
    # FIXME: what about "are we aligned"?
    # FIXME: what about "is the alignment fixed or estimated?"
    # FIXME: what about "how many taxa?"
    # Some of these things can be computed from atmodel and shown in the table

    # These may include '-' characters, but should not
    def sequence_lengths(self):
        return [len(x.seq) for x in self.sequences]

    def min_length(self):
        return min(self.sequence_lengths())

    def max_length(self):
        return max(self.sequence_lengths())

    def taxa(self):
        t = [x.id for x in self.sequences]
        t.sort()
        return t

    name = Str()

    sequences = ContainerList(Bio.SeqRecord.SeqRecord)

    filename = Str()

    debug = Bool(False)

    fixed_alignment = Bool(False)

    alphabet = Str()

    substitution_model = Int()

    indel_model = Int()

    scale_model = Int()

class SubstitutionModel(Atom):
    name = Str()

    model = Str()

    alphabet = Str()

class IndelModel(Atom):
    name = Str()

    model = Str()

class ScaleModel(Atom):
    name = Str()

    model = Str()

class Alphabet(Atom):
    model = Str()

class BranchLengthModel(Atom):
    model = Str()

class TaxonSet(Atom):
    taxa = ContainerList(Str)

def default_smodel_for_alphabet(alphabet):
    smodel = None
    if alphabet == "DNA" or alphabet == "RNA":
        smodel = 'tn93'
    elif alphabet == "Amino Acids":
        smodel = 'lg08'
    return smodel;


class ATModel(Atom):
    """A collection of partitions that can share models

    """

    partitions = ContainerList(Partition)
    smodels = ContainerList(SubstitutionModel)
    imodels = ContainerList(IndelModel)
    scales = ContainerList(ScaleModel)
    taxon_set = TaxonSet()

    # branch_lengths = BranchLengthModel()
    def add_partition(self, filename, sequences, alpha):
        sname = 'S{}'.format(len(self.smodels)+1)
        smodel_index = len(self.smodels)
        smodel = default_smodel_for_alphabet(alpha)
        if smodel is None:
            raise ValueError(f"SModel for alphabet '{alpha}' unknown")
        self.smodels.append(SubstitutionModel(name = sname, model=smodel,alphabet=alpha))

        iname = 'I{}'.format(len(self.imodels)+1)
        imodel = len(self.imodels)
        imodel_index = len(self.imodels)
        self.imodels.append(IndelModel(name = iname, model='rs07'))

        rname = 'R{}'.format(len(self.scales)+1)
        scale = len(self.scales)
        scale_index = len(self.scales)
        self.scales.append(ScaleModel(name = rname, model='~gamma[0.5,2]'))

        pname = 'P{}'.format(len(self.partitions)+1)
        partition = Partition(name = pname,
                              sequences = sequences,
                              filename = filename,
                              alphabet = alpha,
                              substitution_model = smodel_index,
                              indel_model = imodel_index,
                              scale_model = scale_index)

        if len(self.partitions) > 0 and partition.taxa() != self.partitions[0].taxa():
            print("Taxon set does not match!")
            return

        self.partitions.append(partition)

    def remove_partition(self):
        if len(self.partitions) > 0:
            self.partitions.pop()

    # remove a specific partition
    # we will need to adjust _names_ for later partitions

    # remove a specific substitution model
    # we will need to adjust _names_ for later models

    # remove a specific indel model
    # we will need to adjust _names_ for later models


def main():

    with enaml.imports():
        from atmodel_notebook import ATModelNotebook

    at_model = ATModel(partitions=[], smodels=[], imodels=[], scales=[])

    app = QtApplication()
    # Create a view and show it.
    view = ATModelNotebook(model = at_model)
    view.show()

    app.start()

if __name__ == '__main__':
    main()
