from block import Block


class BlockChain:

    def __init__(self):
        self.blockchain = []

    def add_block(self, data):
        try:

            if len(self.blockchain) == 0:
                block = Block(data)

            else:
                previous_block = self.blockchain[-1]
                previous_hash_string = previous_block.hash
                previous_time_stamp = previous_block.timestamp
                block = Block(data, previous_hash_string)

                if block.timestamp == previous_time_stamp:
                    print("You Can't add blocks with the same timestamp")
                    return

            self.blockchain.append(block)

        except ValueError as err:
            print(err)

    def __repr__(self):

        if len(self.blockchain) == 0:
            return "Blockchain is empty"

        blockchain_content = ''

        for block in self.blockchain:
            blockchain_content += f"Blockchain data: {str(block.data)} {str(block.timestamp)} \n"

        return blockchain_content
