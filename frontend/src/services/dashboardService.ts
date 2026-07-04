import api from "./api";

export interface DashboardResponse {
  total_notifications: number;
  open_notifications: number;
  closed_notifications: number;
  organizations: number;

  latest_notifications: {
    id: number;
    exam_name: string;
    organization: string;
    notification_no: string;
    application_end: string;
  }[];
}

export async function getDashboard() {
  const { data } = await api.get<DashboardResponse>(
    "/api/v1/dashboard"
  );

  return data;
}