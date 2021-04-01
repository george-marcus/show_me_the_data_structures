from block import Block


class BlockChain:

    def __init__(self):
        self.blockchain = []

    def add_block(self, data):
        if not data:
            print("You can't add empty values to blockchain")
            return

        if len(self.blockchain) == 0:
            block = Block(data)

        else:
            previous_hash_string = self.blockchain[-1].hash
            block = Block(data, previous_hash_string)

        self.blockchain.append(block)

    def __repr__(self):

        if len(self.blockchain) == 0:
            return "Blockchain is empty"

        blockchain_content = ''

        for block in self.blockchain:
            blockchain_content += f"Blockchain data: {str(block.data)} \n"

        return blockchain_content
