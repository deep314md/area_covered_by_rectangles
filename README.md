# area_covered_by_rectangles

Your task in order to complete this Kata is to write a function which calculates the area covered by a union of rectangles.
Rectangles can have non-empty intersection, in this way simple solution: Sall = S1 + S2 + ... + Sn-1 + Sn (where n - the quantity of rectangles) will not work.

Preconditions
each rectangle is represented as: [x0, y0, x1, y1]
(x0, y0) - coordinates of the bottom left corner
(x1, y1) - coordinates of the top right corner
xi, yi - positive integers or zeroes (0, 1, 2, 3, 4..)
sides of rectangles are parallel to coordinate axes
your input data is array of rectangles
Requirements
Number of rectangles in one test (not including simple tests) range from 3000 to 15000. There are 10 tests with such range. So, your algorithm should be optimal.
Sizes of the rectangles can reach values like 1e6.

