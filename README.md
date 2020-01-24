# phylosetup
Simple GUI to create phylogenetic analysis scripts

## Linux installation

### First install Enaml
``` sh
apt-get install python3-qt5
apt-get install libpyside2-py3-5.14
mkvirtualenv phylosetup -p $(which python3) --system-site-packages
workon phylosetup
pip install enaml enamlx bio
```

It might be necessary to install the apt-based packages _before_ doing the `pip install`.


## Running the program

```
workon phylosetup
python partition.py
```

You should then be able to load the file `data/25-muscle.fasta`.
