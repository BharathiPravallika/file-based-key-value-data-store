# file-based-key-value-data-store
# CRD-operations-of-a-file-based-key-value-data-store
This is a file which can be exposed as a library that supports the basic CRD(create, read, write) operations. Data store is meant to local storage for one single process on single laptop

The data store will support the following :
1. It can be initialized using an optional file path. If one is not provided, it will reliably 
create itself in a reasonable location on the laptop.<br>
2. A new key-value pair can be added to the data store using the Create operation. The key 
is always a string - capped at 32chars. The value is always a JSON object - capped at 
16KB.<br>
3. If Create is invoked for an existing key, an appropriate error must be returned.<br>
4. A Read operation on a key can be performed by providing the key, and receiving the 
value in response, as a JSON object.<br>
5. A Delete operation can be performed by providing the key.<br>
6. Every key supports setting a Time-To-Live property when it is created. This property is
optional. If provided, it will be evaluated as an integer defining the number of seconds 
the key must be retained in the data store. Once the Time-To-Live for a key has expired, 
the key will no longer be available for Read or Delete operations.<br>
7. Appropriate error responses must always be returned to a client if it uses the data store in 
unexpected ways or breaches any limits<br>
8. The file size never exceeds 1GB<br>
9. More than one client process cannot be allowed to use the same file as a data store at any given time.<br>

10.A client process is allowed to access the data store using multiple threads, if it desires to.
The data store must therefore be thread-safe<br>

11.The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store.<br>


Kindly Go through the access.py file and sample_test_cases.pdf file that are attached here with in order to understand clearly how 
the code works and how to perform operations in this. 
