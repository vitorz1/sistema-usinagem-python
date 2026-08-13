import socket
import sqlite3
from datetime import datetime

DB_NAME = "usinagem.db"
HOST = '0.0.0.0'
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"[*] Servidor do ERP ativo e á escuta na porta {PORT}... ")
print(f"[*] Aguardando atualizações de status das máquinas de fábrica...\n ")

try: 
    while True:
        data, addr = sock.recvfrom(1024)
        mensagem = data.decode('utf-8').strip()

        horario = datetime.now().strftime('%H:%M:%S')
        print(f"[{horario}] Mensagem recebida de {addr}: '{mensagem}'")

        if ":" in mensagem:
            id_maquina, novo_status = mensagem.split(":")

            if "TC" in id_maquina and " " not in id_maquina:
                id_maquina = id_maquina.replace("TC", "TC ")

            try: 
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()

                sql = "UPDATE pedidos SET status = ? WHERE maquina = ? AND status != 'Concluido'"
                cursor.execute(sql, (novo_status, id_maquina))
                conn.commit()

                if cursor.rowcount > 0:
                    print(f" -> [BD] Sucesso! {cursor.rowcount} pedido(s) da máquina '{id_maquina}' atualizado(s) para '{novo_status}'. ")
                
                else: 
                    print(f" -> [BD] Nenhum pedido ativo pendentes para a Máquina '{id_maquina}'. ")

            except sqlite3.Error as erro:
                print(f" -> [ERRO BD] Falha ao atualizar o SQLite: {erro}")

            finally:
                conn.close()

except KeyboardInterrupt:
    print("\n[*] Servidor da Fábrica desligado pelo utilizador. ")

finally: 
    sock.close()
     