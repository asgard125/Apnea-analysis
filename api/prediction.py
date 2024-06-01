
def model():
    healthy_indices = set(list(range(1, 16)) + list(range(26, 31)))
    ill_indices = set(range(1, 41)) - healthy_indices
