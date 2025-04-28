import redis
# import time

redis_cache = redis.Redis(host="localhost", port=6379)

# r.set("France","Paris")
# r.set("Germany","Berlin")



# r.mset({"France":"Paris"})
# r.psetex("Germany",1000,"Berlin")

# # france_cap = r.get("France")
# # germany_cap = r.get("Germany")

# # print(france_cap)
# # print(germany_cap)

# # if (r.exists("France")):
# #     print(r.get("France"))
# # else:
# #     print("Not found")

# print(r.get("Germany"))
# time.sleep(2)
# print(r.get("Germany"))
