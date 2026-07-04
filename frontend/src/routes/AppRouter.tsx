import { Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "../components/layout/MainLayout";

import DashboardPage from "../pages/dashboard/DashboardPage";
import NotificationsPage from "../pages/notifications/NotificationsPage";

// Temporary pages (replace these later with real pages)
function BookmarksPage() {
  return <h1 className="text-3xl font-bold">Bookmarks</h1>;
}

function ProfilePage() {
  return <h1 className="text-3xl font-bold">Profile</h1>;
}

function SettingsPage() {
  return <h1 className="text-3xl font-bold">Settings</h1>;
}

export default function AppRouter() {
  return (
    <Routes>
      {/* Redirect root */}
      <Route path="/" element={<Navigate to="/dashboard" replace />} />

      {/* Dashboard */}
      <Route
        path="/dashboard"
        element={
          <MainLayout>
            <DashboardPage />
          </MainLayout>
        }
      />

      {/* Notifications */}
      <Route
        path="/notifications"
        element={
          <MainLayout>
            <NotificationsPage />
          </MainLayout>
        }
      />

      {/* Bookmarks */}
      <Route
        path="/bookmarks"
        element={
          <MainLayout>
            <BookmarksPage />
          </MainLayout>
        }
      />

      {/* Profile */}
      <Route
        path="/profile"
        element={
          <MainLayout>
            <ProfilePage />
          </MainLayout>
        }
      />

      {/* Settings */}
      <Route
        path="/settings"
        element={
          <MainLayout>
            <SettingsPage />
          </MainLayout>
        }
      />
    </Routes>
  );
}