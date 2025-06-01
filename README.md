# blockchain-task
BLOCK STRUCTURE:
In the Blockchain, each block contain :-
1. Index: position in the Blockchain
2. Time stamp: Time at which block is created
3. Previous Hash: hash value of the previous block
4. Hash: Hash value of itself
5. nonce: number used to generate valid hash according to difficulty level( we can change the nonce to generate a valid hash )
6. Transation: it includes Sender's address, Receiver's address and Amount
7. difficulty level: difficulty to solve puzzles for mining the block
We change only nonce value because all others parameters are fixed in the block , for generating a valid hash.
For generating the Hash , we need all parameters of Block.
If anyone change anything in any block then the hash changes , and the Whole blockchain will disturb.It makes it more secure.

