# The "with" statement handles resources safely (like try with resource in Java)
# "with" statement securely closes the resource in the end

with open('resource.txt', 'r') as inputFile:
    # Do something with the resources
    # The resource will be securely closed once the following code is executed
    for line in inputFile:
        print('> {}'.format(line))
