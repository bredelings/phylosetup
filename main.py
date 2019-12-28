import enamlx
enamlx.install()

from atom.api import Atom, Str, Range, Bool, Value, Int, Tuple, observe, ContainerList
import enaml
from enaml.qt.qt_application import QtApplication

class Partition(Atom):
    """ A simple class representing a partition in a phylogenetic analysis.

    """
    filename = Str()

    debug = Bool(False)

    alphabet = Str()

    substitution_model = Int()

    indel_model = Int()

    scale_model = Int()

class SubstitutionModel(Atom):
    model = Str()

    alphabet = Str()

class IndelModel(Atom):
    model = Str()

class ScaleModel(Atom):
    model = Str()

class Alphabet(Atom):
    model = Str()

class BranchLengthModel(Atom):
    model = Str()

class TaxonSet(Atom):
    taxa = ContainerList(Str)

class ATModel(Atom):
    """A collection of partitions that can share models

    """

    partitions = ContainerList(Partition)
    smodels = ContainerList(SubstitutionModel)
    imodels = ContainerList(IndelModel)
    scales = ContainerList(ScaleModel)
    taxon_set = TaxonSet()

    # branch_lengths = BranchLengthModel()
    def add_partition(self, filename, alpha):
        smodel = None
        if alpha == "DNA" or alpha == "RNA":
            smodel = len(self.smodels)
            self.smodels.append(SubstitutionModel(model='tn93',alphabet=alpha))
        elif alpha == "Amino Acids":
            smodel = len(self.smodels)
            self.smodels.append(SubstitutionModel(model='lg08',alphabet=alpha))

        imodel = len(self.imodels)
        self.imodels.append(IndelModel(model='rs07'))

        scale = len(self.scales)
        self.scales.append(ScaleModel(model='~gamma[0.5,2]'))

        partition = Partition(filename = filename, alphabet = alpha, substitution_model = smodel, indel_model = imodel, scale_model = scale)
        self.partitions.append(partition)

    def remove_partition(self):
        if len(self.partitions) > 0:
            self.partitions.pop()


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
