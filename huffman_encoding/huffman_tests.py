from huffman import huffman_encoding
from huffman import huffman_decoding
import sys


def test_huffman(data):
    encoded_data, tree = huffman_encoding(data)

    if encoded_data is None:
        print("Nothing can be encoded")
        return

    print("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print("The content of the data is: {}\n".format(data))

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))

    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))

    print("The content of the decoded data is: {}\n".format(decoded_data))
    print("\n")


test_huffman("The bird is the word")

test_huffman('')
test_huffman('A')
test_huffman('AA')
test_huffman('AAAAA')
