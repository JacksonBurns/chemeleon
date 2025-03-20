wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz
gunzip CID-SMILES.gz
awk '{print $2}' CID-SMILES > pubchem.smiles
rm CID-SMILES
