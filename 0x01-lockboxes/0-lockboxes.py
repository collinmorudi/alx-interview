#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    a function that solves lockboxes problem
    """
    # Start with box 0 unlocked
    unlocked_boxes = set([0])
    # Start with the keys from box 0
    keys = set(boxes[0])

    # Loop until we cannot find any more boxes to unlock
    while True:
        new_keys = set()
        for key in keys:
            # If the box corresponding to the key is unlocked, skip
            if key in unlocked_boxes or key >= len(boxes):
                continue
            # Unlock the box and collect the keys from that box
            unlocked_boxes.add(key)
            new_keys.update(boxes[key])

        # If no new keys were found, break out of the loop
        if not new_keys.difference(keys):
            break

        # Add the new keys to the existing keys
        keys.update(new_keys)

    # Return true if all boxes are unlocked, else false
    return len(unlocked_boxes) == len(boxes)
