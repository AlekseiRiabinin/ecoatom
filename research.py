from pydantic import BaseModel, Field
from typing import List, Dict, Tuple


class Source(BaseModel):
    name: str = Field()
    plastic: int = Field(default=0)
    glass: int = Field(default=0)
    biowaste: int = Field(default=0)


class Storage(BaseModel):
    name: str = Field()
    max_plastic: int = Field()
    max_glass: int = Field()
    max_biowaste: int = Field()
    plastic: int = Field(default=0)
    glass: int = Field(default=0)
    biowaste: int = Field(default=0)


r = {
    "source2": {"name": "source2", "plastic": 20, "glass": 50, "biowaste": 20},
    "source1": {"name": "source1", "plastic": 100, "glass": 20, "biowaste": 20},
    "x": 1000
}

# Create instances of Source
source1 = Source(name="source1", plastic=(r["x"]//10), glass=(r["x"]//50), biowaste=(r["x"]//50))
source2 = Source(name="source2", plastic=(r["x"]//60), glass=(r["x"]//20), biowaste=(r["x"]//50))

# Create instances of Storage with max capacities
storages = [
    Storage(name="storage1", max_plastic=(r["x"]//100), max_glass=(r["x"]//300), max_biowaste=0),
    Storage(name="storage2", max_plastic=(r["x"]//50), max_glass=0, max_biowaste=(r["x"]//150)),
    Storage(name="storage3", max_plastic=(r["x"]//10), max_glass=0, max_biowaste=(r["x"]//250)),
    Storage(name="storage9", max_plastic=(r["x"]//250), max_glass=0, max_biowaste=(r["x"]//120)),
    Storage(name="storage5", max_plastic=0, max_glass=(r["x"]//220), max_biowaste=(r["x"]//25)),
    Storage(name="storage6", max_plastic=0, max_glass=(r["x"]//100), max_biowaste=(r["x"]//150)),
    Storage(name="storage7", max_plastic=(r["x"]//100), max_glass=0, max_biowaste=(r["x"]//250)),
    Storage(name="storage8", max_plastic=(r["x"]//25), max_glass=(r["x"]//35), max_biowaste=(r["x"]//52))
]


# Define distances from sources to storages
distances: Dict[Tuple[int, int], float] = {
    (0, 0): 100, (0, 1): 50, (0, 2): 600, (0, 3): 610,
    (0, 4): 100, (0, 5): 1200, (0, 6): 650, (0, 7): 600,
    (1, 2): 50, (1, 5): 650, (1, 6): 100
}


# Function to distribute materials optimally
def distribute_materials(
        sources: List[Source],
        storages: List[Storage],
        distances: Dict[Tuple[int, int], float]):

    # Sort distances to prioritize closer storages
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    for (source_idx, storage_idx), _ in sorted_distances:
        source = sources[source_idx]
        storage = storages[storage_idx]

        # Distribute plastic
        if source.plastic > 0:
            available_capacity = storage.max_plastic - storage.plastic
            transfer_amount = min(source.plastic, available_capacity)
            storage.plastic += transfer_amount
            source.plastic -= transfer_amount

        # Distribute glass
        if source.glass > 0:
            available_capacity = storage.max_glass - storage.glass
            transfer_amount = min(source.glass, available_capacity)
            storage.glass += transfer_amount
            source.glass -= transfer_amount

        # Distribute biowaste
        if source.biowaste > 0:
            available_capacity = storage.max_biowaste - storage.biowaste
            transfer_amount = min(source.biowaste, available_capacity)
            storage.biowaste += transfer_amount
            source.biowaste -= transfer_amount


# Distribute materials
distribute_materials([source1, source2], storages, distances)


# # Print the results
# for idx, storage in enumerate(storages):
#     print(storage)

# Print the results
for storage in storages:
    print(storage)
