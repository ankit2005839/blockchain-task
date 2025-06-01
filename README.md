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
VALIDATION LOGIC:
For security , we check the hash of the block and the previous hash of the block should match the hash of the previous block .
It ensures the every block and overall chain is correct and there is no occurance of tampering.
If someone tampered with any component (timestamp, nonce, transaction , etc.), the recomputed value won’t match.
PROOF OF WORK :
It is a consensus mechanism ,in which miners compete to  solve the complex mathmatics puzzle will be the first one to validate it  
In PoW-based , the nonce is a number that miners adjust to find a hash of the block that meets the difficulty target.
SHA-256 is a cryptographic hash function:
It’s deterministic: same input → same output
It’s unpredictable: even a 1-bit change → totally different output
that's why it's difficult for miners to validate.
