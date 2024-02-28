        ####### Avoiding Index Errors When Working with Lists #########
# ---------------------------------------------------------------------------- #
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) results in an index error
# When index error happens, try adjusting index by one.
# KEEP IN MIND:
# ALWAYS USE -1 TO ACCESS TO THE LAST ITEM
motorcycles = []
# print(motorcycles(-1)) will also results in an index error
# No items are in motorcycles

# IF an index error occurs and you can't fix it
# try print the list or the length of list.