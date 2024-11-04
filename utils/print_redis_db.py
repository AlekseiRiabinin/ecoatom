from redis_dict import RedisDict


db = RedisDict(host="redis", port=6379)

# loop through the dictionary and print each key-value pair
for key, val in db.items():
    if str(key).startswith("storage"):
        print(f"{key} ->   "
              f"plastic: {val['plastic']:<5} "
              f"glass: {val['glass']:<5} "
              f"biowaste: {val['biowaste']:<5}")
