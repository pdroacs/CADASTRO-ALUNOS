from models.aluno import criar_tabela, inserir_aluno, listar_alunos, atualizar_aluno, remover_aluno


def menu():
    criar_tabela()
    while True:
        print("\n===== Sistema de Cadastro de Alunos =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Editar aluno")
        print("4 - Remover aluno")
        print("5 - Sair")

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
            id_aluno = int(input("ID do aluno a editar: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            curso = input("Novo curso: ")
            atualizar_aluno(id_aluno, nome, idade, curso)
            print("✅ Aluno atualizado!")

        elif opcao == "4":
            id_aluno = int(input("ID do aluno a remover: "))
            remover_aluno(id_aluno)
            print("🗑️ Aluno removido com sucesso!")
        elif opcao == '5':
            print("👋 Encerrando o sistema.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == '__main__':
    menu()
