from tipo_ocorrencia import TipoOcorrencia

tipo = TipoOcorrencia()

def incluir():
    obj = tipo.new_object()
    obj.nme_tipo_ocorrencia = input('Qual o nome do tipo? ')
    obj.tpo_tipo_ocorrencia = input('E para P-Prestador ou E-Empregado? ')
    obj.sts_tipo_ocorrencia = 'A'
    obj.txt_modelo_ocorrencia = input('Qual o nome do modelo? ')
    tipo.insert(obj)
    print('Incluido tipo: ', obj.idt_tipo_ocorrencia)

def listar():
    lista = tipo.read_all()
    for obj in lista:
        print(obj.idt_tipo_ocorrencia, '|', obj.nme_tipo_ocorrencia, '|', obj.tpo_tipo_ocorrencia)

#incluir()
listar()