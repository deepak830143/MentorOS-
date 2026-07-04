import {
  LayoutDashboard,
  Bell,
  Bookmark,
  User,
  Settings,
} from "lucide-react";

export const navigation = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/dashboard",
  },
  {
    title: "Notifications",
    icon: Bell,
    path: "/notifications",
  },
  {
    title: "Bookmarks",
    icon: Bookmark,
    path: "/bookmarks",
  },
  {
    title: "Profile",
    icon: User,
    path: "/profile",
  },
  {
    title: "Settings",
    icon: Settings,
    path: "/settings",
  },
];