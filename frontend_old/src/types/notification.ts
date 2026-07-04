export interface Notification {
  id: number;
  source: string;
  organization: string;
  exam_name: string;
  notification_no: string;
  title: string;
  notification_hash: string;
  category: string;
  status: string;
  vacancies: number | null;
  qualification: string | null;
  age_limit: string | null;
  salary: string | null;
  application_start: string | null;
  application_end: string | null;
  exam_date: string | null;
  pdf_url: string | null;
  apply_url: string | null;
  official_url: string | null;
  description: string | null;
  ai_summary: string | null;
  created_at: string;
  updated_at: string;
}