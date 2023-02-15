import hashlib


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # usa um hash SHA-256 para calcular o hash do bloco
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8') +
                   self.previous_hash.encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def get_latest_block(self):
        return self.chain[-1]


# cria a blockchain
blockchain = Blockchain()

while True:
    print("\nO que você deseja fazer?")
    print("1. Adicionar um novo bloco")
    print("2. Exibir a cadeia de blocos")
    print("3. Sair")
    option = input("\nDigite a opção desejada: ")

    if option == "1":
        data = input("\nDigite os dados do novo bloco: ")
        blockchain.add_block(Block(data, "0"))
        print("\nBloco adicionado à cadeia de blocos!")

    elif option == "2":
        # exibe a cadeia de blocos
        for block in blockchain.chain:
            print("Dados: ", block.data)
            print("Hash: ", block.hash)
            print("Hash anterior: ", block.previous_hash)
            print("\n")

    elif option == "3":
        break

    else:
        print("Opção inválida. Tente novamente.")