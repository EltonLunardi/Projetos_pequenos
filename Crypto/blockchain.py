import random
import copy
import hashlib
import json
import sys


def hashMe(msg=""):
    # Por conveniência, esta é uma função auxiliar que envolve nosso algoritmo de hash
    if type(msg) != str:
        # Se não classificarmos as chaves, não podemos garantir a repetibilidade!
        msg = json.dumps(msg, sort_keys=True)

    if sys.version_info.major == 2:
        return str(hashlib.sha256(msg).hexdigest(), 'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()


random.seed(0)


def makeTransaction(maxValue=3):
    # Criara transações validas no range de (1,maxValue)
    sign = int(random.getrandbits(1))*2 - 1   # Escolha aleatória de -1 e 1
    amount = random.randint(1, maxValue)
    eltonPays = sign * amount
    JoaoPays = -1 * eltonPays
    # Por construção, isso sempre retornará transações que respeitam a conservação de tokens.
    # No entanto, observe que não fizemos nada para verificar se eles estão no cheque especial de uma conta
    return {u'Elton': eltonPays, u'Joao': JoaoPays}


txnBuffer = [makeTransaction() for i in range(30)]


def updateState(txn, state):
    # Entradas: txn, state: dicionários digitados com nomes de contas, contendo valores numéricos para valor de transferência (txn) ou saldo de conta (state)
    # Retorna: estado atualizado, com usuários adicionais adicionados ao estado, se necessário
    # NOTA: Isso não valida a transação - apenas atualiza o estado!

    # Se a transação for válida, atualize o estado

    # Como os dicionários são mutáveis, vamos evitar qualquer confusão criando uma cópia de trabalho dos dados.
    state = state.copy()
    for key in txn:
        if key in state.keys():
            state[key] += txn[key]
        else:
            state[key] = txn[key]
    return state


def isValidTxn(txn, state):
    # Assuma que a transação é um dicionário digitado por nomes de contas

    # Verifique se a soma dos depósitos e saques é 0
    if sum(txn.values()) != 0:
        return False

    # Verifique se a transação não causa um cheque especial
    for key in txn.keys():
        if key in state.keys():
            acctBalance = state[key]
        else:
            acctBalance = 0
        if (acctBalance + txn[key]) < 0:
            return False

    return True


state = {u'Elton': 5, u'Joao': 5}

# Transação básica-
print(isValidTxn({u'Elton': -3, u'Joao': 3}, state))
# Mas não podemos criar ou destruir tokens!
print(isValidTxn({u'Elton': -4, u'Joao': 3}, state))
# Também não podemos fazer saques a descoberto em nossa conta.
print(isValidTxn({u'Elton': -6, u'Joao': 6}, state))
# A criação de novos usuários é válida
print(isValidTxn({u'Elton': -4, u'Joao': 2, 'Cleitin': 2}, state))
# Mas as mesmas regras ainda se aplicam!
print(isValidTxn({u'Elton': -4, u'Joao': 3, 'Cleitin': 2}, state))

state = {u'Elton': 50, u'Joao': 50}  # Define o estado inicial
genesisBlockTxns = [state]
genesisBlockContents = {u'blockNumber': 0, u'parentHash': None,
                        u'txnCount': 1, u'txns': genesisBlockTxns}
genesisHash = hashMe(genesisBlockContents)
genesisBlock = {u'hash': genesisHash, u'contents': genesisBlockContents}
genesisBlockStr = json.dumps(genesisBlock, sort_keys=True)

chain = [genesisBlock]


def makeBlock(txns, chain):
    parentBlock = chain[-1]
    parentHash = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    txnCount = len(txns)
    blockContents = {u'blockNumber': blockNumber, u'parentHash': parentHash,
                     u'txnCount': len(txns), 'txns': txns}
    blockHash = hashMe(blockContents)
    block = {u'hash': blockHash, u'contents': blockContents}

    return block


blockSizeLimit = 5  # Número arbitrário de transações por bloco-
# isso é escolhido pelo minerador do bloco e pode variar entre os blocos!

while len(txnBuffer) > 0:
    bufferStartSize = len(txnBuffer)

    # Reúna um conjunto de transações válidas para inclusão
    txnList = []
    while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
        newTxn = txnBuffer.pop()
        # Retorna falso se o txn for invalido
        validTxn = isValidTxn(newTxn, state)

        if validTxn:           # Se tivemos um estado valido, not False
            txnList.append(newTxn)
            state = updateState(newTxn, state)
        else:
            print("Transição ignorada!")
            sys.stdout.flush()
            continue  # Esta foi uma transação inválida; ignore e siga em frente

    # Criar um bloco
    myBlock = makeBlock(txnList, chain)
    chain.append(myBlock)

chain[0]
chain[1]

state


def checkBlockHash(block):
    # Gera uma exceção se o hash não corresponder ao conteúdo do bloco
    expectedHash = hashMe(block['contents'])
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block %s' %
                        block['contents']['blockNumber'])
    return


