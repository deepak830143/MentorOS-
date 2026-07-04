import api from "./api";
import type { Notification } from "../types/notification";

class NotificationService {
  async getNotifications(): Promise<Notification[]> {
    const response = await api.get<Notification[]>("/api/v1/notifications");
    return response.data;
  }
}

export const notificationService = new NotificationService();