from blockchain import BlockChain


blockchain = BlockChain()

print(blockchain)
blockchain.add_block(None)
blockchain.add_block('')
print(blockchain)

blockchain.add_block("0")
blockchain.add_block("1")
blockchain.add_block("2")
print(blockchain)
