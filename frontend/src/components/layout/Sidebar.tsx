import Logo from "./Logo";
import SidebarItem from "./SidebarItem";
import UserCard from "./UserCard";

import { navigation } from "../../constants/navigation";

export default function Sidebar() {
  return (
    <aside
      className="
      fixed
      left-0
      top-0
      z-50
      flex
      h-screen
      w-80

      flex-col
      border-r
      border-slate-200
      bg-white
      shadow-sm
    "
    >
      <div className="border-b border-slate-200 p-6">
        <Logo />
      </div>

      <nav className="flex-1 space-y-2 overflow-y-auto p-4">
        {navigation.map((item) => (
          <SidebarItem
            key={item.path}
            title={item.title}
            path={item.path}
            icon={item.icon}
          />
        ))}
      </nav>

      <div className="border-t border-slate-200 p-4">
        <UserCard
          name="Deepak"
          role="Career Explorer"
        />
      </div>
    </aside>
  );
}