import hashlib
import json
import time
class Block:
    def __init__(self,index,tstamp,transaction,nonce=0,prevhash=''):
        self.nonce=nonce
        self.index=index
        self.tstamp=tstamp
        self.transaction=transaction
        self.prevhash=prevhash
        self.hash=self.calculate()
    def calculate(self):
         block_string=json.dumps({"index":self.index,"nonce":self.nonce,"tstamp":self.tstamp,"transaction":self.transaction,"prevhash":self.prevhash}).encode()
         return hashlib.sha256(block_string).hexdigest()
    def mine_block(self,difficulty=0):
        while not self.hash.startswith('0'*difficulty): 
            self.nonce += 1
            self.hash = self.calculate()

        print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain=[self.generateGenesBlock(),]
    def generateGenesBlock(self):
        return Block(0,time.time(),'Genesis Block',0,'0')
    def addBlock(self,transaction,difficulty=0):
        lastBlock=self.chain[-1]
        newBlock=Block(lastBlock.index+1,time.time(),transaction,0,lastBlock.hash)
        newBlock.nonce=newBlock.mine_block(difficulty)
        
        newBlock.hash=newBlock.calculate()
        
        self.chain.append(newBlock)
             
    def is_valid(self):
        for prev, curr in zip(self.chain, self.chain[1:]):
            if curr.hash != curr.calculate():
                return False
            if curr.prevhash != prev.hash:
                return False
        return True
coin=Blockchain()
coin.addBlock(500,2)
a=coin.is_valid()
print(a)
blk=Block(0,time.time(),200,0,'0')
blk.mine_block(2)
