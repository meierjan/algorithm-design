
def min_loc_greedy(h):
    telephone_poles = []
    last_pole = -5000
    for house_pos in h:
        if(last_pole + 4000 < house_pos):
            new_pole_position = house_pos+4000
            telephone_poles.append(new_pole_position)
            last_pole = new_pole_position
    return telephone_poles
