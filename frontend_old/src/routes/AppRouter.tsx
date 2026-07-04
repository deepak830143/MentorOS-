import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import LoginPage from "../pages/auth/LoginPage";
import RegisterPage from "../pages/auth/RegisterPage";
import DashboardPage from "../pages/dashboard/DashboardPage";
import NotificationsPage from "../pages/notifications/NotificationsPage";
import NotificationDetailsPage from "../pages/notifications/NotificationDetailsPage";
import BookmarksPage from "../pages/bookmarks/BookmarksPage";
import ProfilePage from "../pages/profile/ProfilePage";

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route path="/login" element={<LoginPage />} />

        <Route path="/register" element={<RegisterPage />} />

        <Route path="/dashboard" element={<DashboardPage />} />

        <Route
          path="/notifications"
          element={<NotificationsPage />}
        />

        <Route
          path="/notifications/:id"
          element={<NotificationDetailsPage />}
        />

        <Route
          path="/bookmarks"
          element={<BookmarksPage />}
        />

        <Route
          path="/profile"
          element={<ProfilePage />}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default AppRouter;