import datetime as _dt
import hashlib as _hashlib
import json as _json
from operator import truediv
from this import d

class Blockchain:
    def __init__(self) :
        self.chain = list()
        genesis_block = self._create_block(
            data="i am the genesis block", proof=1, previous_hash="0", index=1
        )
        self.chain.append(genesis_block)

    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = self.proof_of_work(previous_proof = previous_proof, index = index, data = data)
        #pass

    def _to_digest(
        self, new_proof: int, previous_proof: int, index: str, data: str
        ) -> bytes:
        to_digest = str(index) + data
        return to_digest.encode()        

    def proof_of_work(self, previous_proof: str, index: int, data: str) -> int:
        new_proof = 1,
        check_proof = False

        while not check_proof:
            print(new_proof)
            to_digest =  self._to_digest(new_proof, previous_proof, index, data)
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            if hash_value[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
                
        return new_proof

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash,
        }

        return block
