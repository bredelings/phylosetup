# phylosetup
Simple GUI to create phylogenetic analysis scripts

## Linux installation

### First install Enaml
``` sh
apt-get install python-qt5
(?) apt-get install libpyside-5.11
mkvirtualenv enaml -p $(which python3) --system-site-packages
workon phylosetup
pip install enaml enamlx bio
```

## Running the program

```
workon phylosetup
python partition.py
```