def checkBlockValidity(block, parent, state):
    # Queremos verificar as seguintes condições:
    # - Cada uma das transações são atualizações válidas para o estado do sistema
    # - O hash do bloco é válido para o conteúdo do bloco
    # - O número do bloco incrementa o número do bloco pai em 1
    # - Referencia com precisão o hash do bloco pai
    parentNumber = parent['contents']['blockNumber']
    parentHash = parent['hash']
    blockNumber = block['contents']['blockNumber']

    # Verifique a validade da transação; lançar um erro se uma transação inválida for encontrada.
    for txn in block['contents']['txns']:
        if isValidTxn(txn, state):
            state = updateState(txn, state)
        else:
            raise Exception('Invalid transaction in block %s: %s' %
                            (blockNumber, txn))

    # Verifique a integridade do hash; gera erro se for impreciso
    checkBlockHash(block)

    if blockNumber != (parentNumber+1):
        raise Exception(
            'Hash does not match contents of block %s' % blockNumber)

    if block['contents']['parentHash'] != parentHash:
        raise Exception('Parent hash not accurate at block %s' % blockNumber)

    return state


def checkChain(chain):
    # Trabalhe a cadeia do bloco gênese (que recebe tratamento especial),
    # verificando se todas as transações são válidas internamente,
    # que as transações não causem um cheque especial,
    # e que os blocos estão ligados por seus hashes.
    # Isso retorna o estado como um dicionário de contas e saldos,
    # ou retorna False se um erro foi detectado

    # Processamento de entrada de dados: certifique-se de que nossa cadeia seja uma lista de dicts
    if type(chain) == str:
        try:
            chain = json.loads(chain)
            assert (type(chain) == list)
        except:  # Este é um catch-all, reconhecidamente bruto
            return False
    elif type(chain) != list:
        return False

    state = {}
    # Prepare a bomba verificando o bloco de gênese
    # Queremos verificar as seguintes condições:
    # - Cada uma das transações são atualizações válidas para o estado do sistema
    # - O hash do bloco é válido para o conteúdo do bloco

    for txn in chain[0]['contents']['txns']:
        state = updateState(txn, state)
    checkBlockHash(chain[0])
    parent = chain[0]

    # Verificando blocos subseqüentes: Estes também precisam verificar
    # - a referência ao hash do bloco pai
    # - a validade do número do bloco
    for block in chain[1:]:
        state = checkBlockValidity(block, parent, state)
        parent = block

    return state


checkChain(chain)

chainAsText = json.dumps(chain, sort_keys=True)
checkChain(chainAsText)

nodeBchain = copy.copy(chain)
nodeBtxns = [makeTransaction() for i in range(5)]
newBlock = makeBlock(nodeBtxns, nodeBchain)

print("Blockchain no nó A tem %s blocos de comprimento" % len(chain))

try:
    print("Novo Bloco recebido; checando validade...")
    # Atualize o estado - isso gerará um erro se o bloco for inválido!
    state = checkBlockValidity(newBlock, chain[-1], state)
    chain.append(newBlock)
except:
    print("Bloco invalido; ignorando e esperando o próximo bloc...")

print("Blockchain no nó A tem %s blocos de comprimento" % len(chain))
