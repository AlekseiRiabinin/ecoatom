import redis


# connect to Redis
db = redis.Redis(host="redis", port=6379)

# flush all data
db.flushall()

print("All data purged from Redis.")
