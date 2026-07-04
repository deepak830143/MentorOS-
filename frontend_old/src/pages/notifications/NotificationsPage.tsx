import MainLayout from "../../components/layout/MainLayout";
import NotificationCard from "../../components/notifications/NotificationCard";
import { useNotifications } from "../../hooks/useNotifications";

export default function NotificationsPage() {
  const { data, isLoading, isError } = useNotifications();

  if (isLoading) {
    return (
      <MainLayout>
        <div className="flex h-screen items-center justify-center">
          <h1 className="text-2xl font-bold">
            Loading Notifications...
          </h1>
        </div>
      </MainLayout>
    );
  }

  if (isError) {
    return (
      <MainLayout>
        <div className="flex h-screen items-center justify-center">
          <h1 className="text-2xl font-bold text-red-600">
            Failed to load notifications.
          </h1>
        </div>
      </MainLayout>
    );
  }

  return (
    <MainLayout>
      <div className="space-y-8">

        <div>
          <h1 className="text-4xl font-bold">
            Notifications
          </h1>

          <p className="mt-2 text-slate-500">
            Browse the latest government notifications.
          </p>
        </div>

        <div className="grid gap-6">

          {data?.map((notification) => (
            <NotificationCard
              key={notification.id}
              notification={notification}
            />
          ))}

        </div>

      </div>
    </MainLayout>
  );
}