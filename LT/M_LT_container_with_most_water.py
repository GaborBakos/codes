'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

INPUT: height -> List[int]
OUTPUT: max area

'''


def maxArea(height):
    ''' 
        This is a O(n) in time complexity and O(1) in space complexity.
        We pass through our list from the two sides.
        If a pillar is shorter than the other then we move inwards from this pillar's side. We can gain additional area by doing so (if the more inward pillar is taller).
    '''
    max_area = 0
    l_width = 0
    r_width = len(height) - 1
    while l_width < r_width:
        w = r_width - l_width
        h = min(height[l_width], height[r_width])
        max_area = max(max_area, w * h)

        if height[l_width] < height[r_width]:
            l_width += 1
        else:
            r_width -= 1
    return max_area


height = [1, 1, 8, 9, 6, 2, 3, 4, 5, 8, 8, 9, 9, 9, 1, 1, 1, 1, 1]
print('Input: {}\nMax Area: {}'.format(height, maxArea(height)))
