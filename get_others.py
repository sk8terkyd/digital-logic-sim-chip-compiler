import Chip


def get_others(chip):
    """
    Purpose: Returns every chip in a givin chip that isn't a builtin chip
    Arguments: chip (Chip)
    Example: If i pass in an "XOR" chip object,
    it will return ["NAND", "OR"] because, XOR is made of
    ["AND", "NAND", "OR"] so "NAND" and "OR" are the only non builtin
    chips.
    """
    others = []

    for i in chip.component_list:
        if i not in ["AND", "NOT", "SIGNAL IN", "SIGNAL OUT"]:
            chip.chipComponents.remove(i)
            others.append(i)

    return others
