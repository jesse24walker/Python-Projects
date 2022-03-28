height=int(input("Enter the height:"))
bounces=int(input("Enter the number of bounces:"))
distance=0
bounciness=0.6
for bounces in range(bounces):
    distance+=height
    height*=bounciness
    distance+=height
    bounces-=1

print("The distance that the ball travelled is %.2f" % distance)
