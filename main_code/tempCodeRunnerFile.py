    pickle_in = open(f"level{level}_data" , "rb")
    world_data = pickle.load(pickle_in)
    world = World(world_data)