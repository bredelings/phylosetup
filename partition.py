from atom.api import Atom, Str, Range, Bool, Value, Int, Tuple, observe
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

def main():
    # Create an employee with a boss
    partition1 = Partition(
        filename = '25-muscle.fasta', alphabet = 'RNA', substitution_model = 'tn93', indel_model = 'rs07', scale = '~gamma[0.5,2]'
    )

    # Import our Enaml EmployeeView
    with enaml.imports():
        from partition_view import PartitionView

    app = QtApplication()
    # Create a view and show it.
    view = PartitionView(partition=partition1)
    view.show()

    app.start()

if __name__ == '__main__':
    main()
