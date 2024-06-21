# Aluno: Arthur Mendes
# Curso: Análise e Desenvolvimento de Sistemas

import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None


def save_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def aluno_existe(students, code, cpf):
    for student in students:
        if student["code"] == code or student["cpf"] == cpf:
            return True
    return False

def disciplina_existe(disciplines, code, name):
    for discipline in disciplines:
        if discipline["code"] == code or discipline["name"] == name:
            return True
    return False

def professor_existe(teachers, code, cpf, name):
    for teacher in teachers:
        if teacher["code"] == code or teacher["cpf"] == cpf or teacher["name"] == name:
            return True
    return False

def turma_existe(classes, code):
    for class_ in classes:
        if class_["code"] == code:
            return True
    return False

def matricula_existe(enrollments, student_code, class_code):
    for enrollment in enrollments:
        if enrollment["student_code"] == student_code and enrollment["class_code"] == class_code:
            return True
    return False

def main():
    # Carrega os dados do arquivo JSON
    data = load_data('data.json')
    if data is not None:
        students = data.get('students', [])
        disciplines = data.get('disciplines', [])
        teachers = data.get('teachers', [])
        classes = data.get('classes', [])
        enrollments = data.get('enrollments', [])
    else:
        students = []
        disciplines = []
        teachers = []
        classes = []
        enrollments = []

    while True:
        print("\n\n---- MENU PRINCIPAL ----")
        print("1. Menu de Estudantes")
        print("2. Menu de Disciplinas")
        print("3. Menu de Professores")
        print("4. Menu de Turmas")
        print("5. Menu de Matrículas")
        print("6. Sair")
        option = input("\nDigite a opção desejada: ")

        if option == "1":
            # Menu de Estudantes
            print("\n\n---- MENU DE ESTUDANTES ----")
            while True:
                print("\n\nMenu de Estudantes:")
                print("1. Cadastrar Estudante")
                print("2. Listar Estudantes")
                print("3. Excluir Estudante")
                print("4. Editar Estudante")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    # Cadastrar Estudante
                    print("Cadastrar Estudante")
                    code = int(input("Digite o código do estudante: "))
                    cpf = input("Digite o CPF do estudante: ")
                    if aluno_existe(students, code, cpf):
                        print("Informação já cadastrada. Tente com outros dados!")
                        continue
                    name = input("Digite o nome do estudante: ")
                    student = {"code": code, "name": name, "cpf": cpf}
                    students.append(student)
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                    print(f"Estudante {student['name']} cadastrado com sucesso!")
                elif option == "2":
                    # Listar Estudantes
                    print("Listar Estudantes")
                    print("Lista de Estudantes:")
                    for student in students:
                        print(f"Código: {student['code']} - Nome: {student['name']} - CPF: {student['cpf']}")
                elif option == "3":
                    # Excluir Estudante
                    print("Excluir Estudante")
                    code = int(input("Digite o código do estudante que deseja excluir: "))
                    students = [s for s in students if s["code"] != code]
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                elif option == "4":
                    # Editar Estudante
                    print("Editar Estudante")
                    code = int(input("Digite o código do estudante que deseja editar: "))
                    for student in students:
                        if student["code"] == code:
                            new_code = int(input("Digite o novo código: "))


                            new_cpf = input("Digite o novo CPF: ")
                            if aluno_existe(students, new_code, new_cpf):
                                print("Informação já cadastrada. Tente com outros dados!")
                                break
                            new_name = input("Digite o novo nome: ")
                            student["code"] = new_code
                            student["name"] = new_name
                            student["cpf"] = new_cpf
                            save_data('data.json',
                                      {'students': students, 'disciplines': disciplines, 'teachers': teachers,
                                       'classes': classes, 'enrollments': enrollments})
                            print(f"Estudante {student['name']} editado com sucesso!")
                            break
                    else:
                        print("Estudante não encontrado")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

        elif option == "2":
            # Menu de Disciplinas
            print("\n\n---- MENU DE DISCIPLINAS ----")
            while True:
                print("\n\nMenu de Disciplinas:")
                print("1. Cadastrar Disciplina")
                print("2. Listar Disciplinas")
                print("3. Excluir Disciplina")
                print("4. Editar Disciplina")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    # Cadastrar Disciplina
                    print("Cadastrar Disciplina")
                    code = int(input("Digite o código da disciplina: "))
                    name = input("Digite o nome da disciplina: ")
                    if disciplina_existe(disciplines, code, name):
                        print("Informação já cadastrada. Tente com outros dados!")
                        continue
                    discipline = {"code": code, "name": name}
                    disciplines.append(discipline)
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                    print(f"Disciplina {discipline['name']} cadastrada com sucesso!")
                elif option == "2":
                    # Listar Disciplinas
                    print("Listar Disciplinas")
                    print("Lista de Disciplinas:")
                    for discipline in disciplines:
                        print(f"Código: {discipline['code']} - Nome: {discipline['name']}")
                elif option == "3":
                    # Excluir Disciplina
                    print("Excluir Disciplina")
                    code = int(input("Digite o código da disciplina que deseja excluir: "))
                    disciplines = [d for d in disciplines if d["code"] != code]
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                elif option == "4":
                    # Editar Disciplina
                    print("Editar Disciplina")
                    code = int(input("Digite o código da disciplina que deseja editar: "))
                    for discipline in disciplines:
                        if discipline["code"] == code:
                            new_code = int(input("Digite o novo código: "))
                            new_name = input("Digite o novo nome: ")
                            if disciplina_existe(disciplines, new_code, new_name):
                                print("Informação já cadastrada. Tente com outros dados!")
                                break
                            discipline["code"] = new_code
                            discipline["name"] = new_name
                            save_data('data.json',
                                      {'students': students, 'disciplines': disciplines, 'teachers': teachers,
                                       'classes': classes, 'enrollments': enrollments})
                            print(f"Disciplina {discipline['name']} editada com sucesso!")
                            break
                    else:
                        print("Disciplina não encontrada")

                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "3":
            # Menu de Professores
            print("\n\n---- MENU DE PROFESSORES ----")
            while True:
                print("\n\nMenu de Professores:")
                print("1. Cadastrar Professor")
                print("2. Listar Professores")
                print("3. Excluir Professor")
                print("4. Editar Professor")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    # Cadastrar Professor
                    print("Cadastrar Professor")
                    code = int(input("Digite o código do professor: "))
                    cpf = input("Digite o CPF do professor: ")
                    name = input("Digite o nome do professor: ")
                    if professor_existe(teachers, code, cpf, name):
                        print("Informação já cadastrada. Tente com outros dados!")


                        continue
                    teacher = {"code": code, "name": name, "cpf": cpf}
                    teachers.append(teacher)
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                    print(f"Professor {teacher['name']} cadastrado com sucesso!")
                elif option == "2":
                    # Listar Professores
                    print("Listar Professores")
                    print("Lista de Professores:")
                    for teacher in teachers:
                        print(f"Código: {teacher['code']} - Nome: {teacher['name']} - CPF: {teacher['cpf']}")
                elif option == "3":
                    # Excluir Professor
                    print("Excluir Professor")
                    code = int(input("Digite o código do professor que deseja excluir: "))
                    teachers = [t for t in teachers if t["code"] != code]
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                elif option == "4":
                    # Editar Professor
                    print("Editar Professor")
                    code = int(input("Digite o código do professor que deseja editar: "))
                    for teacher in teachers:
                        if teacher["code"] == code:
                            new_code = int(input("Digite o novo código: "))
                            new_name = input("Digite o novo nome: ")
                            new_cpf = input("Digite o novo CPF: ")
                            if professor_existe(teachers, new_code, new_cpf, new_name):
                                print("Informação já cadastrada. Tente com outros dados!")
                                break
                            teacher["code"] = new_code
                            teacher["name"] = new_name
                            teacher["cpf"] = new_cpf
                            save_data('data.json',
                                      {'students': students, 'disciplines': disciplines, 'teachers': teachers,
                                       'classes': classes, 'enrollments': enrollments})
                            print(f"Professor {teacher['name']} editado com sucesso!")
                            break
                    else:
                        print("Professor não encontrado")

                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "4":
            # Menu de Turmas
            print("\n\n---- MENU DE TURMAS ----")
            while True:
                print("\n\nMenu de Turmas:")
                print("1. Cadastrar Turma")
                print("2. Listar Turmas")
                print("3. Excluir Turma")
                print("4. Editar Turma")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    # Cadastrar Turma
                    print("Cadastrar Turma")
                    code = int(input("Digite o código da turma: "))
                    if turma_existe(classes, code):
                        print("Informação já cadastrada. Tente com outros dados!")
                        continue
                    name = input("Digite o nome da turma: ")
                    class_ = {"code": code, "name": name}
                    classes.append(class_)
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                    print(f"Turma {class_['name']} cadastrada com sucesso!")
                elif option == "2":
                    # Listar Turmas
                    print("Listar Turmas")
                    print("Lista de Turmas:")
                    for class_ in classes:
                        print(f"Código: {class_['code']} - Nome: {class_['name']}")
                elif option == "3":
                    # Excluir Turma
                    print("Excluir Turma")
                    code = int(input("Digite o código da turma que deseja excluir: "))
                    classes = [c for c in classes if c["code"] != code]
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                elif option == "4":
                    # Editar Turma
                    print("Editar Turma")
                    code = int(input("Digite o código da turma que deseja editar: "))
                    for class_ in classes:
                        if class_["code"] == code:
                            new_code = int(input("Digite o novo código: "))
                            new_name = input("Digite o novo nome: ")
                            if turma_existe(classes, new_code):
                                print("Informação já cadastrada. Tente com outros dados!")
                                break
                            class_["code"] = new_code
                            class_["name"] = new_name
                            save_data('data.json',
                                      {'students': students, 'disciplines': disciplines, 'teachers': teachers,


                                       'classes': classes, 'enrollments': enrollments})
                            print(f"Turma {class_['name']} editada com sucesso!")
                            break
                    else:
                        print("Turma não encontrada")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "5":
            # Menu de Matrículas
            print("\n\n---- MENU DE MATRÍCULAS ----")
            while True:
                print("\n\nMenu de Matrículas:")
                print("1. Matricular Estudante em Turma")
                print("2. Listar Matrículas")
                print("3. Cancelar Matrícula")
                print("4. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    # Matricular Estudante em Turma
                    print("Matricular Estudante em Turma")
                    student_code = int(input("Digite o código do estudante: "))
                    class_code = int(input("Digite o código da turma: "))
                    if not aluno_existe(students, student_code, ""):
                        print("Estudante não encontrado")
                        continue
                    if not turma_existe(classes, class_code):
                        print("Turma não encontrada")
                        continue
                    if matricula_existe(enrollments, student_code, class_code):
                        print("Estudante já matriculado nesta turma")
                        continue
                    enrollment = {"student_code": student_code, "class_code": class_code}
                    enrollments.append(enrollment)
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                    print("Estudante matriculado com sucesso!")
                elif option == "2":
                    # Listar Matrículas
                    print("Listar Matrículas")
                    print("Lista de Matrículas:")
                    for enrollment in enrollments:
                        student_name = [s['name'] for s in students if s['code'] == enrollment['student_code']][0]
                        class_name = [c['name'] for c in classes if c['code'] == enrollment['class_code']][0]
                        print(f"Estudante: {student_name} - Turma: {class_name}")
                elif option == "3":
                    # Cancelar Matrícula
                    print("Cancelar Matrícula")
                    student_code = int(input("Digite o código do estudante: "))
                    class_code = int(input("Digite o código da turma: "))
                    if not matricula_existe(enrollments, student_code, class_code):
                        print("Matrícula não encontrada")
                        continue
                    enrollments = [e for e in enrollments if e["student_code"] != student_code or e["class_code"] != class_code]
                    save_data('data.json', {'students': students, 'disciplines': disciplines, 'teachers': teachers, 'classes': classes, 'enrollments': enrollments})
                    print("Matrícula cancelada com sucesso!")
                elif option == "4":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()