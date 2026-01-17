"""CV data schema validation."""

from datetime import date
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, EmailStr


class PersonalInfo(BaseModel):
    """Personal information section."""

    name: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    birth_date: Optional[date] = None


class Experience(BaseModel):
    """Work experience entry."""

    id: str
    company: str
    title: str
    period: str
    location: Optional[str] = None
    technologies: Optional[List[str]] = []
    description: str


class Education(BaseModel):
    """Education entry."""

    id: str
    degree: str
    school: Optional[str] = None
    graduation_year: Optional[int] = None
    description: Optional[str] = None


class Skill(BaseModel):
    """Skill entry."""

    category: str
    items: List[str]


class Certification(BaseModel):
    """Certification entry."""

    id: str
    title: str
    issuer: str
    issued_date: Optional[date] = None
    expires_date: Optional[date] = None


class Project(BaseModel):
    """Project entry."""

    id: str
    title: str
    technologies: Optional[List[str]] = []
    description: str
    url: Optional[str] = None


class CVData(BaseModel):
    """Complete CV data structure."""

    personal: PersonalInfo
    summary: str
    experience: List[Experience]
    education: List[Education]
    skills: List[Skill]
    certifications: Optional[List[Certification]] = []
    languages: Optional[List[Dict[str, str]]] = []
    projects: Optional[List[Project]] = []


def validate_cv(data: Dict[str, Any]) -> CVData:
    """Validate CV data against schema.

    Args:
        data: CV data dictionary

    Returns:
        Validated CVData object

    Raises:
        ValidationError: If data doesn't match schema
    """
    return CVData(**data)
