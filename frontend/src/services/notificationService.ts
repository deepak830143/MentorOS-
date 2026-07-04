import api from "./api";
import type { Notification } from "../types/notification";

export const notificationService = {
  async getNotifications(): Promise<Notification[]> {
    const response = await api.get("/api/v1/notifications");
    return response.data;
  },
};