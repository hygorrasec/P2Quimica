# import RDKit ----------------------------------------------------------------
from rdkit import Chem
from rdkit.Chem import Draw

# define the smiles string and covert it into a molecule sturcture ------------
water = '[H]O[H]'

mol = Chem.MolFromSmiles(water)

# draw the modecule -----------------------------------------------------------
Draw.MolToFile(mol, 'water.png')

# draw the molecule with property ---------------------------------------------
for i, atom in enumerate(mol.GetAtoms()):
    atom.SetProp("molAtomMapNumber", str(atom.GetIdx()))
    
Draw.MolToFile(mol, 'water_with_prop.png')