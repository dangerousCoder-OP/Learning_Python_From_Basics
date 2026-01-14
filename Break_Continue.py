# continue skips the desired if else block but stays in the loop
for i in range(5):
    if i == 3:
        continue
    print(i)

# break comes out of the loop When you have nested loops, a break statement affects only the
# innermost loop where it appears.
for i in range(10):
    print(i)
    if i == 5:
        break