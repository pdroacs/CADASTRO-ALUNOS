from models.aluno import criar_tabela, inserir_aluno, listar_alunos


def menu():
    criar_tabela()
    while True:
        print("\n===== Sistema de Cadastro de Alunos =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            inserir_aluno(nome, idade, curso)
            print("✅ Aluno cadastrado!")
        elif opcao == "2":
            alunos = listar_alunos()
            print("\n📋 Lista de alunos:")
            for aluno in alunos:
                print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")
        elif opcao == "3":
            print("👋 Encerrando o sistema.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == '__main__':
    menu()
