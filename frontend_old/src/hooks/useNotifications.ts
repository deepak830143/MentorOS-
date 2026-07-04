import { useQuery } from "@tanstack/react-query";
import { notificationService } from "../services/notificationService";

export function useNotifications() {
  return useQuery({
    queryKey: ["notifications"],
    queryFn: async () => {
      return await notificationService.getNotifications();
    },
  });
}