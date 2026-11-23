"""
LeetCode 1125: Smallest Sufficient Team
Difficulty: Hard
Pattern: Bitmask DP (Skill-Mask Set Cover Transition)

Time Complexity: O(people * 2^skills)
Space Complexity: O(2^skills)
"""

from typing import Dict, List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_idx = {skill: i for i, skill in enumerate(req_skills)}
        n_skills = len(req_skills)
        full_mask = (1 << n_skills) - 1

        person_masks: List[int] = []
        for skills in people:
            m = 0
            for s in skills:
                if s in skill_idx:
                    m |= 1 << skill_idx[s]
            person_masks.append(m)

        # Map covered skill_mask -> integer bitmask of selected people indices
        dp: Dict[int, int] = {0: 0}

        for i, p_mask in enumerate(person_masks):
            if p_mask == 0:
                continue
            for mask, team in list(dp.items()):
                combined = mask | p_mask
                if combined == mask:
                    continue
                candidate_team = team | (1 << i)
                if combined not in dp or candidate_team.bit_count() < dp[combined].bit_count():
                    dp[combined] = candidate_team

        best_team_mask = dp[full_mask]
        return [i for i in range(len(people)) if best_team_mask & (1 << i)]


if __name__ == "__main__":
    sol = Solution()
    res = sol.smallestSufficientTeam(
        ["java", "nodejs", "reactjs"],
        [["java"], ["nodejs"], ["nodejs", "reactjs"]],
    )
    assert res == [0, 2]
    print("LC 1125 verified successfully!")
