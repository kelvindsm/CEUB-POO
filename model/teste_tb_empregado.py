from empregado import Empregado

empr = Empregado()

def listar():
    lista = empr.read_all()
    for obj in lista:
        print(obj.idt_empregado, '|', obj.mat_empregado, '|', obj.nme_empregado, '|',obj.sts_empregado, '|', obj.tel_empregado, '|', obj.rml_empregado, '|', obj.pwd_empregado)

emp = empr.new_object()
emp.eml_empregado = 'carlos.alberto@ceub.com'
emp.mat_empregado = '9987654321'
emp.nme_empregado = 'Carlos Alberto'
emp.sts_empregado = 'A'
emp.tel_empregado = '3123134'
emp.rml_empregado = '1231431124'
emp.pwd_empregado = 'naoesenha'
empr.insert(emp)
print(emp.idt_empregado)

emp = empr.new_object()
emp.eml_empregado = 'fernanda.costa@ceub.com'
emp.mat_empregado = '5555554321'
emp.nme_empregado = 'Fernanda Costa'
emp.sts_empregado = 'A'
emp.tel_empregado = '12471346'
emp.rml_empregado = '1231433334'
emp.pwd_empregado = 'talvezesenha'
empr.insert(emp)
print(emp.idt_empregado)

emp = empr.new_object()
emp.eml_empregado = 'roberto.alves@ceub.com'
emp.mat_empregado = '6529754321'
emp.nme_empregado = 'Roberto Alves'
emp.sts_empregado = 'I'
emp.tel_empregado = '125923536'
emp.rml_empregado = '1241823161'
emp.pwd_empregado = 'nuncaserasenha'

empr.insert(emp)
print(emp.idt_empregado)

listar()
