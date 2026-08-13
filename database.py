import sqlite3

class Database:
    def __init__(self, db_name="usinagem.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        
        self.cursor.execute('''

            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )

        ''')

        self.cursor.execute('''
                            
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome_peca TEXT NOT NULL,
                numeracao TEXT,
                quantidade INTEGER DEFAULT 0,
                maquina TEXT
            )
          
    ''' )
        
        self.cursor.execute('''

            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                id_peca INTEGER,
                quantidade_pedida INTEGER,
                data_entrada TEXT,
                maquina TEXT,
                status TEXT DEFAULT 'Pendente',
                FOREIGN KEY (id_cliente) REFERENCES clientes (id),
                FOREIGN KEY (id_peca) REFERENCES estoque (id)   
                        
                            
                            
        
            )


        ''')
        self.conn.commit()