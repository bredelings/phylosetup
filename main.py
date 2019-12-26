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

    substitution_model = Str()

    indel_model = Str()

    scale = Str()

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

class ATModel(Atom):
    """A collection of partitions that can share models

    """

    partitions = ContainerList(Partition)
    smodels = ContainerList(SubstitutionModel)
    imodels = ContainerList(IndelModel)
    scales = ContainerList(ScaleModel)

    # branch_lengths = BranchLengthModel()
    def add_partition(self):
        partition = Partition(filename = '25-muscle.fasta', alphabet = 'RNA', substitution_model = 'tn93', indel_model = 'rs07', scale = '~gamma[0.5,2]')
        self.partitions.append(partition)

    def remove_partition(self):
        if len(self.partitions) > 0:
            self.partitions.pop()


def main():

    with enaml.imports():
        from partition_view import PartitionView
        from partition_view import PartitionsTab

    data_model = ATModel(partitions=[], smodels=[], imodels=[], scales=[])

    app = QtApplication()
    # Create a view and show it.
    view = PartitionsTab(model = data_model)
    view.show()

    app.start()

if __name__ == '__main__':
    main()
