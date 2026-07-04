import api from "./api";

export interface DashboardResponse {
  total_notifications: number;
  open_notifications: number;
  closed_notifications: number;
  organizations: number;
  latest_notifications: {
    id: number;
    exam_name: string;
    notification_no: string;
    organization: string;
    application_end: string;
  }[];
  category_distribution: Record<string, number>;
  organization_distribution: Record<string, number>;
}

export const dashboardService = {
  async getDashboard(): Promise<DashboardResponse> {
    const response = await api.get<DashboardResponse>(
      "/api/v1/dashboard"
    );

    return response.data;
  },
};