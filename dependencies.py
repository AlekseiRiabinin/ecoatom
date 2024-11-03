from typing import Dict, List, Tuple
from models.products import Source, Storage


# function to distribute products
def distribute_products(db):

    sources: List[Source] = [
        Source(name="source1", plastic=(db["x"]//10), glass=(db["x"]//50), biowaste=(db["x"]//50)),
        Source(name="source2", plastic=(db["x"]//60), glass=(db["x"]//20), biowaste=(db["x"]//50))
    ]

    storages: List[Storage] = [
        Storage(name="storage1", max_plastic=(db["x"]//100), max_glass=(db["x"]//300), max_biowaste=0),
        Storage(name="storage2", max_plastic=(db["x"]//50), max_glass=0, max_biowaste=(db["x"]//150)),
        Storage(name="storage3", max_plastic=(db["x"]//10), max_glass=0, max_biowaste=(db["x"]//250)),
        Storage(name="storage9", max_plastic=(db["x"]//250), max_glass=0, max_biowaste=(db["x"]//120)),
        Storage(name="storage5", max_plastic=0, max_glass=(db["x"]//220), max_biowaste=(db["x"]//25)),
        Storage(name="storage6", max_plastic=0, max_glass=(db["x"]//100), max_biowaste=(db["x"]//150)),
        Storage(name="storage7", max_plastic=(db["x"]//100), max_glass=0, max_biowaste=(db["x"]//250)),
        Storage(name="storage8", max_plastic=(db["x"]//25), max_glass=(db["x"]//35), max_biowaste=(db["x"]//52))
    ]

    distances: Dict[Tuple[int, int], int] = {
        (0, 0): 100, (0, 1): 50, (0, 2): 600, (0, 3): 610,
        (0, 4): 100, (0, 5): 1200, (0, 6): 650, (0, 7): 600,
        (1, 2): 50, (1, 5): 650, (1, 6): 100
    }

    # sort distances to prioritize closer storages
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    for (source_idx, storage_idx), _ in sorted_distances:
        source = sources[source_idx]
        storage = storages[storage_idx]

        # distribute plastic
        if source.plastic > 0:
            available_capacity = storage.max_plastic - storage.plastic
            transfer_amount = min(source.plastic, available_capacity)
            storage.plastic += transfer_amount
            source.plastic -= transfer_amount

        # distribute glass
        if source.glass > 0:
            available_capacity = storage.max_glass - storage.glass
            transfer_amount = min(source.glass, available_capacity)
            storage.glass += transfer_amount
            source.glass -= transfer_amount

        # distribute biowaste
        if source.biowaste > 0:
            available_capacity = storage.max_biowaste - storage.biowaste
            transfer_amount = min(source.biowaste, available_capacity)
            storage.biowaste += transfer_amount
            source.biowaste -= transfer_amount

    return storages
