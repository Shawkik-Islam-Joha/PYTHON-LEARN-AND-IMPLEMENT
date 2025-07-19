for i in range(100):
  if i==50:
    break        # Get out of the loop
  print(f"Loop run {i}")

for x in range(1,100,5):
  if x>50:
    continue     # Skip this iteration of x
  print(f"Another Loop run {x}")
