from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum
import uuid


class ApplicationStatus(str, Enum):
    PENDING = "pending"
    APPLIED = "applied"
    REVIEWING = "reviewing"
    INTERVIEWED = "interviewed"
    REJECTED = "rejected"
    OFFERED = "offered"
    ACCEPTED = "accepted"


class JobStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    PAUSED = "paused"


class EmailDirection(str, Enum):
    SENT = "sent"
    RECEIVED = "received"


class OutreachTone(str, Enum):
    WARM = "warm"
    STRATEGIC = "strategic"
    BOLD = "bold"
    CURIOUS = "curious"
    FORMAL = "formal"
    FRIENDLY = "friendly"
    CHALLENGER = "challenger"


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# Database Models
class Candidate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    target_roles: List[str] = []
    target_companies: List[str] = []
    target_locations: List[str] = []
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    visa_sponsorship_required: bool = False
    work_authorization: Optional[str] = None
    years_experience: Optional[int] = None
    skills: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True


class Resume(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    version_name: str
    file_path: str
    file_url: Optional[str] = None
    extracted_text: Optional[str] = None
    skills: List[str] = []
    experience_years: Optional[int] = None
    is_primary: bool = False
    ats_score: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TailoringStrategy(str, Enum):
    JOB_SPECIFIC = "job_specific"
    COMPANY_SPECIFIC = "company_specific"
    ROLE_SPECIFIC = "role_specific"
    INDUSTRY_SPECIFIC = "industry_specific"
    SKILL_FOCUSED = "skill_focused"
    EXPERIENCE_FOCUSED = "experience_focused"


class ResumeFormat(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    HTML = "html"


class ATSOptimization(str, Enum):
    BASIC = "basic"
    ADVANCED = "advanced"
    AGGRESSIVE = "aggressive"
    STEALTH = "stealth"


class ResumeVersion(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    resume_id: str
    version_name: str
    tailored_for_job_id: Optional[str] = None
    tailoring_strategy: TailoringStrategy = TailoringStrategy.JOB_SPECIFIC
    ats_optimization_level: ATSOptimization = ATSOptimization.BASIC
    tailored_content: str
    original_content: str
    keywords_injected: List[str] = []
    keywords_optimized: List[str] = []
    sections_modified: List[str] = []
    ats_score: Optional[float] = None
    ats_breakdown: Optional[Dict[str, float]] = None
    readability_score: Optional[float] = None
    keyword_density: Optional[float] = None
    used_count: int = 0
    success_rate: Optional[float] = None
    response_rate: Optional[float] = None
    interview_rate: Optional[float] = None
    generation_params: Dict[str, Any] = {}
    stealth_fingerprint: Optional[str] = None
    format: ResumeFormat = ResumeFormat.PDF
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True


class ResumeGeneticPool(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    job_id: str
    generation: int = 1
    population_size: int = 10
    fitness_scores: List[float] = []
    version_ids: List[str] = []
    best_version_id: Optional[str] = None
    mutation_rate: float = 0.1
    crossover_rate: float = 0.7
    selection_method: str = "tournament"
    optimization_target: str = "ats_score"  # ats_score, response_rate, interview_rate
    created_at: datetime = Field(default_factory=datetime.utcnow)
    converged: bool = False


class ATSAnalysis(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    resume_version_id: str
    job_id: Optional[str] = None
    overall_score: float
    keyword_score: float
    format_score: float
    length_score: float
    section_score: float
    experience_score: float
    education_score: float
    skills_score: float
    contact_score: float
    recommendations: List[str] = []
    missing_keywords: List[str] = []
    keyword_frequency: Dict[str, int] = {}
    section_analysis: Dict[str, Any] = {}
    improvement_suggestions: List[str] = []
    analyzed_at: datetime = Field(default_factory=datetime.utcnow)


class ResumePerformanceMetrics(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    resume_version_id: str
    job_id: Optional[str] = None
    applications_sent: int = 0
    responses_received: int = 0
    interviews_scheduled: int = 0
    offers_received: int = 0
    rejections_received: int = 0
    response_rate: float = 0.0
    interview_rate: float = 0.0
    offer_rate: float = 0.0
    avg_response_time_hours: Optional[float] = None
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    tracking_period_days: int = 30


class KeywordOptimization(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    resume_version_id: str
    job_id: str
    target_keywords: List[str] = []
    injected_keywords: List[str] = []
    keyword_positions: Dict[str, List[int]] = {}  # keyword -> list of positions
    density_scores: Dict[str, float] = {}  # keyword -> density score
    context_analysis: Dict[str, str] = {}  # keyword -> context it was placed in
    optimization_strategy: str = "natural"  # natural, aggressive, stealth
    effectiveness_score: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StealthSettings(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    base_email: EmailStr
    alias_suffix: str
    full_email: EmailStr
    target_company: Optional[str] = None
    target_job_board: Optional[str] = None
    user_agent: Optional[str] = None
    proxy_config: Optional[Dict[str, Any]] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True


class JobRaw(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    job_board: str
    job_board_id: str
    title: str
    company: str
    location: str
    job_type: Optional[str] = None
    experience_level: Optional[str] = None
    salary_range: Optional[str] = None
    description: str
    requirements: List[str] = []
    benefits: List[str] = []
    visa_sponsorship: bool = False
    remote_work: bool = False
    job_url: str
    company_url: Optional[str] = None
    logo_url: Optional[str] = None
    scraped_at: datetime = Field(default_factory=datetime.utcnow)
    status: JobStatus = JobStatus.ACTIVE
    raw_data: Dict[str, Any] = {}


class JobFiltered(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    job_raw_id: str
    candidate_id: str
    match_score: float
    explanation: str
    keywords_matched: List[str] = []
    salary_match: bool = False
    location_match: bool = False
    visa_match: bool = False
    skills_match_score: Optional[float] = None
    experience_match: bool = False
    filtered_at: datetime = Field(default_factory=datetime.utcnow)
    priority: Priority = Priority.MEDIUM
    should_apply: bool = False


class CoverLetter(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    job_id: str
    tone: OutreachTone
    content: str
    pdf_url: Optional[str] = None
    ats_keywords: List[str] = []
    reasoning: Optional[str] = None
    company_research: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    used_count: int = 0
    success_rate: Optional[float] = None
    word_count: int = 0
    personalization_score: Optional[float] = None
    sentiment_analysis: Optional[Dict[str, Any]] = None


class CoverLetterTemplate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    tone: OutreachTone
    industry: Optional[str] = None
    template_content: str
    variables: List[str] = []  # List of variables like {company_name}, {position}
    success_rate: Optional[float] = None
    usage_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CompanyResearch(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    company_name: str
    domain: Optional[str] = None
    about: Optional[str] = None
    mission: Optional[str] = None
    values: List[str] = []
    recent_news: List[str] = []
    culture_keywords: List[str] = []
    tech_stack: List[str] = []
    company_size: Optional[str] = None
    industry: Optional[str] = None
    locations: List[str] = []
    leadership: List[Dict[str, str]] = []
    awards: List[str] = []
    sentiment_score: float = 0.0
    key_initiatives: List[str] = []
    research_timestamp: datetime = Field(default_factory=datetime.utcnow)
    research_sources: List[str] = []
    research_quality_score: Optional[float] = None


class CoverLetterPerformance(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    cover_letter_id: str
    candidate_id: str
    applications_sent: int = 0
    responses_received: int = 0
    interviews_scheduled: int = 0
    offers_received: int = 0
    response_rate: float = 0.0
    interview_rate: float = 0.0
    offer_rate: float = 0.0
    avg_response_time_hours: Optional[float] = None
    performance_score: float = 0.0
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    a_b_test_group: Optional[str] = None


class Application(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    job_id: str
    job_raw_id: str
    resume_version_id: str
    cover_letter_id: Optional[str] = None
    stealth_settings_id: str
    job_board: str
    company: str
    position: str
    application_url: Optional[str] = None
    status: ApplicationStatus = ApplicationStatus.PENDING
    applied_at: Optional[datetime] = None
    response_at: Optional[datetime] = None
    interview_scheduled: Optional[datetime] = None
    rejection_reason: Optional[str] = None
    notes: Optional[str] = None
    tracking_pixel_id: Optional[str] = None
    utm_params: Optional[Dict[str, str]] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OutreachLog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    job_id: Optional[str] = None
    application_id: Optional[str] = None
    channel: str  # 'linkedin', 'email', 'twitter'
    target_person: str
    target_role: Optional[str] = None
    message_content: str
    tone: OutreachTone
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    response_at: Optional[datetime] = None
    response_content: Optional[str] = None
    follow_up_scheduled: Optional[datetime] = None
    follow_up_count: int = 0
    success: bool = False
    ghosted: bool = False
    stealth_settings_id: str


class EmailLog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    direction: EmailDirection
    subject: str
    message_id: str
    alias_used: EmailStr
    job_id: Optional[str] = None
    application_id: Optional[str] = None
    thread_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    snippet: Optional[str] = None
    sender: Optional[str] = None
    recipient: Optional[str] = None
    raw_payload: Dict[str, Any] = {}
    processed: bool = False
    sentiment: Optional[str] = None
    intent: Optional[str] = None


class LearningData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    data_type: str  # 'resume_performance', 'outreach_response', 'interview_feedback'
    context: Dict[str, Any]
    outcome: str
    success_score: Optional[float] = None
    insights: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    applied_to_model: bool = False


class JobScheduler(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    job_name: str
    job_type: str  # 'scraping', 'application', 'outreach', 'analysis'
    schedule_cron: str
    next_run: datetime
    last_run: Optional[datetime] = None
    is_active: bool = True
    parameters: Dict[str, Any] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class GmailOAuth(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    gmail_address: EmailStr
    access_token: str
    refresh_token: str
    token_expiry: datetime
    scopes: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True


# Request/Response Models
class CandidateCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    target_roles: List[str] = []
    target_companies: List[str] = []
    target_locations: List[str] = []
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    visa_sponsorship_required: bool = False
    work_authorization: Optional[str] = None
    years_experience: Optional[int] = None
    skills: List[str] = []


class CandidateUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    target_roles: Optional[List[str]] = None
    target_companies: Optional[List[str]] = None
    target_locations: Optional[List[str]] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    visa_sponsorship_required: Optional[bool] = None
    work_authorization: Optional[str] = None
    years_experience: Optional[int] = None
    skills: Optional[List[str]] = None
    is_active: Optional[bool] = None


class JobSearchRequest(BaseModel):
    candidate_id: str
    job_boards: List[str] = ["indeed", "linkedin", "glassdoor"]
    keywords: List[str] = []
    location: Optional[str] = None
    max_results: int = 50
    date_range: Optional[str] = "7d"  # 1d, 3d, 7d, 14d, 30d


# Phase 7: Recruiter Outreach Engine Models
class OutreachChannel(str, Enum):
    LINKEDIN = "linkedin"
    EMAIL = "email"
    TWITTER = "twitter"
    PHONE = "phone"


class OutreachStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    OPENED = "opened"
    CLICKED = "clicked"
    REPLIED = "replied"
    BOUNCED = "bounced"
    FAILED = "failed"


class CampaignStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class RecruiterType(str, Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"
    AGENCY = "agency"
    HEADHUNTER = "headhunter"


class Recruiter(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: Optional[EmailStr] = None
    linkedin_url: Optional[str] = None
    linkedin_id: Optional[str] = None
    twitter_handle: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    company_domain: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    industry: Optional[str] = None
    recruiter_type: RecruiterType = RecruiterType.INTERNAL
    specializations: List[str] = []  # Tech, Marketing, Sales, etc.
    seniority_levels: List[str] = []  # Junior, Mid, Senior, Executive
    response_rate: Optional[float] = None  # Historical response rate
    avg_response_time: Optional[int] = None  # In hours
    last_contacted: Optional[datetime] = None
    total_contacts: int = 0
    successful_contacts: int = 0
    profile_data: Dict[str, Any] = {}  # Additional scraped data
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True


class OutreachCampaign(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    name: str
    description: Optional[str] = None
    target_roles: List[str] = []
    target_companies: List[str] = []
    target_locations: List[str] = []
    channels: List[OutreachChannel] = []
    status: CampaignStatus = CampaignStatus.DRAFT
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    daily_limit: int = 10  # Max outreach attempts per day
    delay_between_messages: int = 300  # Seconds between messages
    follow_up_delay: int = 86400  # Seconds between follow-ups (24 hours)
    max_follow_ups: int = 3
    personalization_level: str = "medium"  # low, medium, high
    tone: OutreachTone = OutreachTone.WARM
    auto_follow_up: bool = True
    track_opens: bool = True
    track_clicks: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OutreachMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    campaign_id: str
    recruiter_id: str
    candidate_id: str
    channel: OutreachChannel
    subject: Optional[str] = None
    content: str
    personalization_data: Dict[str, Any] = {}  # Data used for personalization
    tone: OutreachTone
    is_follow_up: bool = False
    follow_up_sequence: int = 0  # 0 = initial, 1 = first follow-up, etc.
    parent_message_id: Optional[str] = None  # For follow-ups
    scheduled_for: Optional[datetime] = None
    sent_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    opened_at: Optional[datetime] = None
    clicked_at: Optional[datetime] = None
    replied_at: Optional[datetime] = None
    status: OutreachStatus = OutreachStatus.PENDING
    error_message: Optional[str] = None
    linkedin_message_id: Optional[str] = None
    email_message_id: Optional[str] = None
    metrics: Dict[str, Any] = {}  # Open rates, click rates, etc.
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OutreachTemplate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = None
    channel: OutreachChannel
    tone: OutreachTone
    subject_template: Optional[str] = None  # For email
    message_template: str
    personalization_fields: List[str] = []  # Fields like {name}, {company}, etc.
    follow_up_templates: List[str] = []  # Templates for follow-up messages
    success_rate: Optional[float] = None
    usage_count: int = 0
    created_by: str  # User who created the template
    is_public: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OutreachResponse(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    message_id: str
    recruiter_id: str
    candidate_id: str
    campaign_id: str
    channel: OutreachChannel
    response_type: str  # "reply", "connection_accepted", "profile_view", etc.
    content: Optional[str] = None
    sentiment: Optional[str] = None  # positive, negative, neutral
    intent: Optional[str] = None  # interested, not_interested, more_info, etc.
    response_time: Optional[int] = None  # Time to respond in seconds
    linkedin_response_id: Optional[str] = None
    email_response_id: Optional[str] = None
    auto_processed: bool = False
    requires_follow_up: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class RecruiterResearch(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    recruiter_id: str
    research_type: str  # "profile_scrape", "company_research", "contact_discovery"
    data_source: str  # "linkedin", "company_website", "glassdoor", etc.
    research_data: Dict[str, Any] = {}
    confidence_score: Optional[float] = None
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OutreachAnalytics(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    campaign_id: str
    candidate_id: str
    date: datetime
    messages_sent: int = 0
    messages_delivered: int = 0
    messages_opened: int = 0
    messages_clicked: int = 0
    messages_replied: int = 0
    messages_bounced: int = 0
    connections_made: int = 0
    response_rate: float = 0.0
    open_rate: float = 0.0
    click_rate: float = 0.0
    bounce_rate: float = 0.0
    avg_response_time: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LinkedInOAuth(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    access_token: str
    refresh_token: Optional[str] = None
    token_expiry: datetime
    scopes: List[str] = []
    linkedin_user_id: str
    linkedin_profile_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True


# Request/Response Models for Outreach
class CampaignCreate(BaseModel):
    name: str
    description: Optional[str] = None
    target_roles: List[str] = []
    target_companies: List[str] = []
    target_locations: List[str] = []
    channels: List[OutreachChannel] = []
    daily_limit: int = 10
    delay_between_messages: int = 300
    follow_up_delay: int = 86400
    max_follow_ups: int = 3
    personalization_level: str = "medium"
    tone: OutreachTone = OutreachTone.WARM
    auto_follow_up: bool = True


class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    target_roles: Optional[List[str]] = None
    target_companies: Optional[List[str]] = None
    target_locations: Optional[List[str]] = None
    channels: Optional[List[OutreachChannel]] = None
    status: Optional[CampaignStatus] = None
    daily_limit: Optional[int] = None
    delay_between_messages: Optional[int] = None
    follow_up_delay: Optional[int] = None
    max_follow_ups: Optional[int] = None
    personalization_level: Optional[str] = None
    tone: Optional[OutreachTone] = None
    auto_follow_up: Optional[bool] = None


class RecruiterCreate(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    linkedin_url: Optional[str] = None
    linkedin_id: Optional[str] = None
    twitter_handle: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    company_domain: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    industry: Optional[str] = None
    recruiter_type: RecruiterType = RecruiterType.INTERNAL
    specializations: List[str] = []
    seniority_levels: List[str] = []


class MessageCreate(BaseModel):
    campaign_id: str
    recruiter_id: str
    channel: OutreachChannel
    subject: Optional[str] = None
    content: str
    personalization_data: Dict[str, Any] = {}
    tone: OutreachTone
    scheduled_for: Optional[datetime] = None


class TemplateCreate(BaseModel):
    name: str
    description: Optional[str] = None
    channel: OutreachChannel
    tone: OutreachTone
    subject_template: Optional[str] = None
    message_template: str
    personalization_fields: List[str] = []
    follow_up_templates: List[str] = []
    is_public: bool = False