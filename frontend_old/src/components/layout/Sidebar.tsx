import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Bell,
  Bookmark,
  User,
  Settings,
  LogOut,
  GraduationCap,
} from "lucide-react";

const menuItems = [
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

function Sidebar() {
  return (
    <aside className="w-72 bg-white border-r border-slate-200 shadow-sm flex flex-col justify-between h-screen">

      {/* Logo */}

      <div>

        <div className="flex items-center gap-3 px-8 py-8">

          <div className="bg-blue-600 p-3 rounded-xl">

            <GraduationCap
              size={28}
              className="text-white"
            />

          </div>

          <div>

            <h1 className="text-2xl font-bold text-slate-800">
              MentorOS
            </h1>

            <p className="text-sm text-slate-500">
              Career Platform
            </p>

          </div>

        </div>

        {/* Menu */}

        <nav className="mt-8 px-4">

          {menuItems.map((item) => {

            const Icon = item.icon;

            return (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `flex items-center gap-4 rounded-xl px-5 py-4 mb-3 transition-all duration-200 ${
                    isActive
                      ? "bg-blue-600 text-white shadow-lg"
                      : "text-slate-700 hover:bg-slate-100"
                  }`
                }
              >

                <Icon size={22} />

                <span className="font-medium">
                  {item.title}
                </span>

              </NavLink>
            );
          })}

        </nav>

      </div>

      {/* Bottom */}

      <div className="px-4 pb-8">

        <button
          className="
            flex
            items-center
            gap-4
            w-full
            rounded-xl
            px-5
            py-4
            text-red-500
            hover:bg-red-50
            transition
          "
        >

          <LogOut size={22} />

          <span className="font-medium">
            Logout
          </span>

        </button>

      </div>

    </aside>
  );
}

export default Sidebar;