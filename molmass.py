from molmass import Formula

molecula = 'H2O'

formula = Formula(molecula)
massa_molar = formula.mass
composicao_elementar = formula.composition()

print(f'Massa Molar da molécula "{molecula}" = {massa_molar} g/mol\n')
print(composicao_elementar)
