import os 

for i in range(0,100):
    os.rename(f"C:/Users/hp/OneDrive/Desktop/Project/data/user.789457.{i+1}.jpg", f"C:/Users/hp/OneDrive/Desktop/Project/data/user.789456.{i+1}.jpg")
    
print("completed")