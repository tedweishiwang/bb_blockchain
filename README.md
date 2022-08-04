# Run instruction

Simply run:
`python3 blockchain.py`

Pasting run result here for reference:

```
Initializing block chain...
The Genesis block hash is: 0dfcf9013cc73967876508d0875ca1cdde2dc89651c8dbd2a870ab49a5d9c0e3

Create transactions:
t1 hash is  b'3f54ebe72b4c38a7b84e180b94985b135ad27fd16a037c6c52ba3c015e6f397e'
t2 hash is  b'fde7504652c942333f87dc5b936fb2df03dc2d44ab7091a7910999e0d39e67d3'
t3 hash is  b'e77300753f520f964a9514f26881add38a0beed08acfa1c7397e3d8c146d7297'
t4 hash is  b'26d4bc500be0ab313b25975144163b15e25547aa8ddb23760f9058b8390305c7'
t5 hash is  b'177be6598ed512f09b53c679d9c28253baec74d06eb97829aba1113f485ffe57'
t6 hash is  b'bcf54167abcea828d7fc8e2f12d906a47079f91f8b7a30af95a7b739ea248913'
t7 hash is  b'a09217dde41e5988e21c7941a295263407c3aede3d5c8d730eb5732e5fd55ae3'
t8 hash is  b'96bc365607dba9d437ea8cce29a9450539099b019d3837d5d7dbd12e8e929e73'
t9 hash is  b'fe4d5757c1f0389b554d024a899425e1fbc1625abaab71804617aa3d4e731968'
t10 hash is  b'0f2ae82594aa9ba11053dde25a5d7b4eb76eff5df3e592c3da461c003dcc429d'

Create a block with the first 5 transactions and append to the Genesis block:
new block with block hash 8f3f61a98342a8830bb4dc0f764c2f0e5a24cad207dff389451bee429c1ae594 has been appended.
Create a block with the first 5 transactions and append to the previous block:
new block with block hash 3ae16527e1f29a6b7121aa6acfbc811bd163b2fae66808d83db1b23047f43a8f has been appended.

Testing finding block by height and block hash: 
{'block_hash': '3ae16527e1f29a6b7121aa6acfbc811bd163b2fae66808d83db1b23047f43a8f',
 'block_header': <header.Header object at 0x104d50af0>,
 'block_size': 0,
 'magic_number': 3652501241,
 'transaction_counter': 5,
 'transactions': {b'0f2ae82594aa9ba11053dde25a5d7b4eb76eff5df3e592c3da461c003dcc429d': <transaction.Transaction object at 0x104d3ff70>,
                  b'96bc365607dba9d437ea8cce29a9450539099b019d3837d5d7dbd12e8e929e73': <transaction.Transaction object at 0x104d3fa00>,
                  b'a09217dde41e5988e21c7941a295263407c3aede3d5c8d730eb5732e5fd55ae3': <transaction.Transaction object at 0x104d3fd60>,
                  b'bcf54167abcea828d7fc8e2f12d906a47079f91f8b7a30af95a7b739ea248913': <transaction.Transaction object at 0x104d3f880>,
                  b'fe4d5757c1f0389b554d024a899425e1fbc1625abaab71804617aa3d4e731968': <transaction.Transaction object at 0x104d3ff40>}}

Testing finding transaction by transaction hash: 
{'in_counter': 1,
 'list_of_inputs': ['t3 input transaction for genesis block'],
 'list_of_outputs': ['t3 output transaction for genesis block'],
 'out_counter': 1,
 'transaction_hash': b'e77300753f520f964a9514f26881add38a0beed08acfa1c7397e3d8c'
                     b'146d7297',
 'version_number': 1}

Process finished with exit code 0
```