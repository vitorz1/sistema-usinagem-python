from database import Database

class SistemaUsinagem: 
    def __init__(self):
        
        self.db = Database()

    def adicionar_peca_estoque(self, nome, numeracao, qtd, maquina):

        sql = '''
             INSERT INTO estoque (nome_peca, numeracao, quantidade, maquina)
             VALUES (?, ?, ?, ?)
            
            '''
        
        self.db.cursor.execute(sql,  (nome, numeracao, qtd, maquina))
        self.db.conn.commit()

        print(f" Peça '{nome}' adicionada ao estoque. ")

    
    def listar_estoque(self):

        self.db.cursor.execute("SELECT * FROM estoque")
        return self.db.cursor.fetchall()
    


    def cadastrar_pedido(self, id_cliente, id_peca, qtd, maquina, status):

        sql = '''
            INSERT INTO pedidos (id_cliente, id_peca, quantidade_pedida, maquina, status) 
            VALUES (?, ?, ?, ?, ?)               
            
            '''
        
        self.db.cursor.execute(sql, (id_cliente, id_peca, qtd, maquina, status))
        self.db.conn.commit()

        print(f" Pedido do cliente '{id_cliente}' registrado em produção. ")


    def visualizar_producao(self):
        
        sql = "SELECT id, id_cliente, id_peca, quantidade_pedida, maquina, status FROM pedidos"

        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()
    

    def atualizar_pedido(self, pedido_id, nova_maquina, novo_status):
        sql = "UPDATE pedidos SET maquina = ?, status = ? WHERE id = ?"
        self.db.cursor.execute(sql,(nova_maquina, novo_status, pedido_id))
        self.db.conn.commit()
        
        print(f" Pedido #{pedido_id} atualizado com sucesso! ")


    def deletar_pedido(self, pedido_id):

        sql = "DELETE FROM pedidos WHERE id = ?"
        self.db.cursor.execute(sql, (pedido_id,))
        self.db.conn.commit()
        
        print(f" Pedido #{pedido_id} removido do sistema. ")