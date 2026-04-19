from bisect import bisect_left, bisect_right


class Solution:
    def maxWalls(self, robots, distance, walls):
        n = len(robots)

        robot_data = sorted(zip(robots, distance))
        robots = [r for r, d in robot_data]
        distance = [d for r, d in robot_data]

        walls.sort()

        left_ranges = [(0, 0)] * n
        right_ranges = [(0, 0)] * n
        left_count = [0] * n
        right_count = [0] * n

        INF = 10 ** 30

        for i in range(n):
            pos = robots[i]
            dist = distance[i]

            prev_robot = robots[i - 1] if i > 0 else -INF
            next_robot = robots[i + 1] if i + 1 < n else INF

            # Fire left.
            # Include current robot position, but exclude previous robot position.
            left_start = max(pos - dist, prev_robot + 1)
            left_end = pos

            l = bisect_left(walls, left_start)
            r = bisect_right(walls, left_end)
            left_ranges[i] = (l, r)
            left_count[i] = r - l

            # Fire right.
            # Include current robot position, but exclude next robot position.
            right_start = pos
            right_end = min(pos + dist, next_robot - 1)

            l = bisect_left(walls, right_start)
            r = bisect_right(walls, right_end)
            right_ranges[i] = (l, r)
            right_count[i] = r - l

        dp_left = left_count[0]
        dp_right = right_count[0]

        for i in range(1, n):
            prev_right_l, prev_right_r = right_ranges[i - 1]
            curr_left_l, curr_left_r = left_ranges[i]

            overlap = max(
                0,
                min(prev_right_r, curr_left_r) - max(prev_right_l, curr_left_l)
            )

            new_dp_left = max(
                dp_left + left_count[i],
                dp_right + left_count[i] - overlap
            )

            new_dp_right = max(dp_left, dp_right) + right_count[i]

            dp_left = new_dp_left
            dp_right = new_dp_right

        return max(dp_left, dp_right)
