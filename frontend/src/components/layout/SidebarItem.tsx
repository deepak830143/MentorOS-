import { NavLink } from "react-router-dom";
import type { LucideIcon } from "lucide-react";

interface Props {
  title: string;
  path: string;
  icon: LucideIcon;
}

export default function SidebarItem({
  title,
  path,
  icon: Icon,
}: Props) {
  return (
    <NavLink
      to={path}
      className={({ isActive }) =>
        `
        flex items-center
        gap-4
        rounded-2xl
        px-4
        py-3
        transition-all
        duration-300

        ${
          isActive
            ? "bg-blue-600 text-white shadow-lg"
            : "text-slate-600 hover:bg-slate-100"
        }
      `
      }
    >
      <Icon size={22} />

      <span className="font-medium">
        {title}
      </span>
    </NavLink>
  );
}