# PACMAN

Pacman modes: 
1. Strive for big biscuits
2. Chase and eat as many ghosts as possible
3. Avoid ghosts

Conditions for different modes:

> Default - Pacman will strive for big biscuits. 
> If the Pacman detects ghosts being within a certain distance, the Pacman will avoid ghosts.

> If the Pacman eats big biscuits, it will chase the closest ghost. 

> If the Pacman have eaen all the biscuits, it will go to remaining biscuits. 

# GHOSTS 

Ghost modes: 
1. Chase Pacman
2. Protect big biscuit
3. Avoid Pacman

Conditions for different modes:

> Default - It will strive for Pacman finding the shortest path to him.
> If the ghost is a certain distance from biscuit, it will just go and protect the biscuit. 
>> If Pacman is a certain distance away from biscuit, it will resume striving for Pacman. 

> If Pacman eats biscuits, it will avoid pacman. 
