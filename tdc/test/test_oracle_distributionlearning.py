from tdc.oracles import Oracle

### one args
one_args_oracle = [ 'validity', 'diversity']

two_args_oracle = ['NOVELTY','fcd', 'kl']



smiles_lst = ['CC(C)(C)[C@H]1CCc2c(sc(NC(=O)COc3ccc(Cl)cc3)c2C(N)=O)C1', \
			  'C[C@@H]1CCc2c(sc(NC(=O)c3ccco3)c2C(N)=O)C1', \
			  'CCNC(=O)c1ccc(NC(=O)N2CC[C@H](C)[C@H](O)C2)c(C)c1', \
			  'C[C@@H]1CCN(C(=O)CCCc2ccccc2)C[C@@H]1O']





for name in one_args_oracle:
	oracle = Oracle(name = name)
	print(oracle(smiles_lst))


for name in two_args_oracle:
	oracle = Oracle(name = name)
	print(oracle(smiles_lst, smiles_lst))
