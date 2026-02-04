"""Skills module for deep-agents.

Public API:
- SkillsMiddleware: Middleware for integrating skills into agent execution
- list_skills: List available skills from user and project directories
- SkillMetadata: Type definition for skill metadata
"""

from skills.load import SkillMetadata, list_skills
from skills.middleware import SkillsMiddleware, NoSkillsMiddleware

__all__ = [
    "SkillsMiddleware",
    "NoSkillsMiddleware",
    "SkillMetadata",
    "list_skills",
]