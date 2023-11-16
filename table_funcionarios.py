import psycopg2

# classe de funcionarios
class FuncionarioDB:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()
        self._criar_tabela()

    # criar tabela caso nao exista
    def _criar_tabela(self):
        try:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS cad_funcionarios (
                    user_id serial PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    data_contratação TIMESTAMP NOT NULL,
                    idade INTEGER CHECK (idade >= 18),
                    salario INTEGER NOT NULL
                );
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            # printa o erro caso a tabela já exista
            print(error)

    # inserir novos dados
    def _inserir_dados(self, dados_para_inserir):
        insert_data_query = """
            INSERT INTO cad_funcionarios (user_id, nome, data_contratação, idade, salario)
            VALUES (%s, %s, %s, %s, %s);
        """
        self.cursor.execute(insert_data_query, dados_para_inserir)
        self.connection.commit()

    # consultando dados 
    def _consultar_dados(self):
        consulta_query = "SELECT * FROM cad_funcionarios;"
        self.cursor.execute(consulta_query)
        dados = self.cursor.fetchall()
        return dados

    # Atualizar dados
    def _atualizar_dados(self, user_id, idade):
        atualizacao_query = "UPDATE cad_funcionarios SET idade = %s WHERE user_id = %s;"
        self.cursor.execute(atualizacao_query, (idade, user_id))
        self.connection.commit()

    # Excluir dados
    def _excluir_dados(self, user_id_para_excluir):
        exclusao_query = "DELETE FROM cad_funcionarios WHERE user_id = %s;"
        self.cursor.execute(exclusao_query, (user_id_para_excluir,))
        self.connection.commit()

    # fechar conexao
    def _fechar_conexao(self):
        self.cursor.close()
        self.connection.close()
        print('Operação concluída com sucesso.')


if __name__ == "__main__":

    # Exemplo de utilização da classe
    funcionario_db = FuncionarioDB(
        host='localhost',
        database='clinicavision',
        user='postgres',
        password='12345'
    )
    
    # ----  CHAMANDO AS OPERAÇÕES CRUD DA CLASSE FUNCIONARIOS ----

    # # inserir dados
    # dados_para_inserir = [
    #     # (123462, 'Carlos Alberto', '2023-08-02', 45, 1850),
    #     (123460, 'Leandro', '2023-05-10', 32, 1550),
    #     (123465, 'Fernanda', '2023-06-09', 19, 1500),
    #     # Adicione mais tuplas de dados conforme necessário
    # ]

    # for dados in dados_para_inserir:
    #     funcionario_db._inserir_dados(dados)
        
    # # Consultar dados
    # dados_consultados = funcionario_db._consultar_dados()
    # print("Dados na tabela:")
    # for dado in dados_consultados:
    #     print(dado)

    # # Atualizar dados
    # user_id = 123460
    # idade = 25
    # funcionario_db._atualizar_dados(user_id, idade)

    # # Consultar dados após atualização
    # dados_atualizados = funcionario_db._consultar_dados()
    # print("\nDados após a atualização:")
    # for dado in dados_atualizados:
    #     print(dado)

    # # Excluir dados
    # user_id_para_excluir = 123460
    # funcionario_db._excluir_dados(user_id_para_excluir)

    # # Consultar dados após exclusão
    # dados_apos_exclusao = funcionario_db._consultar_dados()
    # print("\n Dados após a exclusão:")
    # for dado in dados_apos_exclusao:
    #     print(dado)

    funcionario_db._fechar_conexao()
