flowchart TD
A[startupOne]:::red-->|Vendor lock in|A1[Vendor1]
A --> |Vendor lock in|A2[Vendor2]

B[startupTwo]:::red-->|Vendor lock in|A1[Vendor1]
B --> |Vendor lock in|B2[Vendor3]

subgraph NonProfit Open Source
C[theOpenModel]:::orange --Abstraction Layer-->C1[Service1]:::orange
C--Abstraction Layer-->C2[Service2]:::orange
end
C1 --> A1
C2-->A2
C2-->B2


D[neoStartup1]:::blue-->C
E[neoStartup2]:::blue-->C


F[Startups] --> |old model|A 
F --> |old model|B
F --> |new model| D
F --> |new model|E


classDef orange fill:#C74
classDef blue fill:#007
classDef red fill:#700
