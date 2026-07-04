import {
    LayoutDashboard,
    Bell,
    Bookmark,
    User,
    Settings
} from "lucide-react";

export const navigation = [

    {
        title: "Dashboard",
        icon: LayoutDashboard,
        href: "/dashboard"
    },

    {
        title: "Notifications",
        icon: Bell,
        href: "/notifications"
    },

    {
        title: "Bookmarks",
        icon: Bookmark,
        href: "/bookmarks"
    },

    {
        title: "Profile",
        icon: User,
        href: "/profile"
    },

    {
        title: "Settings",
        icon: Settings,
        href: "/settings"
    }

];