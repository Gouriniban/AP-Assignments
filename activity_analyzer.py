from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce


def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    user_time = defaultdict(float)

    for log in logs:
        user_time[log["user"]] += log["duration"]

    return dict(user_time)


def most_active_users(logs: List[Dict], k: int) -> List[str]:
    user_time = total_time_per_user(logs)

    sorted_users = sorted(user_time.items(), key=lambda x: x[1], reverse=True)

    return [user for user, _ in sorted_users[:k]]


def unique_actions(logs: List[Dict]) -> Set[str]:
    return {log["action"] for log in logs}


def total_activity_time(logs: List[Dict]) -> float:
    return reduce(lambda total, log: total + log["duration"], logs, 0.0)


if __name__ == "__main__":

    logs = [
        {"user": "CSB24001", "action": "YouTube", "duration": 1.2},
        {"user": "CSB24033", "action": "Instagram", "duration": 0.8},
        {"user": "CSB24055", "action": "LeetCode", "duration": 2.0},
        {"user": "CSB24001", "action": "YouTube", "duration": 1.5},
        {"user": "CSB24033", "action": "WhatsApp", "duration": 1.0},
        {"user": "CSB24033", "action": "Instagram", "duration": 0.7},
    ]

    print("Total time per user:")
    print(total_time_per_user(logs))

    print("\nTop 2 active users:")
    print(most_active_users(logs, 2))

    print("\nUnique actions:")
    print(unique_actions(logs))

    print("\nTotal activity time:")
    print(total_activity_time(logs))