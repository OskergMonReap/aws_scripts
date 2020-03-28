# Working With DynamoDB
Fully managed NoSQL Database in AWS, multi-region, multi-master with built-in security/backup/restore as well as in-memory caching

## Data Structures
- *No fixed schema*
- Attributes = { key: value }
  - Attributes can contain nested attributes
    - { key: { key: value, key: value }}

#### Partition (HASH) Key 
> **required item for every item in your table(s)**
>
> consists of a single attribute, key value is used as input for hash function to determine storage

#### Sort (RANGE) Key
> Together with the Partition key, known as `Composite Primary Key`
>
> Applies first attribute to a hash function, storing items with the same partition key together
>
> The sort key, as the name implies, is then used to determine the order
>
> **Items can share partition keys, but NOT sort keys**

## Secondary Indexes
#### **Global Secondary Index**
> Possesses partition and sort keys, which CAN differ from table keys
>
> Can be created at any time

#### **Local Secondary Index**
> Possesses partition key identical to table, but with a different sort key from table
>
> Must be created at Table Creation time, cannot be added after the fact
